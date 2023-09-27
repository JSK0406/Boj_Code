const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

let A = input.shift().trim()
let BList = input.shift().trim().split('')


while (true) {
    if (BList.slice(-1)[0] === 'A') {
        BList.pop()
    } else {
        BList.pop()
        BList.reverse()
    }
    if (A.length === BList.length) {
        break
    }
}

if (A === BList.join('')) {
    console.log(1)
} else {
    console.log(0)
}