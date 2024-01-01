const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const K = Number(input.shift());
const originEdges = input.shift().split(' ').map(Number);
const edges = [...originEdges];

let ans = 0;

while (edges.length > 0) {
    const upperInx = Number.parseInt((edges.length-1)/2)-1;
    const [leftNum, rightNum] = [edges.pop(), edges.pop()]
    ans += Math.abs(leftNum-rightNum) + originEdges.pop() + originEdges.pop();
    edges[upperInx] += Math.max(leftNum, rightNum);
}

console.log(ans);