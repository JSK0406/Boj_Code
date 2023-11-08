const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const N = Number(input.shift());

// 1: 상근, 2: 창영

if (N % 7 === 2 || N % 7 === 0) {
    console.log('CY');
} else {
    console.log('SK');
}

// 1 : 상근
// 2 : 창영
// 3 : 상근
// 4 : 상근
// 5 : 상근
// 6 : 상근
// 7 : 창영