const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const N = +input.shift();

const dp = Array(50001).fill(99999);

initNum = 1;
while (true) {
    powNum = initNum ** 2;
    dp[powNum] = 1;
    if (powNum > N) {
        break;
    }
    for (let i = 1; i < 50001; i++) {
        dp[i + powNum] = Math.min(dp[i + powNum], dp[i] + 1);
    }
    initNum += 1;
}

console.log(dp[N]);