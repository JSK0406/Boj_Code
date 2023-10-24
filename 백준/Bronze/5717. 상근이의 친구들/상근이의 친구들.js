const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

while (true) {
    const [A, B] = input.shift().split(' ').map(Number);
    if (A === 0 && B === 0) {
        break;
    }
    console.log(A + B)
}