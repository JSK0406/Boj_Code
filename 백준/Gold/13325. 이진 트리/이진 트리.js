const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const K = Number(input.shift());
const originEdges = input.shift().split(' ').map(Number);
const edges = [...originEdges];

let ans = 0;

for (let i = edges.length-1; i >= 0; i--) {
    const upperInx = Number.parseInt((i-1)/2)-1;
    const [leftNum, rightNum] = [edges[i-1], edges[i]]
    ans += Math.abs(leftNum-rightNum) + originEdges[i-1] + originEdges[i];
    edges[upperInx] += Math.max(leftNum, rightNum);
    i--;
}

console.log(ans);