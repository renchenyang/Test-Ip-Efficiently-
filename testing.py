#!/usr/bin/env python
# -*- coding: UTF-8 -*-
 
import os, sys, socket, struct, select, time,thread,sqlite3
 
# From /usr/include/linux/icmp.h; your milage may vary.
ICMP_ECHO_REQUEST = 8 # Seems to be the same on Solaris.
 
def checksum(source_string):
    sum = 0
    countTo = (len(source_string)/2)*2
    count = 0
    while count<countTo:
        thisVal = ord(source_string[count + 1])*256 + ord(source_string[count])
        sum = sum + thisVal
        sum = sum & 0xffffffff 
        count = count + 2
 
    if countTo<len(source_string):
        sum = sum + ord(source_string[len(source_string) - 1])
        sum = sum & 0xffffffff 
 
    sum = (sum >> 16)  +  (sum & 0xffff)
    sum = sum + (sum >> 16)
    answer = ~sum
    answer = answer & 0xffff
 
    answer = answer >> 8 | (answer << 8 & 0xff00)
 
    return answer
 
 
def receive_one_ping(my_socket, ID, timeout):
    """
    receive the ping from the socket.
    """
    cx = sqlite3.connect(os.path.abspath('.')+"db.sqlite3")
    cu=cx.cursor()
    cu.execute("select ip from default_todolist") 
    iplist=cu.fetchall()
    while True:
        whatReady = select.select([my_socket], [], [], timeout)
        if whatReady[0] == []: # Timeout
            break
        else:
            recPacket, addr = my_socket.recvfrom(1024)
            add,m=addr
            cu.execute("select * from default_todolist where ip=(?)",(add,)) 
            the_arrive_ip=cu.fetchall()
            if the_arrive_ip:
                iplist.remove((add,))
                cu.execute("update default_todolist set state=1 where ip=(?)",(add,))
                cx.commit()
                cu.execute("select * from default_historydata where ip=(?) order by state desc",(add,)) 

                items=cu.fetchall()
                if items:
                    ladb2_item=items[0]
                    item_id,item_add,item_time,item_state=ladb2_item
                    if item_state==0:
                        cu.execute("select * from default_historydata") 
                        items2=cu.fetchall()
                        t = (len(items2)+1,add,time.time(),1)
                        cx.execute("insert into default_historydata values (?,?,?,?)", t)
                        cx.commit()
                else:
                    cu.execute("select * from default_historydata") 
                    items2=cu.fetchall()
                    t = (len(items2)+1,add,time.time(),1)
                    cx.execute("insert into default_historydata values (?,?,?,?)", t)
                    cx.commit()
    for i in iplist:
        cu.execute("update default_todolist set state=0 where ip=(?)",i)
        cx.commit()
        cu.execute("select * from default_historydata where ip=(?) order by state desc",i) 
        items=cu.fetchall()
        if items:
            ladb2_item=items[0]
            item_id,item_add,item_time,item_state=ladb2_item
            if item_state==1:
                cu.execute("select * from default_historydata") 
                items2=cu.fetchall()
                t = (len(items2)+1,i[0],time.time(),0)
                cx.execute("insert into default_historydata values (?,?,?,?)", t)
                cx.commit()
        else:
            cu.execute("select * from default_historydata") 
            items2=cu.fetchall()
            t = (len(items2)+1,i[0],time.time(),0)
            cx.execute("insert into default_historydata values (?,?,?,?)", t)
            cx.commit()
    cu.execute("select * from default_historydata") 

def send_one_ping(my_socket, dest_addr, ID):

    # Header is type (8), code (8), checksum (16), id (16), sequence (16)
    my_checksum = 0
    
    # Make a dummy heder with a 0 checksum.
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, my_checksum, ID, 1)
    bytesInDouble = struct.calcsize("d")
    data = (192 - bytesInDouble) * "Q"
    data = struct.pack("d", time.time()) + data

    my_checksum = checksum(header + data)
    header = struct.pack(
        "bbHHh", ICMP_ECHO_REQUEST, 0, socket.htons(my_checksum), ID, 1
    )
    packet = header + data
    cx = sqlite3.connect(os.path.abspath('.')+"db.sqlite3")
    cu=cx.cursor()

    cu.execute("select * from default_todolist") 
    for item in cu.fetchall():
        the_id,dest_addr,n = item
        my_socket.sendto(packet, (dest_addr, 1))   

if __name__ == '__main__':
    cx = sqlite3.connect(os.path.abspath('.')+"db.sqlite3")
    cu=cx.cursor()
  
    try:
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.getprotobyname("icmp"))
    except socket.error, (errno, msg):
        if errno == 1:
            # Operation not permitted
            msg = msg + (
                " - Note that ICMP messages can only be sent from processes"
                " running as root."
            )
            raise socket.error(msg)
        raise # raise the original error

    my_ID = os.getpid() & 0xFFFF

    address = ('localhost', 9999)  
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    s.bind(address)
    s.listen(5) 

    while 1:
        thread.start_new_thread( receive_one_ping, (my_socket, my_ID, 2) )
        thread.start_new_thread( send_one_ping, (my_socket, "www.baidu.com", my_ID) )
        time.sleep(3)
        whatReady = select.select([s], [], [], 27)
        s.close()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        s.bind(address)
        s.listen(5) 
    
    s.close()
    my_socket.close()

    sys.exit(0)