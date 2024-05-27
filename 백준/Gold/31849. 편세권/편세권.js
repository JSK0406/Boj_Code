const { info } = require("console");
const fs = require("fs");
const { brotliCompress } = require("zlib");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
        this.pre = null;
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

    popleft() {
        if (this.cnt === 0) {
            return null;
        }

        const value = this.head.value;

        if (this.cnt === 1) {
            this.init()
        } else {
            this.head = this.head.next;
            this.head.pre = null;
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

            node.pre = tmp;

            this.tail = node;
        }

        this.cnt += 1;
    }

    getLength() {
        return this.cnt;
    }
}

const [R, C, N, M] = input.shift().split(' ').map(Number);

const visited = Array.from({length: R+1}, () => Array(C+1).fill(0));
const roomArr = [];

for (let i = 0; i < N; i++) {
    roomArr.push(input[i].split(' ').map(Number));
}

const q = new Deque();

for (let i = N; i < N+M; i++) {
    const [r, c] = input[i].split(' ').map(Number);
    visited[r][c] = 1
    q.append([r, c])
}

const nr = [0, 0, 1, -1];
const nc = [1, -1, 0, 0];

while (q.getLength() > 0) {
    const [nowRow, nowCol] = q.popleft();
    const nowPrice = visited[nowRow][nowCol]

    for (let i = 0; i < 4; i++) {
        const [nextRow, nextCol] = [nowRow+nr[i], nowCol+nc[i]];
        if (0 <= nextRow && nextRow <= R && 0 <= nextCol && nextCol <= C) {
            if (visited[nextRow][nextCol] === 0) {
                visited[nextRow][nextCol] = nowPrice + 1;
                q.append([nextRow, nextCol])
            }
        }
    }
}

let ans = 99999999999;

for (let [r, c, p] of roomArr) {
    ans = Math.min(ans, (visited[r][c] - 1) * p)
}

console.log(ans)

// visited에서 1 빼야함