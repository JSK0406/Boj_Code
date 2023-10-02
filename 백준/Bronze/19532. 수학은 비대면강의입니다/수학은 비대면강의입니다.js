const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const [a, b, c, d, e, f] = input.shift().trim().split(' ').map(num => Number(num))

let [ansX, ansY] = [-1000, -1000]
for (x = -999; x < 1000; x++) {
    for (y = -999; y < 1000; y++) {
        if (a * x + b * y === c && d * x + e * y === f) {
            [ansX, ansY] = [x, y]
            break;
        }
    }
    if (ansX !== -1000) {
        break;
    }
}
console.log(ansX, ansY)