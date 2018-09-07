       function drawAndShareImage(){
            var canvas = document.createElement("canvas");
            canvas.width = 700;
            canvas.height = 700;
            var context = canvas.getContext("2d");

            context.rect(0 , 0 , canvas.width , canvas.height);
            context.fillStyle = "#fff";
            context.fill();

            var myImage = new Image();
            myImage.src = "3cd2edc2601a90d212be59f443248744.jpg";    //背景图片  你自己本地的图片或者在线图片
            myImage.crossOrigin = 'Anonymous';

            myImage.onload = function(){
                context.drawImage(myImage , 0 , 0 , 700 , 700);

                context.font = "60px Courier New";
                context.fillText("我是文字",350,450);

                var myImage2 = new Image();
                myImage2.src = "276ad2fc491332aa1cb20aa258650806.jpg";   //你自己本地的图片或者在线图片
                myImage2.crossOrigin = 'Anonymous';
                
                myImage2.onload = function(){
                    context.drawImage(myImage2 , 175 , 175 , 225 , 225);
                    var base64 = canvas.toDataURL("image/png");  //"image/png" 这里注意一下
                    var img = document.getElementById('avatar');

                    // document.getElementById('avatar').src = base64;
                    img.setAttribute('src' , base64);
                }
            }
        }