class Node {
    constructor(value) {
        this.value = value;
        this.next = null
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
        this.tail = null;
    }

    appendleft(value) {
        const node = new Node(value);

        if (!this.head) {
            this.head = node;
            this.tail = node;
        } else {
            const tmp = this.head;
            tmp.prev = node;

            this.head = node;

            node.next = tmp;
        }

        this.cnt += 1;
    }

    popleft() {
        if (this.cnt === 0) return -1;

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

    pop() {
        if (this.cnt === 0) return -1;

        const value = this.tail.value;

        if (this.cnt === 1) {
            this.init();
        } else {
            this.tail = this.tail.prev;
            this.tail.next = null;
            this.cnt -= 1;
        }

        return value;
    }

    length() {
        return this.cnt;
    }

    showHead() {
        if (this.cnt === 0) {
            return -1
        } else {
            return this.head.value;
        }
    }
    
    showTail() {
        if (this.cnt === 0) {
            return -1
        } else {
            return this.tail.value;
        }
    }
}


const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const [row, col] = input.shift().split(' ').map(Number);
const mapList = [];
const visited = Array.from({length: row}, () => Array(col).fill(0))

for (let i = 0; i < row; i++) {
    mapList.push(input[i].split('').map(Number))
}

const q = new Deque();
q.append([0, 0])
visited[0][0] = 1

const nrr = [0, 0, 1, -1];
const ncc = [1, -1, 0, 0];

while (visited[row-1][col-1] === 0) {
    const [nowRow, nowCol] = q.popleft();
    const nowCnt = visited[nowRow][nowCol];

    for (let i = 0; i < 4; i++) {
        const [nextRow, nextCol] = [nowRow + nrr[i], nowCol + ncc[i]];

        if (0 <= nextRow && nextRow < row && 0 <= nextCol && nextCol < col) {
            if (visited[nextRow][nextCol] === 0 && mapList[nextRow][nextCol] === 1) {
                visited[nextRow][nextCol] = nowCnt + 1;
                q.append([nextRow, nextCol])
            }
        }
    }
}

console.log(visited[row-1][col-1])