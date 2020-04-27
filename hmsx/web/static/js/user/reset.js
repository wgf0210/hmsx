;
var user_reset_ops = {
    init:function(){
        this.eventBind()
    },
    eventBind:function(){
        $('#save').click(function(){
            var btn_target = $(this)
            if (btn_target.hasClass('disabled')){
                alert('请求正在进行，请稍后再试~~')
                return
            }
            var old_password = $('#old_password').val()
            var new_password = $('#new_password').val()
            console.log(old_password,new_password)
            if (!old_password || old_password.length<6){
                alert('请输入正确的旧密码！')
                return false;
            }
            if (!new_password || new_password.length<6){
                alert('请输入符合规范的新密码！')
                return false;
            }
            if (new_password === old_password){
                alert('新密码与旧密码不能一致！')
                return false;
            }
            btn_target.addClass('disabled')
            $.ajax({
                url:common_ops.buildUrl('/user/resetpwd/'),
                type:'POST',
                data:{'old_password':old_password,'new_password':new_password},
                dataType:'json',
                success:function(resp){
                    alert(resp.msg)
                    console.log(resp)
                    btn_target.removeClass('disabled')
                },
                error:function(error){
                    console.log(error)
                }
            })
        })
    }
}
$(document).ready(function(){
    user_reset_ops.init()
})