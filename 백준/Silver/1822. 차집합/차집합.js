const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const [N, M] = input.shift().split(' ').map(Number);
const nList = input.shift().split(' ').map(Number).sort((a, b) => a-b);
const mSet = new Set(input.shift().split(' ').map(Number));

const diff = nList.filter((n) => !mSet.has(n))

console.log(diff.length)
console.log(diff.join(' '))