const { info } = require("console");
const fs = require("fs");
const { brotliCompress } = require("zlib");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const N = Number(input.shift())

for (let i = 0; i < N; i++) {
    const T = Number(input.shift())
    const arr = [];
    for (let j = 0; j < T; j++) {
        const tmp = input.shift().split(' ')
        tmp[1] = Number(tmp[1])
        arr.push(tmp)
    }
    arr.sort((a, b) => b[1]-a[1])
    console.log(arr[0][0])
}