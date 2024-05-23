class Heapq {
    constructor() {
        this.heap = [];
    }

    heapifyUp() {
        let idx = this.heap.length - 1;
        while (idx > 0) {
            const parentIdx = Math.floor((idx-1) / 2);
            if (this.heap[parentIdx] <= this.heap[idx]) {
                break;
            } 
            [this.heap[parentIdx], this.heap[idx]] = [this.heap[idx], this.heap[parentIdx]];
            idx = parentIdx;
        }
    }

    heapifyDown() {
        let idx = 0;
        const length = this.heap.length;

        while (true) {
            let smallIdx = idx;
            const leftIdx = 2 * idx + 1;
            const rightIdx = 2 * idx + 2;

            if (leftIdx < length && this.heap[leftIdx] < this.heap[smallIdx]) {
                smallIdx = leftIdx;
            }

            if (rightIdx < length && this.heap[rightIdx] < this.heap[smallIdx]) {
                smallIdx = rightIdx;
            }

            if (smallIdx === idx) {
                break;
            }

            [this.heap[idx], this.heap[smallIdx]] = [this.heap[smallIdx], this.heap[idx]];
            idx = smallIdx;
        }
    }

    size() {
        return this.heap.length;
    }

    heappush(value) {
        this.heap.push(value);
        this.heapifyUp();
    }

    heappop() {
        if (this.size() === 0) {
            return null;
        }

        const root = this.heap[0];
        const last = this.heap.pop();

        if (this.size() > 0) {
            this.heap[0] = last;
            this.heapifyDown();
        }

        return root;
    }
}


const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const N = Number(input.shift())

const hq = new Heapq();

for (let i = 0; i < N; i++) {
    const nowInput = input[i]
    if (nowInput[0] === '0') {
        if (hq.size() === 0) {
            console.log(-1)
        } else {
            console.log(-hq.heappop())
        }
    } else {
        const lst = nowInput.split(' ').map(Number);
        const NN = lst.shift();
        for (let j = 0; j < NN; j++) {
            hq.heappush(-lst[j])
        }
    }
}