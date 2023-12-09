const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split('\n');
// let input = fs.readFileSync(filePath).toString().trim().split('\n');

input.forEach((str) => {
    console.log(str)
})