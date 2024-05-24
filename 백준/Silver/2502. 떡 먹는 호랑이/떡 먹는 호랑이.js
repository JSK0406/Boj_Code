const fs = require("fs");
const { brotliCompress } = require("zlib");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

// 할머니가 넘어온 날, 그 날 호랑이에게 준 떡의 개수
const [D, K] = input.shift().split(' ').map(Number);
// 2 7 9 16 25 41
// 2
// 7
// 2 + 7
// 7 + (2 + 7 )
// (2 + 7 ) + 7 + (2 + 7)
//

// 첫번째 수 A, 두번째 수 B
const dp = Array(D+1).fill(0)
dp[1] = {'A': 1, 'B': 0}
dp[2] = {'A': 0, 'B': 1}

for (let i = 3; i <= D; i++) {
    const [nowA, nowB] = [dp[i-1]['A'] + dp[i-2]['A'], dp[i-1]['B'] + dp[i-2]['B']];
    dp[i] = {'A': nowA, 'B': nowB}
}

for (let aCnt = 1; aCnt <= K; aCnt++) {
    if ((K - aCnt * dp[D]['A']) % dp[D]['B'] === 0) {
        console.log(aCnt)
        console.log((K - aCnt * dp[D]['A']) / dp[D]['B'])
        break;
    }
}