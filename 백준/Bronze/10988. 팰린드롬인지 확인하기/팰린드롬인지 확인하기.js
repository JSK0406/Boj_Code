const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const str = input.shift().trim();

let answer = 1;
for (let i = 0; i < parseInt(str.length / 2); i++) {
    if (str[i] !== str[str.length - 1 - i]) {
        answer = 0;
        break;
    }
}

console.log(answer);