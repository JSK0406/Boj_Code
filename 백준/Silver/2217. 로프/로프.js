const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const N = Number(input.shift())

let numList = input.map(Number)

numList.sort((a, b) => a - b)
let maxAns = 0;

for (let i = 0; i < N; i++) {
    maxAns = Math.max(numList.shift() * (numList.length + 1), maxAns)
}

console.log(maxAns)
// console.log(numList[0] * numList.length)