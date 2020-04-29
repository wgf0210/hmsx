;
var account_index_ops = {
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
            // $.ajax({
            //     url:common_ops.buildUrl('/account/remove-or-recover/'),
            //     type:'POST',
            //     data:{
            //         'id':id,
            //         'acts':'remove'
            //     },
            //     dataType:'json',
            //     success:function(resp){
            //         if (resp.code==200){
            //             window.location.gref = common_ops.buildUrl('/account/index/')
            //         }
            //         alert(resp.msg)
            //         console.log(resp.msg)
            //     },
            //     error:function(error){
            //         console.log(error.msg)
            //     }
            // })
        })
        $('.recover').click(function(){
            id = $(this).attr('data')
            that.myajax(id,'recover')
            // $.ajax({
            //     url:common_ops.buildUrl('/account/remove-or-recover/'),
            //     type:'POST',
            //     data:{
            //         'id':id,
            //         'acts':'recover'
            //     },
            //     dataType:'json',
            //     success:function(resp){
            //         if (resp.code==200){
            //             window.location.gref = common_ops.buildUrl('/account/index/')
            //         }
            //         alert(resp.msg)
            //         console.log(resp.msg)
            //     },
            //     error:function(error){
            //         console.log(error.msg)
            //     }
            // })
        })
    },
    // 封装ajax操作
    myajax:function(id,acts){
        $.ajax({
            url:common_ops.buildUrl('/account/remove-or-recover/'),
            type:'POST',
            data:{
                'id':id,
                'acts':acts
            },
            dataType:'json',
            success:function(resp){
                if (resp.code==200){
                    window.location.gref = common_ops.buildUrl('/account/index/')
                }
                alert(resp.msg)
                console.log(resp.msg)
            },
            error:function(error){
                console.log(error.msg)
            }
        })
    }
}

$(document).ready(function(){
    account_index_ops.init()
})