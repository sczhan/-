let n;
let a;
do{
    n=prompt("请输入正整数")
    a=n*1
}while(isNaN(a) || parseInt(n)!=a || a<0);
for (let i=1; i <= 2 * n - 1; i++) {
    let s = "";
    if (i <= n) {
        for (let j=1; j<= n - i; j++) {
            s += "  "
        }
        for (let k=1; k<= i; k++) {
            s += " *  "
        }
       console.log(s)
    } else {
        for (let j=1; j<=i-n; j++) {
            s += "  "
        }
        for (let k=i; k <= 2*n-1; k++) {
            s += " *  "
        }
        console.log(s)
    }
}