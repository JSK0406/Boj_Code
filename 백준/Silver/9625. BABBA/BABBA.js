const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const K = +input.shift();

const dp = Array.from({length: K+1}, () => Array(2).fill(0));
// A, B 개수
dp[1][0] = 0;
dp[1][1] = 1;

for (let i = 2; i < K+1; i++) {
    dp[i][0] = dp[i-1][1];
    dp[i][1] = dp[i-1][1] + dp[i-1][0];
}

console.log(dp[K][0], dp[K][1])