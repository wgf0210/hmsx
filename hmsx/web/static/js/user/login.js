;
// console.log('aaaa')
var user_login_ops = {
    init:function(){
        this.eventBind()
    },
    eventBind:function(){
        console.log('click')
        $('.login_wrap .do-login').click(function(){
            var login_name = $('.login_wrap input[name=login_name]').val()
            var login_pwd = $('.login_wrap input[name=login_pwd]').val()

            console.log(login_name)
            console.log(login_pwd)
        })
    }
}
$(document).ready(function(){
    user_login_ops.init()
})