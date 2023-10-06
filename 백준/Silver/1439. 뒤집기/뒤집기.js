const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

let lst = input.shift().trim().split('').map(Number);

let zerosCnt = 0;
let onesCnt = 0;

let formerNum = lst[0];

if (formerNum === 0) {
    zerosCnt += 1;
} else {
    onesCnt += 1;
}

for (num of lst) {
    if (num === formerNum) {

    } else {
        if (num === 0) {
            zerosCnt += 1;
        } else {
            onesCnt += 1;
        }
    }
    formerNum = num;
}

if (zerosCnt + onesCnt === 1) {
    console.log(0)
} else {
    console.log(Math.min(zerosCnt, onesCnt))
}