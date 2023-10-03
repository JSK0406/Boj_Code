const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const N = +input.shift().trim();  // 보드 크기

let appleList = []
let appleCnt = +input.shift().trim()
for (let i = 0; i < appleCnt; i++) {
    const [row, col] = input.shift().trim().split(' ').map(Number);
    appleList.push([row - 1, col - 1]);
}

let dirChangeList = []
let dirCnt = +input.shift().trim();
for (let i = 0; i < dirCnt; i++) {
    const [x, D] = input.shift().trim().split(' ');
    dirChangeList.push([Number(x) + 1, D]);
}

let q = []  // 머리가 앞(작은 인덱스), 꼬리가 뒤(큰 인덱스)
q.push([0, 0]);

let nowDir = 'right';
let T = 0;

while (true) {
    T += 1;
    if (dirChangeList.length > 0 && T === dirChangeList[0][0]) {
        if (dirChangeList[0][1] === 'D') {
            if (nowDir === 'right') {
                nowDir = 'down';
            } else if (nowDir === 'left') {
                nowDir = 'up';
            } else if (nowDir === 'up') {
                nowDir = 'right';
            } else {
                nowDir = 'left';
            }
        } else {
            if (nowDir === 'right') {
                nowDir = 'up';
            } else if (nowDir === 'left') {
                nowDir = 'down';
            } else if (nowDir === 'up') {
                nowDir = 'left';
            } else {
                nowDir = 'right';
            }
        }
        dirChangeList.shift();
    }

    let [nextRow, nextCol] = [q[0][0], q[0][1]];
    
    let isFinish = false;

    if (nowDir === 'up') {
        nextRow -= 1;
        if ((0 <= nextRow && nextRow < N) && (0 <= nextCol && nextCol < N)) {
            q.unshift([nextRow, nextCol]);
        } else {
            isFinish = true;
            break;
        }
    } else if (nowDir === 'down') {
        nextRow += 1;
        if ((0 <= nextRow && nextRow < N) && (0 <= nextCol && nextCol < N)) {
            q.unshift([nextRow, nextCol]);
        } else {
            isFinish = true;
            break;
        }
    } else if (nowDir === 'left') {
        nextCol -= 1;
        if ((0 <= nextRow && nextRow < N) && (0 <= nextCol && nextCol < N)) {            q.unshift([nextRow, nextCol]);
        } else {
            isFinish = true;
            break;
        }
    } else {
        nextCol += 1;
        if ((0 <= nextRow && nextRow < N) && (0 <= nextCol && nextCol < N)) {            q.unshift([nextRow, nextCol]);
        } else {
            isFinish = true;
            break;
        }
    }

    for (lst of q.slice(1, q.length)) {
        if (lst[0] === nextRow && lst[1] === nextCol) {
            isFinish = true;
            break;
        }
    }

    if (isFinish === true) {
        break;
    }

    let isApple = false;
    for (let i = 0; i < appleList.length; i++) {
        if (nextRow === appleList[i][0] && nextCol === appleList[i][1]) {
            isApple = true;
            appleList.splice(i, 1);
        }
    }
    if (!isApple) {
        q.pop();
    }
}

console.log(T);