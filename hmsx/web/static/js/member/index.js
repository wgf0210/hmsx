;
var member_index_ops = {
    init:function(){
        this.eventBind()
    },
    eventBind:function(){
        $('.wrap_search .search').click(function(){
            $('.wrap_search').submit();
        })
        var that = this;
        $('.remove').click(function(){
            id = $(this).attr('data')
            that.myajax(id,'remove')
        })
        $('.recover').click(function(){
            id = $(this).attr('data')
            that.myajax(id,'recover')
        })
    },
    // 封装ajax操作
    myajax:function(id,acts){
        $.ajax({
            url:common_ops.buildUrl('/member/remove-or-recover/'),
            type:'POST',
            data:{
                'id':id,
                'acts':acts
            },
            dataType:'json',
            success:function(resp){
                if (resp.code==200){
                    window.location.href = common_ops.buildUrl('/member/index/')
                }
                alert(resp.msg)
                console.log(resp.msg)
            },
            error:function(error){
                alert('123')
                console.log(error.msg)
                console.log('123')
            }
        })
    }
}

$(document).ready(function(){
    member_index_ops.init()
})