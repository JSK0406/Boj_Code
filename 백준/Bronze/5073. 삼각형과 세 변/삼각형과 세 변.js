const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

while(true) {
  const [A, B, C] = input.shift().trim().split(' ').map(Number)
  if (A === 0 && B === 0 && C === 0) {
    break;
  }
  if (Math.max(A, B, C) >= A+B+C - Math.max(A, B, C)) {
    console.log('Invalid')
    continue;
  }
  if ((new Set([A, B, C]).size === 1)) {
    console.log('Equilateral')
  } else if ((new Set([A, B, C]).size === 2)) {
    console.log('Isosceles')
  } else {
    console.log('Scalene')
  }
}