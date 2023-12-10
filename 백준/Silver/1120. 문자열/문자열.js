const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
// let input = fs.readFileSync(filePath).toString().split('\n');
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const [str1, str2] = input.shift().trim().split(' ');

let longer;
let shorter;

if (str1.length > str2.length) {
    longer = str1;
    shorter = str2;
} else {
    longer = str2;
    shorter = str1;
}

let ans = 0;
if (str1.length === str2.length) {
    for (let i = 0; i < str1.length; i++) {
        if (str1[i] !== str2[i]) {
            ans += 1;
        }
    }
} else {
    let diff = 999_999_999;
    for (let i = 0; i < longer.length - shorter.length + 1; i++) {
        let tmpDiff = 0;
        for (let j = i; j < i + shorter.length; j++) {
            if (shorter[j-i] !== longer[j]) {
                tmpDiff += 1;
            }
        }
        diff = Math.min(diff, tmpDiff)
    }
    ans += diff;
}

console.log(ans);