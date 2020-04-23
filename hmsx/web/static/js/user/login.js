;
// console.log('aaaa')
var user_login_ops = {
    init:function(){
        this.eventBind()
    },
    eventBind:function(){
        console.log('click')
        $('.login_wrap .do-login').click(function(){
            var btn_target = $(this)
            if (btn_target.hasClass('disabled')){
                alert('请不要重复提交,检测到你有一笔提交尚未完成！')
                return;
            }
            var login_name = $('.login_wrap input[name=login_name]').val()
            var login_pwd = $('.login_wrap input[name=login_pwd]').val()
            console.log(login_name)
            // 前端校检 不为空，长度不小于1
            if(login_name == undefined || login_name.length<1){
                alert('输入的用户名为空')
                return;
            }
            if(login_pwd == undefined || login_pwd.length<1){
                alert('输入的密码为空')
                return;
            }
            btn_target.addClass('disabled')
            // Ajax 用来做前后端分离，数据格式是json{key:value}
            // 前端发送的数据是json格式，要求后端范蝴蝶数据也是json格式
            $.ajax({
                url:'/user/login',
                type:'POST',
                data:{'login_name':login_name,'login_pwd':login_pwd},
                dataType:'json',
                success:function(response){
                    btn_target.removeClass('disabled')
                    console.log(response)
                }
            })
        })
    }
}
$(document).ready(function(){
    user_login_ops.init()
})