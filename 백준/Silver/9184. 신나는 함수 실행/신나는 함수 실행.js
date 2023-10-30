const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const dp = Array.from({length: 102}, () => Array.from({length: 102}, () => Array(102).fill(null)));

function recursion(a, b, c) {
    if (dp[a+50][b+50][c+50] !== null) {
        return dp[a+50][b+50][c+50]
    }
    if (a <= 0 || b <= 0 || c <= 0) {
        dp[a+50][b+50][c+50] = 1;
        return dp[a+50][b+50][c+50]
    }
    if (a > 20 || b > 20 || c > 20) {
        dp[a+50][b+50][c+50] = recursion(20, 20, 20);
        return dp[a+50][b+50][c+50]
    }
    if (a < b && b < c) {
        dp[a+50][b+50][c+50] = recursion(a, b, c-1) + recursion(a, b-1, c-1) - recursion(a, b-1, c);
        return dp[a+50][b+50][c+50]
    }
    dp[a+50][b+50][c+50] = recursion(a-1, b, c) + recursion(a-1, b-1, c) + recursion(a-1, b, c-1) - recursion(a-1, b-1, c-1);
    return dp[a+50][b+50][c+50]
}

while (true) {
    const [a, b, c] = input.shift().split(' ').map(Number);
    if (a === -1 && b === -1 && c === -1) {
        break;
    }
    console.log(`w(${a}, ${b}, ${c}) = ${recursion(a, b, c)}`);
}
