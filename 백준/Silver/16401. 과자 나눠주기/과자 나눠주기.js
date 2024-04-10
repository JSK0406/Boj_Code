const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const [M, N] = input.shift().split(' ').map(Number)
const snacks = input.shift().split(' ').map(Number)
snacks.sort((a, b) => b-a)
let [left, right] = [0, snacks[0]]

let ans = 0;
while (left <= right) {
    const num = parseInt((left + right) / 2)
    let cnt = 0;
    
    for (const snack of snacks) {
        cnt += Math.floor(snack / num)
        if (M <= cnt) {
            break;
        }
    }
    if (M <= cnt) {
        left = Math.floor((left + right) / 2) + 1
        ans = Math.max(ans, num)
    } else {
        right = Math.floor((left + right) / 2) - 1
    }
}

console.log(ans);