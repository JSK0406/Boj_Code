const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const password = input.shift().trim();

const dp = Array(password.length).fill(0);

// 20
// 02
// 2002
// 2032
// 2302

// 1일 때
if (password[0] === '0') {
    dp[0] = 0
} else {
    dp[0] = 1
}

// 2일 때
if (password.length > 1) {
    if (password[0] === '0') {
        dp[1] = 0;
    } else if (password[1] === '0') {
        if (Number(password[0]) <= 2) {
            dp[1] = 1; 
        } else {
            dp[1] = 0;
        }
    } else {
        if (Number(password[0] + password[1]) <= 26) {
            dp[1] = 2;
        } else {
            dp[1] = 1;
        } 
    }
}

if (password.length >= 3) {
    for (let i = 2; i < password.length; i++) {
        if (password[i-1] === '0') {
            if (password[i] === '0') {
                dp[dp.length-1] = 0;
                break;
            }
            dp[i] = dp[i-1] % 1000000;
        } else if (password[i] === '0') {
            if (Number(password[i-1]) <= 2 && Number(password[i-1]) > 0) {
                dp[i] = dp[i-2] % 1000000;
            } else {
                dp[dp.length-1] = 0;
                break;
            }
        } else {
            if (Number(password[i-1] + password[i]) <= 26) {
                dp[i] = (dp[i-2] + dp[i-1]) % 1000000;
            } else {
                dp[i] = dp[i-1] % 1000000;
            }
        }
    }
}

console.log(dp[dp.length-1] % 1000000)