const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const T = Number(input.shift());

const dfs = (preLeft, preRight, inLeft, inRight, preOrder, inOrder, inIdx) => {
    if (preLeft > preRight || inLeft > inRight) {
        return;
    }
    const nowRoot = preOrder[preLeft];
    const rootIdx = inIdx[nowRoot];

    const leftNode = rootIdx - inLeft - 1;  // 3
    const rightNode = inRight - rootIdx;  // 3

    dfs(preLeft+1, preLeft+leftNode+1, inLeft, inLeft+leftNode, preOrder, inOrder, inIdx);
    dfs(preRight-rightNode+1, preRight, inRight-rightNode+1, inRight, preOrder, inOrder, inIdx);

    process.stdout.write(`${nowRoot} `)
}

for (let _ = 0; _ < T; _++) {
    const N = Number(input.shift());
    const preOrder = input.shift().split(' ').map(Number);
    const inOrder = input.shift().split(' ').map(Number);
    
    const inIdx = Array(N+1).fill(0);
    
    for (let i = 0; i < N; i++) {
        inIdx[inOrder[i]] = i;
    }
    
    dfs(0, N-1, 0, N-1, preOrder, inOrder, inIdx);
    console.log('')
}
