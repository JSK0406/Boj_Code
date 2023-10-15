const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const INF = 999999999
const N = Number(input.shift())
let mapList = []
for (let lst of input) {
    mapList.push(lst.trim().split(' ').map(Number))
}
let dp = Array.from({length:N}, () => Array(1 << N).fill(-1))

const dfs = (now, visited) => {
    // 모든 비트가 1이면 : 모두 방문
    if (visited === (1 << N) - 1) {
        // 출발지로 돌아갈 수 있으면
        if (mapList[now][0] != 0) {
            return mapList[now][0]
        // 돌아가지 못하면
        } else {
            return INF
        }
    }

    if (dp[now][visited] !== -1) {
        return dp[now][visited]
    }

    dp[now][visited] = INF;

    for (let next = 1; next < N; next++) {
        // 다음으로 가는 길이 없다면
        if (mapList[now][next] === 0) {
            continue;
        }
        // 이미 방문했다면
        if ((visited & (1 << next)) > 0) {
            continue;
        }
        dp[now][visited] = Math.min(dp[now][visited], dfs(next, visited | (1 << next)) + mapList[now][next])
    }
    return dp[now][visited]
}

console.log(dfs(0, 1 << 0))
