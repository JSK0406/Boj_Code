const { info } = require("console");
const fs = require("fs");
const { brotliCompress } = require("zlib");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const [S, P] = input.shift().split(' ').map(Number);
const dnaStr = input.shift().split('');

let left = 0;
let right = left+P;
const cntArr = input.shift().split(' ').map(Number);  // A C G T

const isPossible = () => {
    for (let i of cntArr) {
        if (i > 0) {
            return false;
        }
    }
    return true;
}

for (let i = 0; i < right; i++) {
    if (dnaStr[i] === 'A') {
        cntArr[0] -= 1
    }
    if (dnaStr[i] === 'C') {
        cntArr[1] -= 1
    }
    if (dnaStr[i] === 'G') {
        cntArr[2] -= 1
    }
    if (dnaStr[i] === 'T') {
        cntArr[3] -= 1
    }
}


let ans = 0;
// left~right+1
// right는 
while (right <= S) {
    if (isPossible()) {
        ans += 1;
    }
    if (right === S) {
        break;
    }

    if (dnaStr[left] === 'A') {
        cntArr[0] += 1
    }
    if (dnaStr[left] === 'C') {
        cntArr[1] += 1
    }
    if (dnaStr[left] === 'G') {
        cntArr[2] += 1
    }
    if (dnaStr[left] === 'T') {
        cntArr[3] += 1
    }

    if (dnaStr[right] === 'A') {
        cntArr[0] -= 1
    }
    if (dnaStr[right] === 'C') {
        cntArr[1] -= 1
    }
    if (dnaStr[right] === 'G') {
        cntArr[2] -= 1
    }
    if (dnaStr[right] === 'T') {
        cntArr[3] -= 1
    }

    left += 1;
    right += 1;
}

console.log(ans)
