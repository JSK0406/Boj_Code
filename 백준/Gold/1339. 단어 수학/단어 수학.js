const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const N = Number(input.shift().trim())
let strList = []
let maxLength = 0;

for (let i = 0; i < N; i++) {
    strList.push([input[i].trim(), ''])
    maxLength = Math.max(maxLength, input[i].trim().length)
}

strList.sort(function(a, b) {
    return b[0].length-a[0].length
})

strObject = {}

for (let len = 0; len < maxLength; len++) {
    for (let i = 0; i < strList.length; i++) {
        str = strList[i][0]
        if (str.length >= maxLength - len) {
            let transLength = -maxLength + len + str.length;
            if (strObject[str[transLength]]) {
                strObject[str[transLength]] += 10**(maxLength-len)
            } else {
                strObject[str[transLength]] = 10**(maxLength-len)
            }
        }
    }
}

strNumObject = {}
strNumList = []
for (str in strObject) {
    strNumList.push([str, strObject[str]])
}

strNumList.sort(function(a, b) { return b[1] - a[1] })

let num = 9;
for (lst of strNumList) {
    strNumObject[lst[0]] = num;
    num -= 1
}

let ans = 0;

for (str of strList) {
    let tmpNum = ''
    for (alpha of str[0].split('')) {
        tmpNum += String(strNumObject[alpha])
    }
    ans += +tmpNum;
}
// console.log(strNumList)
console.log(ans)