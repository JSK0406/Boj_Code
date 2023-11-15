const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const N = Number(input.shift());

const numList = input.map(Number);
const dp = Array(N).fill(1);

let maxCount = 0;
for (let idx = 0; idx < N; idx++) {
    for (let moveIdx = idx; 0 <= moveIdx; moveIdx--) {
        if (numList[idx] > numList[moveIdx]) {
            dp[idx] = Math.max(dp[moveIdx] + 1, dp[idx])
        }
    }
    maxCount = Math.max(dp[idx], maxCount)
}

console.log(N - maxCount)