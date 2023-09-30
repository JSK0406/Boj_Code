const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const AList = input.shift().trim().split('');
AList.unshift(null);
const BList = input.shift().trim().split('');
BList.unshift(null);
const CList = input.shift().trim().split('');
CList.unshift(null);

let dp = Array.from({length : AList.length + 1}, () => Array.from({length : BList.length + 1}, () => Array(CList.length + 1).fill(0)));

for (a=1; a<AList.length+1; a++) {
    for (b = 1; b < BList.length+1; b++) {
        for (c = 1; c < CList.length+1; c++) {
            if (AList[a] === BList[b] && CList[c] === BList[b]) {
                dp[a][b][c] = dp[a-1][b-1][c-1] + 1;
            } else {
                dp[a][b][c] = Math.max(dp[a - 1][b][c], dp[a][b - 1][c], dp[a][b][c - 1])
            }
        }
    }
}

console.log(dp[AList.length-1][BList.length-1][CList.length-1])