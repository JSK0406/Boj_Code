const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

let AList = input.shift().trim().split('')
let BList = input.shift().trim().split('')
let ALen = AList.length
let BLen = BList.length

let dp = Array.from({ length: ALen }, () => Array(BLen).fill(0));
let visitedList = Array.from({ length: ALen }, () => Array(BLen).fill(0));
for (a=0; a<ALen; a++) {
    for (b=0; b<BLen; b++) {
        if (AList[a] === BList[b]) {
            dp[a][b] = 1
        }
    }
}

let ans = 0;
for (a = 0; a < ALen; a++) {
    for (b = 0; b < BLen; b++) {
        startA = a;
        startB = b;
        if (!visitedList[startA][startB] && dp[startA][startB] === 1) {
            let cnt = 0;
            while (startA<ALen && startB<BLen && dp[startA][startB] === 1 && !visitedList[startA][startB]) {
                visitedList[startA][startB] = 1
                cnt += 1;
                startA += 1;
                startB += 1;
            }
            ans = Math.max(ans, cnt)
        }
    }
}

console.log(ans)