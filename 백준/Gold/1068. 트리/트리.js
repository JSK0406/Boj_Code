const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const N = Number(input.shift());
const parentInfo = input.shift().split(' ').map(Number);
const deletedNode = Number(input.shift());

const childArr = Array.from({ length: N+1 }, () => Array(0));

let rootNode = 0;
for (let i = 0; i < N; i++) {
    if (parentInfo[i] === -1) {
        rootNode = i;
        continue;
    }
    childArr[parentInfo[i]].push(i);
}

let ans = 0;
const dfs = (now) => {
    if (now === deletedNode) {
        return;
    }
    let childCnt = 0;
    for (let child of childArr[now]) {
        if (child === deletedNode) {
            continue;
        }
        dfs(child)
        childCnt += 1;
    }

    if (childCnt === 0) {
        ans += 1
    }
}

dfs(rootNode)
console.log(ans);