function solution(arr)
{
    let stack = [];

    arr.forEach((num) => {
        if (stack.length === 0 || stack[stack.length-1] !== num) {
            stack.push(num)
        }
    })
    
    return stack;
}