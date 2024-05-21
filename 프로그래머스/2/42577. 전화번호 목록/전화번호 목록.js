function solution(phone_book) {
    var answer = true;
    
    phone_book.sort()
    console.log(phone_book)
    
    for (let i = 0; i < phone_book.length-1; i++) {
        const [left, right] = [phone_book[i], phone_book[i+1]]
        
        let is_equal = false;
        for (let j = 0; j < Math.min(left.length, right.length); j++) {
            if (left[j] !== right[j]) {
                is_equal = true;
                break
            }
        }
        if (!is_equal) {
            answer = false;
            break;
        }
    }
    return answer;
}