function solution(progresses, speeds) {
    var answer = [];
    
    let stack = [];
    
    for (let i = 0; i < speeds.length; i++) {
        const [pro, speed] = [progresses[i], speeds[i]];
        const [div, mod] = [Math.floor((100-pro)/speed), (100-pro)%speed]

        if (mod === 0) {
            stack.push(div)
        } else {
            stack.push(div+1)
        }
    }
    
    let cnt = 1;
    let maxDay = stack[0];
    for (let i = 1; i < stack.length; i++) {
        const now = stack[i];
        if (maxDay < now) {
            maxDay = now;
            answer.push(cnt);
            cnt = 1;
        } else {
            cnt += 1;
        }
    }
    console.log(stack)
    answer.push(cnt);
    return answer;
}