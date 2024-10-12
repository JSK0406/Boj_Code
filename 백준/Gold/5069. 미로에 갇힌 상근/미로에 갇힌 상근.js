const { info } = require("console");
const fs = require("fs");
const { brotliCompress } = require("zlib");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const T = Number(input.shift());
const mapArr = Array.from({ length: 15 }, () => Array.from({ length: 101 }, () => Array(101).fill(0)))
mapArr[0][50][50] = 1;

const nd = [[-1, 0], [1, 0], [0, 1], [0, -1], [-1, -1], [1, 1]];

const check = (r, c) => {
    return 0 <= r && r <= 100 && 0 <= c && c <= 100;
}

for (let n = 1; n <= 14; n++) {
    for (let r = 0; r <= 100; r++) {
        for (let c = 0; c <= 100; c++) {
            for (let i = 0; i < 6; i++) {
                const [nr, nc] = [r+nd[i][0], c+nd[i][1]]
                if (check(nr, nc)) {
                    mapArr[n][r][c] += mapArr[n-1][nr][nc]
                }
            }
        }
    }
}

for (let i = 0; i < T; i++) {
    const n = Number(input[i])
    console.log(mapArr[n][50][50])
}