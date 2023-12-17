const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const N = Number(input.shift())
const M = Number(input.shift())

const degreeArr = Array(N+1).fill(0);
const pointingArr = Array.from({length: N+1}, () => []);
const ansArr = Array(N+1).fill(0)
const isMainArr = Array(N+1).fill(true);

for (let i = 0; i < M; i++) {
    const [thisNum, neededNum, cnt] = input.shift().split(' ').map(Number);
    degreeArr[neededNum] += 1;
    pointingArr[thisNum].push([neededNum, cnt]);
    isMainArr[thisNum] = false
}

const q = [];

for (let i = 1; i < N+1; i++) {
    if (degreeArr[i] === 0) {
        q.push(i);
    }
}

while (q.length > 0) {
    const now = q.shift();
    for (const [next, cnt] of pointingArr[now]) {
        degreeArr[next] -= 1;
        if (ansArr[now] === 0) {
            ansArr[next] += cnt;
        } else {
            ansArr[next] += ansArr[now] * cnt;
        }
        if (degreeArr[next] === 0) {
            q.push(next);
        }
    }
}

for (let i = 1; i < N+1; i++) {
    if (isMainArr[i]) {
        console.log(`${i} ${ansArr[i]}`)
    }
}