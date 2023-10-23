const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const [N, M] = input.shift().split(' ').map(Number);

const mapList = [];
for (let lst of input) {
    mapList.push([...lst.trim()].map(Number))
}

let dp = Array.from({length : N+1}, () => Array(M+1).fill(0))


let ansSide = 0;
for (let row = 0; row < N; row++) {
    for (let col = 0; col < M; col++) {
        if (mapList[row][col] === 0) {
            dp[row+1][col+1] = 0;
        } else {
            dp[row+1][col+1] = Math.min(dp[row+1][col] + 1, dp[row][col+1] + 1, dp[row][col] + 1)
            ansSide = Math.max(ansSide, dp[row+1][col+1])
        }
    }
}

console.log(ansSide ** 2)