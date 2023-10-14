const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const N = Number(input.shift())
let numList = input.shift().trim().split(' ').map(Number)

let ans = 0;

const mergeSort = (left, right) => {

    if (left < right) {
        const mid = Math.floor((left + right) / 2)
        mergeSort(left, mid)
        mergeSort(mid + 1, right)
        let sortedPartialList = []
        let moveLeft = left;
        let moveRight = mid + 1;

        while (moveLeft <= mid && moveRight <= right) {
            if (numList[moveLeft] <= numList[moveRight]) {
                sortedPartialList.push(numList[moveLeft])
                moveLeft += 1;
            } else {
                sortedPartialList.push(numList[moveRight])
                ans += mid - moveLeft + 1
                moveRight += 1;
            }
        }

        if (moveLeft <= mid) {
            sortedPartialList = sortedPartialList.concat(numList.slice(moveLeft, mid + 1))
        }
        if (moveRight <= right) {
            sortedPartialList = sortedPartialList.concat(numList.slice(moveRight, right + 1))
        }

        for (let i = 0; i < sortedPartialList.length; i++) {
            numList[left + i] = sortedPartialList[i]
        }

        // numList = numList.slice(0, left) + sortedPartialList + numList.slice(right+1, numList.length)
    }
}

mergeSort(0, N-1)
console.log(ans)