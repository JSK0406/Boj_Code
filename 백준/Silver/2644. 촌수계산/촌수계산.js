const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

let n = Number(input.shift());
let [person1, person2] = input.shift().split(' ').map(Number);
let m = Number(input.shift());
let arr = input.map((i) => i.split(' ').map(Number))

let edgeList = [...Array(n + 1)].map(() => []);
let visitedList = Array(n + 1).fill(0);

arr.map(([A, B]) => {
    edgeList[A].push(B);
    edgeList[B].push(A);
})

ans = 0;

const dfs = (now, cnt) => {
    if (now === person2) {
        ans = cnt;
    }
    for (let next of edgeList[now]) {
        if (!visitedList[next]) {
            visitedList[next] = 1
            dfs(next, cnt + 1)
        }
    }
    return
}

dfs(person1, 0)
ans ? console.log(ans) : console.log(-1);