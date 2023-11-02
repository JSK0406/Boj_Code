const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const N = +input.shift();
const numList = input.shift().split(' ').map(Number);
const dp = Array(N).fill(999999999);
dp[0] = 0;

for (let i = 0; i < N-1; i++) {
    const nowNum = numList[i];
    for (let j = i + 1; j < i + nowNum + 1; j++) {
        if (j >= N) {
            break;
        }
        dp[j] = Math.min(dp[i] + 1, dp[j]);
    }
}

if (dp[N-1] === 999999999) {
    console.log(-1)
} else {
    console.log(dp[N-1])
}