const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const [N, X] = input.shift().split(' ').map(Number);
const numList = input.shift().split(' ').map(Number);

let sum = 0;
for (let i = 0; i < X; i++) {
    sum += numList[i];
}

let ansSum = sum;
let cnt = 1;
for (let i = X; i < N; i++) {
    sum -= numList[i-X];
    sum += numList[i];
    if (ansSum === sum) {
        cnt += 1;
    } else if (ansSum < sum) {
        ansSum = sum;
        cnt = 1;
    }
}

if (ansSum === 0) {
    console.log('SAD')
} else {
    console.log(ansSum);
    console.log(cnt);
}
