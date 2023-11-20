const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const [N, M] = input.shift().split(' ').map(Number);
const timeList = input.shift().split(' ').map(Number);

let formerCnt = M;
let letterCnt = M;
const ansList = [];
if (N <= M) {
    console.log(N)
} else {
    let totTime;
    let left = 0;
    let right = 60000000000;
    while (left <= right) {
        const mid = parseInt((left + right) / 2);
        let totChild = M;
        timeList.forEach((time) => {
            totChild += parseInt(mid / time);
        })
        if (totChild < N) {
            left = mid + 1;
        } else {
            totTime = mid;
            right = mid -1;
        }
    }

    timeList.forEach((time, idx) => {
        letterCnt += parseInt(totTime/time);
        formerCnt += parseInt((totTime-1)/time);
        if ((parseInt(totTime/time) - parseInt((totTime-1)/time)) === 1) {
            ansList.push(idx+1)
        }
    })
    console.log(ansList[N - formerCnt - 1])
}
