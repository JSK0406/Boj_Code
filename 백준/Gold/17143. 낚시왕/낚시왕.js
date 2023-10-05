const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

// row, col, 상어 수
const [R, C, M] = input.shift().trim().split(' ').map(Number);

const catchShark = (kingCol, mapList) => {
    for (let kingRow = 0; kingRow < R; kingRow++) {
        if (mapList[kingRow][kingCol] !== 0) {
            return [mapList[kingRow][kingCol][0], mapList[kingRow][kingCol][1]]  // 크기, id
        } 
    }
    return [0, -1];
}

const makeMapList = (sharkList) => {
    let newMapList = Array.from({length:R}, () => Array(C).fill(0));
    let newSharkList = []
    for (let i = 0; i < sharkList.length; i++) {
        let [sharkRow, sharkCol, speed, dir, size, id] = sharkList[i];
        // sharkRow -= 1;
        // sharkCol -= 1;
        for (let i = 0; i < speed; i++) {
            if (dir === 1) {
                if (sharkRow === 0) {
                    dir = 2;
                    sharkRow += 1;
                } else {
                    sharkRow -= 1;
                }
            } else if (dir === 2) {
                if (sharkRow === R-1) {
                    dir = 1;
                    sharkRow -= 1;
                } else {
                    sharkRow += 1;
                }
            } else if (dir === 3) {
                if (sharkCol === C-1) {
                    dir = 4;
                    sharkCol -= 1;
                } else {
                    sharkCol += 1;
                }
            } else if (dir === 4) {
                if (sharkCol === 0) {
                    dir = 3;
                    sharkCol += 1;
                } else {
                    sharkCol -= 1;
                }
            }
        }
        // console.log(sharkRow, sharkCol)
        if (newMapList[sharkRow][sharkCol] === 0) {
            newMapList[sharkRow][sharkCol] = [size, id]
            newSharkList.push([sharkRow, sharkCol, speed, dir, size, id])
        } else {
            if (newMapList[sharkRow][sharkCol][0] > size) {
                
            } else {
                disappearedSharkId = newMapList[sharkRow][sharkCol][1]
                newSharkList = newSharkList.filter((lst) => lst[5] !== disappearedSharkId)
                newMapList[sharkRow][sharkCol] = [size, id]
                newSharkList.push([sharkRow, sharkCol, speed, dir, size, id])
            }
        }
    }
    return [newMapList, newSharkList]
}

sharkList = []

for (let i = 0; i < input.length; i++) {
    // row, col, 속력(1:위 2:아래 3:오른쪽 4:왼쪽), 이동방향, 크기, id
    nowAddList = input[i].split(' ').map(Number)
    nowAddList[0] -= 1;
    nowAddList[1] -= 1;
    nowAddList.push(i)
    sharkList.push(nowAddList);
}

let newMapList = Array.from({ length: R }, () => Array(C).fill(0));
let newSharkList = []
let kingCol = 0;
for (let i = 0; i < sharkList.length; i++) {
    let [sharkRow, sharkCol, speed, dir, size, id] = sharkList[i];
    if (newMapList[sharkRow][sharkCol] === 0) {
        newMapList[sharkRow][sharkCol] = [size, id]
        newSharkList.push([sharkRow, sharkCol, speed, dir, size, id])
    } else {
        if (newMapList[sharkRow][sharkCol][0] > size) {
    
        } else {
            disappearedSharkId = newMapList[sharkRow][sharkCol][1]
            newSharkList = newSharkList.filter((lst) => lst[5] !== disappearedSharkId)
            newMapList[sharkRow][sharkCol] = [size, id]
            newSharkList.push([sharkRow, sharkCol, speed, dir, size, id])
        }
    }
}
let ans = 0;

let [catchedSize, catchedId] = catchShark(kingCol, newMapList)
ans += catchedSize;
// console.log(catchedId)
// console.log(newSharkList)
sharkList = newSharkList.filter((lst) => lst[5] !== catchedId);
// console.log(newMapList, catchedSize)
// console.log(newMapList)
for (kingCol = 1; kingCol < C; kingCol++) {
    [mapList, sharkList] = makeMapList(sharkList);
    [catchedSize, catchedId] = catchShark(kingCol, mapList)
    // console.log(mapList, catchedSize)
    ans += catchedSize;
    sharkList = sharkList.filter((lst) => lst[5] !== catchedId);
    // console.log(mapList)
}
console.log(ans);