const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const [N, M] = input.shift().split(' ').map(Number);

const apps = input.shift().split(' ').map(Number);
const restartMemory = input.shift().split(' ').map(Number);
restartMemory.unshift(0);
apps.unshift(0);

let sumRestart = 0;
restartMemory.forEach((memory) => sumRestart += memory);

const dp = Array.from({ length: N+1 }, () => Array(sumRestart+1).fill(0));

let ans = 999_999_999;
for (let i = 1; i < restartMemory.length; i++) {
    for (let memory = 0; memory <= sumRestart; memory++) {
        if (restartMemory[i] > memory) {
            dp[i][memory] = dp[i-1][memory];
        } else if (restartMemory[i] === 0) {
                dp[i][memory] = dp[i-1][memory]+apps[i];
        } else {
            dp[i][memory] = Math.max(dp[i-1][memory-restartMemory[i]]+apps[i], dp[i-1][memory])
        }
        if (dp[i][memory] >= M) {
            ans = Math.min(memory, ans);
        }
    }
}

console.log(ans);