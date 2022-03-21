;
var user_register_ops = {
    init:function(){
        this.eventBind()
    },
    eventBind:function(){
        $(".register .do-register").click(function () {
            var username = $(".register input[name=username]").val();
            var phone = $(".register input[name=phone]").val();
            var password1 = $(".register input[name=password1]").val();
            var password2 = $(".register input[name=password2]").val();
            if (username == undefined || username.length < 1){
                return;
            }

            if (phone == undefined || phone.length != 11){
                return;
            }
            var datas = {
                'username': username,
                'phone': phone,
                'password1': password1,
                'password2': password2
            };
            $.ajax({
                url: "/user/register",
                type: "POST",
                data: datas,
                dataType: 'json',
                success:function(res){
                    if (res.code == 200){
                        window.location.href = '/user/login'
                    }

                }

            })
        })
    }
};



$(document).ready(function () {
    user_register_ops.init();
});