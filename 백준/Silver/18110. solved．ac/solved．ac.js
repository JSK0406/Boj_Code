const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const N = Number(input.shift())
const lst = []
input.forEach((num) => lst.push(Number(num)))

if (N == 0) {
    console.log(0)
}
else {
    lst.sort((a, b) => a-b)
    const num = Math.round(N*0.15)
    let totSum = 0;
    for (let i = num; i < N-num; i++) {
        totSum += lst[i]
    }
    console.log(Math.round(totSum/(N-2*num)))
}

