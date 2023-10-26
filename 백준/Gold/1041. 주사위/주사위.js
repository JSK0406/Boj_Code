const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const pairNumObject = {
    0 : 5,
    1 : 4,
    2 : 3,
    3 : 2,
    4 : 1,
    5 : 0,
}

const N = Number(input.shift().trim());
const originalNumList = input.shift().split(' ').map(Number)

const getMinSumThreeNumber = (originalNumList) => {
    let minSum = 999999999;
    for (let baseIdx = 0; baseIdx < 6; baseIdx++) {
        let possibleNumList = [0, 1, 2, 3, 4, 5];
        let baseNum = originalNumList[baseIdx];
        const filteredPossibleNumList = possibleNumList.filter(num => num !== baseIdx && num !== pairNumObject[baseIdx])
        for (let left = 0; left < 3; left++) {
            for (let right = left + 1; right < 4; right++) {
                const [leftNum, rightNum] = [filteredPossibleNumList[left], filteredPossibleNumList[right]]
                if (pairNumObject[leftNum] === rightNum) {
                    continue
                }
                minSum = Math.min(minSum, baseNum + originalNumList[leftNum] + originalNumList[rightNum])
            }
        }
    }
    return minSum;
}

const getMinSumTwoNumber = (originalNumList) => {
    let minSum = 999999999;
    for (let baseIdx = 0; baseIdx < 6; baseIdx++) {
        let possibleNumList = [0, 1, 2, 3, 4, 5];
        let baseNum = originalNumList[baseIdx];
        const filteredPossibleNumList = possibleNumList.filter(num => num !== baseIdx && num !== pairNumObject[baseIdx])
        for (let otherIdx = 0; otherIdx < 4; otherIdx++) {
            minSum = Math.min(minSum, baseNum + originalNumList[filteredPossibleNumList[otherIdx]])
        }
    }
    return minSum;
}

const threeNumSum = getMinSumThreeNumber(originalNumList)
const twoNumSum = getMinSumTwoNumber(originalNumList)
const oneNumSum = originalNumList.sort((a, b) => a-b)[0]

const threeCnt = 4;
const twoCnt = 4 * (N - 2) + (N - 1) * 4;
const oneCnt = (N ** 2) * 5 - 3 * threeCnt - 2 * twoCnt

if (N===1) {
    let oneSum = 0;
    originalNumList.map((num) => oneSum += num);
    console.log(oneSum - originalNumList[5])
} else {
    console.log(threeNumSum * threeCnt + twoNumSum * twoCnt + oneNumSum * oneCnt)
}