alert("密码错误，请重新输入");
function login1() {
    if (document.getElementById("username").value == "") {
        document.getElementById("warn1").innerHTML = "请输入您的用户名";
        document.getElementById("username").focus();
        //return;
    } else {
        document.getElementById("warn1").innerHTML = "";
        //return;
    }
}

function login2() {
    if (document.getElementById("password").value == "") {
        document.getElementById("warn2").innerHTML = "请输入您的密码";
        document.getElementById("password").focus();
        //return;
    } else {
        document.getElementById("warn2").innerHTML = "";
        //return;
    }
    //document.loginForm.submit();
}
function login3() {
    if (document.getElementById("password").value == "" || document.getElementById("username").value == "") {
        alert("请输入用户名和密码!");
        return false;
    }
    else {
        document.getElementById("loginForm").submit();
        return true;
    }
}