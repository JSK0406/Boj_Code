const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const [N, L] = input.shift().trim().split(' ').map(Number);
let mapList = [];

for (let _ = 0; _ < N; _++) {
    mapList.push(input.shift().trim().split(' ').map(Number))
}

const checkRow = (row) => {
    let isPossible = true;
    let roadList = Array(N).fill(0);
    let height = mapList[row][0];
    for (let col = 1; col < N; col++) {
        if (height === mapList[row][col]) {

        } else {
            if (height + 1 === mapList[row][col]) {
                if (col - L >= 0) {
                    for (let i = col-L; i < col; i++) {
                        if (roadList[i] === 1 || mapList[row][i] !== height) {
                            isPossible = false;
                            break;
                        } else {
                            roadList[i] = 1;
                        }
                    }
                } else {
                    isPossible = false;
                    break;
                }
                height += 1;
            } else if (height === mapList[row][col] + 1) {
                if (col + L - 1 < N) {
                    for (let i = col; i < col + L; i++) {
                        if (mapList[row][i] === height - 1) {
                            roadList[i] = 1;
                        } else {
                            isPossible = false;
                            break;
                        }
                    }
                } else {
                    isPossible = false;
                    break;
                }
                col = col + L - 1
                height -= 1;
            } else {
                isPossible = false;
                break;
            }
        }

        if (!isPossible) {
            break;
        }
    }
    // console.log(roadList)
    // console.log(isPossible)
    return isPossible ? 1 : 0;
}

const checkCol = (col) => {
    let isPossible = true;
    let roadList = Array(N).fill(0);
    let height = mapList[0][col];
    for (let row = 1; row < N; row++) {
        if (height === mapList[row][col]) {

        } else {
            if (height === mapList[row][col] - 1) {
                if (row - L >= 0) {
                    for (let i = row - L; i < row; i++) {
                        if (roadList[i] === 1 || mapList[i][col] !== height) {
                            isPossible = false;
                            break;
                        } else {
                            roadList[i] = 1;
                        }
                    }
                } else {
                    isPossible = false;
                    break;
                }
                height += 1;
            } else if (height === mapList[row][col] + 1) {
                if (row + L - 1 < N) {
                    for (let i = row; i < row + L; i++) {
                        if (mapList[i][col] === height - 1) {
                            roadList[i] = 1;
                        } else {
                            isPossible = false;
                            break;
                        }
                    }
                } else {
                    isPossible = false;
                    break;
                }
                row = row + L - 1
                height -= 1;
            } else {
                isPossible = false;
                break;
            }
        }

        if (!isPossible) {
            break;
        }
    }
    // console.log(roadList)
    // console.log(isPossible)
    return isPossible ? 1 : 0;
}


let ans = 0;
for (let j = 0; j < N; j++) {
    ans += checkRow(j)
    ans += checkCol(j)
    // console.log(j, checkCol(j))
}

// checkRow(0);
// checkCol(2)
console.log(ans);