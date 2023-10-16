const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const T = Number(input.shift())

for (let _ = 0; _ < T; _++) {
    const K = Number(input.shift())
    let pageList = input.shift().split(' ').map(Number);
    const sumList = [0]
    let sum = 0;
    pageList.forEach((num) => {sum+=num; sumList.push(sum)})

    // start, end
    let dp = Array.from({length: K}, () => Array(K).fill(999999999));

    for (end = 0; end < K; end++) {
        for (start = end; start >= 0; start--) {
            if (start === end) {
                dp[start][end] = 0;
            } else {
                const idx = end - start;
                for (i = 0; i < idx; i++) {
                    dp[start][end] = Math.min(dp[start][end], dp[start][end-idx+i] + dp[start + 1 + i][end] + sumList[end + 1] - sumList[start])
                    // dp[start][end] = Math.min(dp[start][end], dp[start][end-idx+i] + dp[start + 1 + i][end])
                }
            }
        }
    }
    console.log(dp[0][K-1])
}
