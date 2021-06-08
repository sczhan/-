let n;
let a;
let count=0;
let sum=0;
let average=0;
let list="";
do{
    n=prompt("请输入数字: ");
    a=n*1;
    if (! isNaN(a)){
        list+= n+" ";
        count += 1;
        sum +=a;
        average=sum/count;
    }
}while (n!="end");
console.log("刚才输入的数字是: " + list + "\n个数是: " + count + "\n总和是: " + sum +"\n平均值是: " +average);

// while(1){
//     n=prompt("请输入数字: ");
//     if (n=="end"){
//         break
//     }
//     else{
//         a=n*1;
//         if (! isNaN(a)){
//             list+= n+" ";
//             count += 1;
//             sum +=a;
//             average=sum/count;
//         }
//     }
// }
// console.log("刚才输入的数字是: " + list + "\n个数是: " + count + "\n总和是: " + sum +"\n平均值是: " +average);