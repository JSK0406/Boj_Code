const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

let ans = 0;
input.map((num) => {ans += Number(num)})
console.log(ans)