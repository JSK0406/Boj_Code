const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

let [N, M] = input.shift().trim().split(' ')

let reversedN = Number(String(N).split('').reverse().join(''))
let reversedM = Number(String(M).split('').reverse().join(''))

console.log(Number(String(reversedN + reversedM).split('').reverse().join('')))