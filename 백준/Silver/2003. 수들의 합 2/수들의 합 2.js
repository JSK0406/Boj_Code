const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const [N, M] = input.shift().split(' ').map(Number);
const numList = input.shift().split(' ').map(Number);
let sumList = [0];

let sum = 0;
for (let num of numList) {
    sum += num;
    sumList.push(sum);
}

let left = 0;
let right = 1;

let ans = 0;
while (right < sumList.length) {
    nowSum = sumList[right] - sumList[left];
    if (nowSum === M) {
        ans += 1;
        right += 1;
    } else if (nowSum < M) {
        right += 1;
    } else {
        left += 1;
    }
}

console.log(ans);