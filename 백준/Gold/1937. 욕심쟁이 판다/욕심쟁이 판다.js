const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const N = Number(input.shift());
const mapList = Array.from({ length: N }, () => input.shift().split(' ').map(Number));
const dp = Array.from({ length: N }, () => Array(N).fill(0));


const dfs = (row, col) => {
    if (dp[row][col] !== 0) {
        return dp[row][col];
    }
    dp[row][col] = 1;
    for (let i = 0; i < 4; i++) {
        const [nr, nc] = [[0, -1], [0, 1], [1, 0], [-1, 0]][i];
        const [nextRow, nextCol] = [row + nr, col + nc];
        if (0 <= nextRow && nextRow < N && 0 <= nextCol && nextCol < N && mapList[row][col] < mapList[nextRow][nextCol]) {
            dp[row][col] = Math.max(dp[row][col], dfs(nextRow, nextCol) + 1);
        }
    }
    return dp[row][col]
}

let ans = 0;
for (row = 0; row < N; row++) {
    for (col = 0; col < N; col++) {
        ans = Math.max(ans, dfs(row, col))
    }
}

console.log(ans);