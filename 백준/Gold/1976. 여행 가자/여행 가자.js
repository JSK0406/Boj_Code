const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const N = Number(input.shift());
const M = Number(input.shift());

const edgeArr = Array.from({ length: N }, () => input.shift().split(' ').map(Number));
const parentArr = Array.from(Array(N).keys());

const cityArr = input.shift().split(' ').map((i) => Number(i) - 1);

const find = (x) => {
    if (x != parentArr[x]) {
        parentArr[x] = find(parentArr[x]);
    }
    return parentArr[x];
}

const union = (x, y) => {
    [x, y] = [find(x), find(y)];
    if (x < y) {
        parentArr[y] = x;
    } else {
        parentArr[x] = y;
    }
}

for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
        if (edgeArr[i][j] === 1) {
            union(i, j);
        }
    }
}

let ans = 'YES'
for (let i = 0; i < M-1; i++) {
    if (parentArr[cityArr[i]] === parentArr[cityArr[i+1]]) {
        continue;
    } else {
        ans = 'NO';
        break;
    }
}

console.log(ans);