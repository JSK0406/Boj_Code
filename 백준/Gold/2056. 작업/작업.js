const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const N = Number(input.shift())

const timeArr = Array(N+1).fill(0);
const formerArr = Array.from({ length: N+1 }, () => []);
const visitedArr = Array(N+1).fill(false);

for (let i = 1; i < N+1; i++) {
    const info = input.shift().split(' ').map(Number);
    timeArr[i] = info[0];
    for (let j = 0; j < info[1]; j++) {
        formerArr[i].push(info[j+2]);
    }
}

let ans = [];

const dfs = (now) => {
    visitedArr[now] = true;
    formerArr[now].forEach((before) => {
        if (!visitedArr[before]) {
            dfs(before);
        }
    })
    ans.push(now);
}

for (let i = 1; i < N+1; i++) {
    if (!visitedArr[i]) {
        dfs(i)
    }
}

let time = Array(N+1).fill(0);

let maxTime = 0;
ans.forEach((node) => {
    if (formerArr[node].length === 0) {
        time[node] = timeArr[node];
    }
    formerArr[node].forEach((former) => {
        time[node] = Math.max(time[node], time[former] + timeArr[node]);
    })
    maxTime = Math.max(maxTime, time[node]);
})

console.log(maxTime);