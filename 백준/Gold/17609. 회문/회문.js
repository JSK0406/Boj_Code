const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const N = Number(input.shift());

const checkPal = (left, right, isPassed, strList) => {
    let isPal = true;
    while (left < right) {
        if (strList[left] === strList[right]) {
            left += 1;
            right -= 1;
        } else {
            if (!isPassed) {
                return Math.min(checkPal(left + 1, right, true, strList), checkPal(left, right - 1, true, strList));
            } else {
                isPal = false;
                break;
            }
        }
    }
    if (isPal && !isPassed) {
        return 0
    } else if (isPal && isPassed) {
        return 1
    } else {
        return 2
    }
}

for (_ = 0; _ < N; _++) {
    let strList = input.shift().trim().split('');
    let [left, right] = [0, strList.length-1];
    console.log(checkPal(left, right, false, strList));
}