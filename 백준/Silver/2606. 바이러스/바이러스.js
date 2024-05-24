const fs = require("fs");
const { brotliCompress } = require("zlib");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const N = Number(input.shift()) // 컴퓨터 수
const M = Number(input.shift()) // 연결 수

const mapList = Array.from({length: N+1}, () => [])
const visited = Array(N+1).fill(0)

input.forEach((i) => {
    const tmp = i.split(' ').map(Number);
    mapList[tmp[0]].push(tmp[1])
    mapList[tmp[1]].push(tmp[0])
})

let ans = 0;
visited[1] = 1
const dfs = (now) => {
    mapList[now].forEach((next) => {
        if (visited[next] === 0) {
            ans += 1;
            visited[next] = 1
            dfs(next)
        }
    })
}
dfs(1)
console.log(ans)