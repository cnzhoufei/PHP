
//判断设备
function isPc() {
    var userAgentInfo = navigator.userAgent;
    var Agents = ["Android", "iPhone",
                "SymbianOS", "Windows Phone",
                "iPad", "iPod"];
    var flag = true;
    for (var v = 0; v < Agents.length; v++) {
        if (userAgentInfo.indexOf(Agents[v]) > 0) {
            flag = false;
            break;
        }
    }
    return flag;
}
//图片懒加载
function loadimg(){
    height = window.innerHeight;
    imgdata = $('[data-src]')
    for(i = 0;i < imgdata.length;i++){
        sTop = $(window).scrollTop();//滚动条顶部高度
        mtop = $(imgdata[i]).offset().top;//当前元素位置
        activity = mtop - sTop;
        if (activity < (height - 120) && activity > 50){
            $(imgdata[i]).attr('src',$(imgdata[i]).attr('data-src'));
        }
    }
}

//base64上传图片
function upload(obj){
   var reader = new FileReader();
    var AllowImgFileSize = 2100000; //上传图片最大值(单位字节)（ 2 M = 2097152 B ）超过2M上传失败
    var file = obj.files[0];
    var imgUrlBase64;
    if (file) {
        //将文件以Data URL形式读入页面  
        imgUrlBase64 = reader.readAsDataURL(file);
        reader.onload = function (e) {
          if (AllowImgFileSize != 0 && AllowImgFileSize < reader.result.length) {
                alert( '上传失败，请上传不大于2M的图片！');
                return;
            }else{
                //执行上传操作
                // alert(reader.result);
                $('#img').attr('src',reader.result)
                $('input[name=img]').val(reader.result);
            }
        }
     }
}

