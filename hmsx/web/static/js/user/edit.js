;
var user_edit_ops = {
    init:function(){
        this.eventBind()
    },
    eventBind:function(){
        $('.user_edit_wrap .save').click(function(){
            var btn_target = $(this)
            if (btn_target.hasClass('disabled')){
                alert('请求正在进行，请稍后再试~~')
                return
            }
            var nickname_value = $('.user_edit_wrap input[name=nickname]').val()
            var email_value = $('.user_edit_wrap input[name=email]').val()
            console.log(nickname_value,email_value)
            if (!nickname_value || nickname_value.length<2){
                alert('请输入符合规范的昵称')
                return false;
            }
            if (!email_value || email_value.length<2){
                alert('请输入符合规范的邮箱')
                return false;
            }
            btn_target.addClass('disabled')
            $.ajax({
                url:common_ops.buildUrl('/user/edit/'),
                type:'POST',
                data:{'nickname':nickname_value,'email':email_value},
                dataType:'json',
                success:function(resp){
                    alert(resp.msg)
                    console.log(resp.msg)
                    
                },
                error:function(error){
                    console.log(error)
                }
            })
        })
    }
}
$(document).ready(function(){
    user_edit_ops.init()
})