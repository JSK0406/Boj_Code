const { info } = require("console");
const fs = require("fs");
const { brotliCompress } = require("zlib");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const N = Number(input.shift());
const map = new Map();

input.forEach((ele) => {
    const extension = ele.split('.')[1];
    if (map.has(extension)) {
        map.set(extension, map.get(extension)+1)
    } else {
        map.set(extension, 1)
    }
})

const resultArr = [...map]

resultArr.sort((a, b) => a[0].localeCompare(b[0]))

resultArr.forEach((ele) => {
    console.log(ele[0], ele[1])
})