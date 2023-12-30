const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const N = Number(input.shift());
const isRoot = Array(N+1).fill(true);
const trees = Array.from({ length: N+1 }, () => Array(2).fill(0));

for (let _ = 0; _ < N; _++) {
    const [root, left, right] = input.shift().split(' ').map(Number);
    if (left !== -1) {
        isRoot[left] = false
        trees[root][0] = left;
    }
    if (right !== -1) {
        isRoot[right] = false
        trees[root][1] = right;
    }
}

const levels = Array.from({ length: N+1 }, () => Array(2).fill(0));

let cnt = 1;

const inOrder = (now, level) => {
    if (trees[now][0] !== 0) {
        inOrder(trees[now][0], level+1)
    }
    if (levels[level][0] === 0) {
        levels[level][0] = cnt;
    } else {
        levels[level][0] = Math.min(levels[level][0], cnt);
    }
    levels[level][1] = Math.max(levels[level][1], cnt);
    cnt++;
    if (trees[now][1] !== 0) {
        inOrder(trees[now][1], level+1)
    }
}

let root = -1;
for (let i = 1; i < N+1; i++) {
    if (isRoot[i] === true) {
        root = i;
        break;
    }
}

inOrder(root, 1);

let [ansLevel, ansWidth] = [-1, -1];
for (let i = 1; i < N+1; i++) {
    if (ansWidth < levels[i][1] - levels[i][0]) {
        ansLevel = i;
        ansWidth = levels[i][1] - levels[i][0];
    }
}

console.log(ansLevel, ansWidth+1);