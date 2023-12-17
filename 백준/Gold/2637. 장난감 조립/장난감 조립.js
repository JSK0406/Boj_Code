const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const N = Number(input.shift())
const M = Number(input.shift())

const isPointedArr = Array(N+1).fill(false);
const pointedArr = Array(N+1).fill(0);
const pointingArr = Array.from({length: N+1}, () => []);
const ansArr = Array(N+1).fill(0)
const isMainArr = Array(N+1).fill(true);

for (let i = 0; i < M; i++) {
    const [thisNum, neededNum, cnt] = input.shift().split(' ').map(Number);
    pointedArr[neededNum] += 1;
    pointingArr[thisNum].push([neededNum, cnt]);
    isMainArr[thisNum] = false
}

const q = [];
while (true) {
    for (let i = 1; i < N+1; i++) {
        if (pointedArr[i] === 0 && !isPointedArr[i]) {
            q.push(i);
            isPointedArr[i] = true;
        }
    }
    if (q.length === 0) {
        break;
    }

    while (q.length > 0) {
        const nowNum = q.shift();
        for (lst of pointingArr[nowNum]) {
            const [num, cnt] = lst;
            pointedArr[num] -= 1;
            if (ansArr[nowNum] === 0) {
                ansArr[num] += cnt;
            } else {
                ansArr[num] += ansArr[nowNum] * cnt;
            }
        }
    }
}

for (let i = 1; i < N+1; i++) {
    if (isMainArr[i]) {
        console.log(`${i} ${ansArr[i]}`)
    }
}