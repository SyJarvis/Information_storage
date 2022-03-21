;
var user_login_ops = {
    init:function(){
        this.eventBind()
    },
    eventBind:function(){
        $(".login .do-login").click(function () {
            var username = $(".login input[name=username]").val();
            var password = $(".login input[name=password]").val();
            if (username == undefined || username.length < 1){
                return;
            }

            if (password == undefined || password.length < 6){
                return;
            }
            var datas = {
                'username': username,
                'password': password
            };
            $.ajax({
                url: "/user/login",
                type: "POST",
                data: datas,
                dataType: 'json',
                success:function(res){
                    var callback=null;
                    console.log("登录成功");
                    if (res.code == 200){
                        window.location.href = '/'
                    }

                }

            })
        })
    }
};



$(document).ready(function () {
    user_login_ops.init();
});