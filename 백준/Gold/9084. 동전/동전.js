const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const T = Number(input.shift());

for (let _ = 0; _ < T; _++) {
    const N = Number(input.shift());
    const coins = input.shift().split(' ').map(Number);
    coins.unshift(0);
    const price = Number(input.shift());

    const dp = Array(price+1).fill(0);
    dp[0] = 1;
    for (let coin of coins) {
        for (let p = 1; p <= price; p++) {
            if (p-coin >= 0) {
                dp[p] += dp[p-coin];
            }
        }
    }
    console.log(dp[price])
}