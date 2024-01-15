const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const T = Number(input.shift());

const infoArr = [0];

for (let i = 0; i < T; i++) {
    const [a, b] = input[i].split(' ').map(Number);
    infoArr.push([a, b]);
}

const dp = Array(T+1).fill(0);

for (let day = 1; day <= T; day++) {
    const [time, price] = infoArr[day];

    dp[day] = Math.max(dp[day-1], dp[day]);

    if (day-1+time > T) {
        continue;
    }
    dp[day-1+time] = Math.max(dp[day-1]+price, dp[day-1+time]);
}

console.log(dp[T]);