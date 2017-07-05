判断访问方式
            dump(request()->isPost());

验证码<img src="{:captcha_src()}" alt="验证码" style="width:150px;" onclick="this.src='{:captcha_src()}?'+Math.random()" />
if(!captcha_check($captcha)){
//验证失败
};

