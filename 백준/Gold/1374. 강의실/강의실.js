class Heapq {
    constructor() {
	    this.heap = [null];
    }

    heappush(value) {
	    let cur = this.heap.length;

	    while (cur > 1) {
	      const parent = Math.floor(cur / 2);
	      if (this.heap[parent] > value) {
	        this.heap[cur] = this.heap[parent];
	        cur = parent;
	      } else {
		      break;
	      }
	    }

	    this.heap[cur] = value;
    }

    heappop() {
        if (this.heap.length <= 1) return null;
        if (this.heap.length === 2) return this.heap.pop();

        const result = this.heap[1];
        this.heap[1] = this.heap.pop();

        let currentIndex = 1;
        let leftIndex = 2 * currentIndex;
        let rightIndex = 2 * currentIndex + 1;

        while (this.heap[currentIndex] > this.heap[leftIndex] || this.heap[currentIndex] > this.heap[rightIndex]) {
            if (this.heap[rightIndex] === undefined || this.heap[leftIndex] <= this.heap[rightIndex]) {
                [this.heap[currentIndex], this.heap[leftIndex]] = [this.heap[leftIndex], this.heap[currentIndex]];
                currentIndex = leftIndex;
            } else {
                [this.heap[currentIndex], this.heap[rightIndex]] = [this.heap[rightIndex], this.heap[currentIndex]];
                currentIndex = rightIndex;
            }
            leftIndex = 2 * currentIndex;
            rightIndex = 2 * currentIndex + 1;
        }
        return result;
    }
    
    size() {
	    return this.heap.length - 1;
    }

    head() {
	    return this.heap[1];
    }
}




const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const N = Number(input[0])

const infoArr = [];

for (let i = 1; i <= N; i++) {
	const [n, s, e] = input[i].split(' ').map(Number);
	infoArr.push([s, e])
}

infoArr.sort((a, b) => a[0]-b[0] || a[1]-b[1])

const hq = new Heapq();
hq.heappush(infoArr[0][1])

for (let i = 1; i < infoArr.length; i++) {
    const [nowStart, nowEnd] = [infoArr[i][0], infoArr[i][1]]
    if (hq.head() <= nowStart) {
        hq.heappop()
    }
    hq.heappush(nowEnd)
}

console.log(hq.size())
