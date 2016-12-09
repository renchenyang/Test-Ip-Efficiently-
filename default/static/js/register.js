function login3() {
    if (document.getElementById("field3").value == "") {
        document.getElementById("warn3").innerHTML = "请输入要监听的Ip地址";
        document.getElementById("field3").focus();
        return false;
    } else {
        document.getElementById("warn3").innerHTML = "";
        var GetInputValue = document.getElementById("field3").value;
        if (checkemail(GetInputValue) == false) {
            document.getElementById("warn3").innerHTML = "请输入正确的Ip地址格式";
            return false;
        }
        document.getElementById("warn3").innerHTML = "";
        return true;
    }
}

function checkemail(value) {
    var Regx = /^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$/;
    if (Regx.test(value) == true) {
        return true;
    } else {
        return false;
    }
}

function login6() {
    if (login3())
        document.getElementById("test").submit();
}

function login4() {
    if (document.getElementById("field4").value == "") {
        document.getElementById("warn4").innerHTML = "请输入要监听的网段的网络号长度";
        document.getElementById("field4").focus();
        return false;
    } else {
        document.getElementById("warn4").innerHTML = "";
        var GetInputValue = document.getElementById("field4").value;
        if (checklength(GetInputValue) == false) {
            document.getElementById("warn4").innerHTML = "请输入由纯数字组成的长度且范围为0~32";
            return false;
        }
        document.getElementById("warn4").innerHTML = "";
        return true;
    }
}

function checklength(value) {
    if (isNaN(value)) {
        return false;
    } else if (value >= 0 && value <= 32)
        return true;
    else
        return false;
}

function login7() {
    if (login3()&&login4())
        document.getElementById("test").submit();
}