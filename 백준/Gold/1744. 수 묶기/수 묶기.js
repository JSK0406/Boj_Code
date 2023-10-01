const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const N = Number(input.shift().trim());
let numList = input.map((num) => Number(num));
let minusList = []
let zeroList = []
let plusList = []

for (num of numList) {
    if (num < 0) {
        minusList.push(num)
    } else if (num === 0) {
        zeroList.push(num)
    } else {
        plusList.push(num)
    }
}

// plusList.sort().reverse()
// minusList.sort().reverse()

plusList.sort(function (a, b) {
    return b-a;
})
minusList.sort(function (a, b) {
    return a-b;
})

let ans = 0;
let minusIdx = 0;
while (minusIdx < minusList.length) {
    if (minusIdx + 1 < minusList.length) {
        ans += minusList[minusIdx] * minusList[minusIdx + 1]
        minusIdx += 2;
    } else {
        if (zeroList.length > 0) {
            minusIdx += 1;
        } else {
            ans += minusList[minusIdx];
            minusIdx += 1;
        }
    }
}

let plusIdx = 0;
while (plusIdx < plusList.length) {
    if (plusIdx + 1 < plusList.length) {
        if (plusList[plusIdx + 1] === 1) {
            ans += plusList[plusIdx] + plusList[plusIdx + 1]
        } else {
            ans += plusList[plusIdx] * plusList[plusIdx + 1]
        }
        plusIdx += 2;
    } else {
        ans += plusList[plusIdx];
        plusIdx += 1;
    }
}

console.log(ans)