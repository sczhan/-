onload=function(){
    let rdos=document.getElementsByName("site");
    for(let i=0;i<rdos.length;i++){
        rdos[i].onchange=changeSite;
    }

    function changeSite(){
        let chk;
        for(let i=0;i<rdos.length;i++){
            if(rdos[i].checked){
                chk=rdos[i];
            }
        }
        let img=document.getElementsByTagName("img")[0];
        let btn=document.getElementsByTagName("button")[0];
        let frm=document.getElementsByTagName("form")[0];

        if(chk.value=="360"){
            img.src="imgs/360.jpg";
            btn.innerHTML="360搜索";
            frm.action="https://www.so.com/s";
            txt.name="q";
        }
        else if(chk.value=="baidu"){
            img.src="imgs/baidu.jpg";
            btn.innerHTML="百度搜索";
            frm.action="https://www.baidu.com/s";
            txt.name="wd";
        }
        else{
            img.src="imgs/google.jpg";  // 没有搜狗图片,就用谷歌图片先代替了
            btn.innerHTML="搜狗搜索";
            frm.action="https://www.sogou.com/web";
            txt.name="query";
        }
    }
};
