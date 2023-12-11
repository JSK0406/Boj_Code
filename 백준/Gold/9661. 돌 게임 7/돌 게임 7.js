const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
// let input = fs.readFileSync(filePath).toString().split('\n');
let input = fs.readFileSync(filePath).toString().trim().split('\n');

let N = Number(input.shift().trim());

if ([2, 0].includes(N % 5)) {
    console.log('CY')
} else {
    console.log('SK')
}

// 1 => SK
// 2 => CY
// 3 => SK
// 4 => SK
// 5 => CY
// 6 => SK
// 7 => CY
// 8 => SK
// 9 => SK
// 10 => CY