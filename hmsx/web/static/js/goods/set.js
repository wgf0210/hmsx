;
var goods_set_ops = {
    init:function(){
        this.eventBind()
        this.initEditor()
    },
    eventBind:function(){
        var that = this
        $('.upload_pic_wrap input[name=pic]').change(function(){
            $('.upload_pic_wrap').submit()
        })
        $('.wrap_goods_set .save').click(function(){
            var btn_target = $(this)
            if (btn_target.hasClass('disabled')){
                alert('请求正在进行，请稍后再试~~')
                return
            }
            var cat_id_target_value = $('.wrap_goods_set input[name=cat_id]').val()
            var name_target_value = $('.wrap_goods_set input[name=name]').val()
            var price_target_value = $('.wrap_goods_set input[name=price]').val()
            var summary = $.trim('sssssssssssss')
            var stock_target_value = $('.wrap_goods_set input[name=stock]').val()
            var tags_target_value = $.trim($('.wrap_goods_set input[name=tags]').val())
            if (parseInt(cat_id_target_value < 1)){
                alert('请选择分类')
                return
            }
            if (name_target_value.length < 1){
                alert('请输入符合规范的昵称')
                return false;
            }
            if (parseInt(price_target_value < 1)){
                alert('请输入售价')
                return
            }
            if ($('.wrap_goods_set .pri-each').length<1){
                alert('请上传封面')
                return
            }
            if (parseInt(stock_target_value < 1)){
                alert('请输入库存')
                return
            }
            if (tags_target_value.length <1){
                alert('请输入标签，以便搜索')
                return
            }
            if (summary.length < 10){
                alert('请输入描述，不少于10~~')
                return false;
            }
            
            btn_target.addClass('disabled')

            var data = {
                cat_id:cat_id_target_value,
                name:name_target_value,
                price:price_target_value,
                main_image:$('.wrap_goods_set .pic-each .del_image').attr('data'),
                summary:summary,
                stock:stock_target_value,
                tags:tags_target_value,
                id:$('.wrap_goods_set input[name=id]').val()
            }

            $.ajax({
                url:common_ops.buildUrl('/goods/set/'),
                type:'POST',
                data:data,
                dataType:'json',
                success:function(resp){
                    alert(resp.msg)
                    console.log(resp.msg)
                    btn_target.removeClass('disabled')
                    if(resp.code == 200){
                        window.location.href = common_ops.buildUrl('/goods/index/')
                    }
                },
                error:function(error){
                    console.log(error)
                }
            })
        })
    },
    initEditor:function(){
        var that = this
        that.ue = UE.getEditor('editor', {
            toolbars: [
                [
                    'fullscreen', 'source', '|', 'undo', 'redo', '|',
                    'bold', 'italic', 'underline', 'fontborder', 'strikethrough', 'superscript', 'subscript', 'removeformat', 'formatmatch', 'autotypeset', 'blockquote', 'pasteplain', '|', 'forecolor', 'backcolor', 'insertorderedlist', 'insertunorderedlist', 'selectall', 'cleardoc', '|',
                    'rowspacingtop', 'rowspacingbottom', 'lineheight', '|',
                    'customstyle', 'paragraph', 'fontfamily', 'fontsize', '|',
                    'directionalityltr', 'directionalityrtl', 'indent', '|',
                    'justifyleft', 'justifycenter', 'justifyright', 'justifyjustify', '|', 'touppercase', 'tolowercase', '|',
                    'link', 'unlink', 'anchor', '|', 'imagenone', 'imageleft', 'imageright', 'imagecenter', '|',
                    'simpleupload', 'insertimage', 'emotion', 'scrawl', 'insertvideo', 'music', 'attachment', 'map', 'gmap', 'insertframe', 'insertcode', 'webapp', 'pagebreak', 'template', 'background', '|',
                    'horizontal', 'date', 'time', 'spechars', 'snapscreen', 'wordimage', '|',
                    'inserttable', 'deletetable', 'insertparagraphbeforetable', 'insertrow', 'deleterow', 'insertcol', 'deletecol', 'mergecells', 'mergeright', 'mergedown', 'splittocells', 'splittorows', 'splittocols', 'charts', '|',
                    'print', 'preview', 'searchreplace', 'drafts', 'help'
                ]
            ],
            autoHeightEnabled: true,
            autoFloatEnabled: true,
            // 自动保存：出现本地保存成功
            enableAutoSave:true,
            serverUrl:common_ops.buildUrl('/upload/ueditor')
        });
    },
    delete_img:function(){

    }
}

$(document).ready(function(){
    goods_set_ops.init()
})