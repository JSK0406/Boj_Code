class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
        this.prev = null;
    }
}

class Deque {
    constructor() {
        this.init();
    }

    init() {
        this.cnt = 0;
        this.head = null;
        this.tial = null;
    }

    popleft() {
        if (this.cnt === 0) return null;

        const value = this.head.value;

        if (this.cnt === 1) {
            this.init();
        } else {
            this.head = this.head.next;
            this.head.prev = null;
            this.cnt -= 1;
        }

        return value;
    }

    append(value) {
        const node = new Node(value);

        if (this.cnt === 0) {
            this.head = node;
            this.tail = node;
        } else {
            const tmp = this.tail;
            tmp.next = node;

            node.prev = tmp;

            this.tail = node;
        }

        this.cnt += 1;
    }
}

// . : 빈 필드
// # : 울타리
// v : 늑대
// o : 양

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const [row, col] = input.shift().split(' ').map(Number);
const mapList = [];
const visited = Array.from({length: row}, () => Array(col).fill(0));

for (let i = 0; i < row; i++) {
    mapList.push(input[i].split(''))
}

const nrr = [0, 0, 1, -1];
const ncc = [1, -1, 0, 0];

let ansSheep = 0;
let ansWolf = 0;
for (let r = 0; r < row; r++) {
    for (let c = 0; c < col; c++) {
        if (mapList[r][c] !== '#' && visited[r][c] === 0) {
            const q = new Deque();
            q.append([r, c])
            visited[r][c] = 1
            let sheepCnt = 0;
            let wolfCnt = 0;
            if (mapList[r][c] === 'v') {
                wolfCnt += 1;
            }
            if (mapList[r][c] === 'o') {
                sheepCnt += 1;
            }
            while (q.cnt > 0) {
                const [nowRow, nowCol] = q.popleft();
                for (let i = 0; i < 4; i++) {
                    const [nextRow, nextCol] = [nowRow + nrr[i], nowCol + ncc[i]];
                    if (0 <= nextRow && nextRow < row && 0 <= nextCol && nextCol < col) {
                        if (visited[nextRow][nextCol] === 0) {
                            if (mapList[nextRow][nextCol] === '.') {
                                visited[nextRow][nextCol] = 1
                                q.append([nextRow, nextCol])
                            }
                            if (mapList[nextRow][nextCol] === 'v') {
                                visited[nextRow][nextCol] = 1
                                q.append([nextRow, nextCol])
                                wolfCnt += 1;
                            }
                            if (mapList[nextRow][nextCol] === 'o') {
                                visited[nextRow][nextCol] = 1
                                q.append([nextRow, nextCol])
                                sheepCnt += 1;
                            }
                        }
                    }
                }
            }
            if (sheepCnt > wolfCnt) {
                ansSheep += sheepCnt;
            } else {
                ansWolf += wolfCnt;
            }
        }
    }
}

console.log(ansSheep, ansWolf)

