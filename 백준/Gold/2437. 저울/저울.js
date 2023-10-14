const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const N = Number(input.shift())
let scaleList = input.shift().trim().split(' ').map(Number);
scaleList.sort((a, b) => (a - b))

let weightSum = 1
for (const scaleWeight of scaleList) {
    if (weightSum < scaleWeight) {
        break;
    }
    weightSum += scaleWeight
}

console.log(weightSum)