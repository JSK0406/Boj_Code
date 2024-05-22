const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

// 모든 물병에 1리터씩
// 한번에 K병 옮긴다
// K개 이하의 물병으로 만든다
// 같은 양의 물을 두개를 골라서 합침

// 물병 개수, 물병 제한
let [N, K] = input.shift().split(' ').map(Number);

// 무조건 1짜리를 다 합친다
// 

// 3 1
// 1 1 1

// 4

// 13 2
// 1 1 1 1 1 1 1 1 1 1 1 1 1

// 8 8

const twoNum = [0, 1]
let nowNum = 2;
for (let _ = 0; _ < 40; _++) {
	twoNum.push(nowNum)
	nowNum *= 2
}

let ans = 0;
let numSum = 0;
let leftNum = N;
for (let i = twoNum.length-1; i >= 0; i--) {
	while (true) {
		if (leftNum - twoNum[i] >= 0) {
			leftNum -= twoNum[i];
			K -= 1;
		} else {
			break;
		}
		if (K === 1) {
			break
		}
	}
	if (K === 1) {
		break;
	}
}

for (let i = 0; i < twoNum.length; i++) {
	if (leftNum <= twoNum[i]) {
		console.log(twoNum[i]-leftNum)
		break;
	}
}