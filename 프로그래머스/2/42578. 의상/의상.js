function solution(clothes) {
    var answer = 1;
    
    const myMap = new Map();
    
    for (let [a, b] of clothes) {
        if (myMap.has(b)) {
            myMap.set(b, myMap.get(b)+1)
        } else {
            myMap.set(b, 2)
        }
    }
    
    for (let [a, cnt] of myMap.entries()) {
        console.log()
        answer *= cnt
    }
    
    answer -= 1
    
    return answer;
}