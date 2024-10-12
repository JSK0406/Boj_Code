const { info } = require("console");
const fs = require("fs");
const { brotliCompress } = require("zlib");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

// 8가지 방향 혹은 정지
// 미친 아두이노와 겹치면 짐
// 미친 아두이노는 가장 가까운 방향으로 이동
// (r1,s1), 미친 아두이노의 위치를 (r2, s2)라고 했을 때, |r1-r2| + |s1-s2|가 가장 작아지는 방향
// 미친 아두이노가 겹치면 해당 칸 아두이노 없어짐

const [R, C] = input.shift().split(' ').map(Number);
const orderArr = input.pop().split('').map(Number);
const mapList = [];
const nd = [0, [1, -1], [1, 0], [1, 1], [0, -1], [0, 0], [0, 1], [-1, -1], [-1, 0], [-1, 1]];

let [nowRow, nowCol] = [-1, -1];
let robotArr = []
for (let r = 0; r < R; r++) {
    mapList.push(input[r])
    for (let c = 0; c < C; c++) {
        if (input[r][c] === 'I') {
            nowRow = r;
            nowCol = c;
        }
        if (input[r][c] === 'R') {
            robotArr.push([r, c])
        }
    }
}

const check = (arr, r, c) => {
    arr.forEach((a) => {
        if (a.join(' ') === `${r} ${c}`) {
            return true;
        }
    })
    return false;
}

const checkBoard = (r, c) => {
    return 0 <= r && r < R && 0 <= c && c < C;
}

let cnt = 0;
let isFinish = false;
for (let i = 0; i < orderArr.length; i++) {
    const di = orderArr[i];
    [nowRow, nowCol] = [nowRow + nd[di][0], nowCol + nd[di][1]]
    cnt += 1
    if (check(robotArr, nowRow, nowCol)) {
        isFinish = true;
        console.log(robotArr, nowRow, nowCol)
        break;
    }

    const newRobots = []
    for (let j = 0; j < robotArr.length; j++) {
        const [robotRow, robotCol] = [robotArr[j][0], robotArr[j][1]];
        let dirIdx = -1;
        let minValue = 999999999;
        for (let k = 1; k <= 9; k++) {
            const [nextRow, nextCol] = [robotRow+nd[k][0], robotCol+nd[k][1]];
            if (checkBoard(nextRow, nextCol) && Math.abs(nowRow - nextRow) + Math.abs(nowCol - nextCol) < minValue) {
                minValue = Math.abs(nowRow - nextRow) + Math.abs(nowCol - nextCol);
                dirIdx = k;
            }
        }
        if ([nowRow, nowCol].join(' ') === [robotRow+nd[dirIdx][0], robotCol+nd[dirIdx][1]].join(' ')) {
            isFinish = true;
            break;
        }
        newRobots.push([robotRow+nd[dirIdx][0], robotCol+nd[dirIdx][1]])
    }
    if (isFinish) {
        break;
    }
    const cntMap = new Map();
    for (let l = 0; l < newRobots.length; l++) {
        if (cntMap.has(newRobots[l].join(' '))) {
            cntMap.set(newRobots[l].join(' '), cntMap.get(newRobots[l]) + 1);
        } else {
            cntMap.set(newRobots[l].join(' '), 1);
        }
    }
    robotArr = [];
    for (let [key, value] of cntMap) {
        if (value === 1) {
            robotArr.push(key.split(' ').map(Number));
        }
    }
}

if (isFinish || check(robotArr, nowRow, nowCol)) {
    console.log(`kraj ${cnt}`)
} else {
    const resultMap = Array.from({ length: R }, () => Array(C).fill('.'));
    resultMap[nowRow][nowCol] = 'I';
    for (let [r, c] of robotArr) {
        resultMap[r][c] = 'R'
    }
    resultMap.forEach((row) => {
        console.log(row.join(''))
    })
}