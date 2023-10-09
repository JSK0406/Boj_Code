const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

// [16인덱스에 번호에 맞는 dir]
// 현재 맵에 배치된 상태

let mapList = Array.from({length:4}, () => Array(4).fill(0));
let dirList = Array(17).fill(0)

for (let r = 0; r < 4; r++) {
    const [a, b, c, d, e, f, g, h] = input.shift().split(' ').map(Number);
    mapList[r][0] = a
    mapList[r][1] = c
    mapList[r][2] = e
    mapList[r][3] = g
    dirList[a] = b
    dirList[c] = d
    dirList[e] = f
    dirList[g] = h
}

let sum = mapList[0][0]  // 첫번째 고기 먹힘
sharkDir = dirList[mapList[0][0]]  // 상어는 먹은 고기 방향
dirList[mapList[0][0]] = 0  // 첫번째 고기 방향 없음 => 존재x
mapList[0][0] = -1  // 상어 있으면 -1

const moveFish = (mapList, dirList) => {
    for (let idx = 1; idx < 17; idx++) {
        if (dirList[idx] > 0) {
            let dr; let dc;
            let row; let col;
            for (let r = 0; r < 4; r++) {
                for (let c = 0; c < 4; c++) {
                    if (mapList[r][c] === idx) {
                        row = r; col = c; break;
                    }
                }
            }
            if (row === undefined) {
                continue;
            }
            let fishDir = dirList[idx];
            let i = 0;
            while (true) {
                switch (fishDir) {
                    case 1:
                        dr = -1, dc = 0; break;
                    case 2:
                        dr = -1, dc = -1; break;
                    case 3:
                        dr = 0, dc = -1; break;
                    case 4:
                        dr = 1, dc = -1; break;
                    case 5:
                        dr = 1, dc = 0; break;
                    case 6:
                        dr = 1, dc = 1; break;
                    case 7:
                        dr = 0, dc = 1; break;
                    case 8:
                        dr = -1, dc = 1; break;
                }
                let [nextRow, nextCol] = [row + dr, col + dc];
                if (0 <= nextRow && nextRow < 4 && 0 <= nextCol && nextCol < 4 && mapList[nextRow][nextCol] !== -1) {
                    let tmpIdx = mapList[nextRow][nextCol];  // 다음 칸 물고기 저장
                    mapList[row][col] = tmpIdx;  // 지금 칸으로 다음 칸 물고기 이동
                    mapList[nextRow][nextCol] = idx;  // 다음칸으로 지금 칸 물고기 이동 / 자리 교환 끝
                    dirList[idx] = fishDir;  // 바뀐 방향 저장
                    break;
                } else {
                    fishDir = fishDir === 8 ? 1 : fishDir + 1;
                    i += 1;
                    if (i === 8) {
                        break;
                    }
                }
            }
        }
    }

    return mapList
}


let stack = []
stack.push([mapList, dirList, sharkDir, sum])

let ans = 0;
while (stack.length > 0) {
    let [nowMapList, nowDirList, sharkDir, nowSum] = stack.pop()
    ans = Math.max(ans, nowSum);
    nowMapList = moveFish(nowMapList, nowDirList);
    let dr; let dc;

    switch (sharkDir) {
        case 1:
            dr = -1, dc = 0; break;
        case 2:
            dr = -1, dc = -1; break;
        case 3:
            dr = 0, dc = -1; break;
        case 4:
            dr = 1, dc = -1; break;
        case 5:
            dr = 1, dc = 0; break;
        case 6:
            dr = 1, dc = 1; break;
        case 7:
            dr = 0, dc = 1; break;
        case 8:
            dr = -1, dc = 1; break;
    }

    let sharkRow; let sharkCol;

    for (let r = 0; r < 4; r++) {
        for (let c = 0 ; c < 4; c++) {
            if (nowMapList[r][c] === -1) {
                sharkRow = r; sharkCol = c;
                break;
            }
        }
    }

    let [nextRow, nextCol] = [sharkRow, sharkCol]
    while (true) {
        nextRow += dr; nextCol += dc;
        if (0 <= nextRow && nextRow < 4 && 0 <= nextCol && nextCol < 4) {
            if (nowMapList[nextRow][nextCol] > 0) {
                let copiedMapList = nowMapList.map(lst => [...lst]);
                let copiedDirList = [...nowDirList];
                let nextSum = nowSum + copiedMapList[nextRow][nextCol];
                let nextSharkDir = copiedDirList[copiedMapList[nextRow][nextCol]];
                copiedDirList[copiedMapList[nextRow][nextCol]] = 0; // 먹힌 물고기 방향 0
                copiedMapList[sharkRow][sharkCol] = 0;  // 원래 상어 칸 빈칸
                copiedMapList[nextRow][nextCol] = -1;  // 맵에서 다음 칸에 상어
                stack.push([copiedMapList, copiedDirList, nextSharkDir, nextSum])
            } else {
                continue;
            }
        } else {
            break;
        }
    }

}

console.log(ans);