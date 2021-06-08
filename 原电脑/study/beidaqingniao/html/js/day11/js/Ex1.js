for(let i=1; i<10; i++){
    let sum=0;
    let s="";
    for(let j=1; j<=i; j++){
        sum = i*j;
        if (sum<10){
            s += j + "*" +i +"=" + sum + "   ";
        }
        else{
            s += j + "*" +i +"=" + sum + "  ";
        }
    }
    console.log(s)
}