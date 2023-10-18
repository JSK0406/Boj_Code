const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

let [A, B] = input.shift().split(' ').map(Number)
console.log(A ^ B)