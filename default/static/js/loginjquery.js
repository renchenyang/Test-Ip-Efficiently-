$(document).ready(function () {
    $("#username").blur(function () {
        if ($("#username")[0].value == "") {
            $("#warn1").text("请输入您的用户名");
            $("#username").focus();
            return;
        } else {
            $("#warn1").text("");
            return;
        }
    });

    $("#password").blur(function () {
        if ($("#password")[0].value == "") {
            $("#warn2").text("请输入您的密码");
            $("#password").focus();
            return;
        } else {
            $("#warn2").text("");
            return;
        }
        //document.loginForm.submit();
    });
});