const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const [row, col] = input.shift().split(' ').map(Number);
const initMapList = Array.from({ length: row }, () => input.shift().split(' ').map(Number));

const findZeroCnt = (mapList) => {
    let cnt = 0;
    for (let i = 0; i < row; i++) {
        for (let j = 0; j < col; j++) {
            if (mapList[i][j] === 0) {
                cnt += 1
            }
        }
    }
    return cnt;
}

const filling = (mapList, r, c, dir) => {
    const [dr, dc] = {
        'up': [-1, 0],
        'down': [1, 0],
        'left': [0, -1],
        'right': [0, 1],
    }[dir]
    const nowMapList = mapList.map((lst) => [...lst]);
    let [nowRow, nowCol] = [r + dr, c + dc];
    while (0 <= nowRow && nowRow < row && 0 <= nowCol && nowCol < col && nowMapList[nowRow][nowCol] !== 6) {
        if (nowMapList[nowRow][nowCol] === 0) {
            nowMapList[nowRow][nowCol] = '#';
        }
        nowRow += dr;
        nowCol += dc;
    }
    return nowMapList
}

let totMapList = [initMapList];
for (let r = 0; r < row; r++) {
    for (let c = 0; c < col; c++) {
        let tmpList = [];
        if (initMapList[r][c] === 1) {
            totMapList.forEach((mapList) => {
                tmpList.push(filling(mapList, r, c, 'up'))
                tmpList.push(filling(mapList, r, c, 'down'))
                tmpList.push(filling(mapList, r, c, 'left'))
                tmpList.push(filling(mapList, r, c, 'right'))
            })
            totMapList = tmpList;
        } else if (initMapList[r][c] === 2) {
            totMapList.forEach((mapList) => {
                tmpList.push(filling(filling(mapList, r, c, 'left'), r, c, 'right'));
                tmpList.push(filling(filling(mapList, r, c, 'up'), r, c, 'down'));
            })
            totMapList = tmpList;
        } else if (initMapList[r][c] === 3) {
            totMapList.forEach((mapList) => {
                tmpList.push(filling(filling(mapList, r, c, 'up'), r, c, 'left'));
                tmpList.push(filling(filling(mapList, r, c, 'up'), r, c, 'right'));
                tmpList.push(filling(filling(mapList, r, c, 'down'), r, c, 'left'));
                tmpList.push(filling(filling(mapList, r, c, 'down'), r, c, 'right'));
            })
            totMapList = tmpList;
        } else if (initMapList[r][c] === 4) {
            totMapList.forEach((mapList) => {
                tmpList.push(filling(filling(filling(mapList, r, c, 'left'), r, c, 'up'), r, c, 'right'));
                tmpList.push(filling(filling(filling(mapList, r, c, 'down'), r, c, 'left'), r, c, 'up'));
                tmpList.push(filling(filling(filling(mapList, r, c, 'right'), r, c, 'down'), r, c, 'left'));
                tmpList.push(filling(filling(filling(mapList, r, c, 'up'), r, c, 'right'), r, c, 'down'));
            })
            totMapList = tmpList;
        } else if (initMapList[r][c] === 5) {
            totMapList.forEach((mapList) => {
                tmpList.push(filling(filling(filling(filling(mapList, r, c, 'up'), r, c, 'down'), r, c, 'left'), r, c, 'right'));
            })
            totMapList = tmpList;
        }
    }
}

let ans = Infinity;
totMapList.forEach((mapList) => {
    ans = Math.min(ans, findZeroCnt(mapList))
})

console.log(ans);