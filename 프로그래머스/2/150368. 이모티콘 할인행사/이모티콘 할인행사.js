function solution(users, emoticons) {
    const dis_lst = []
    let plus_cnt = 0;
    let emo_price = 0;
    const backtracking = () => {
        if (dis_lst.length === emoticons.length) {
            let [tmp_cnt, tmp_price] = [0, 0];
            users.forEach((user) => {
                let userPrice = 0;
                dis_lst.forEach((dis, idx) => {
                    if (dis >= user[0]) {
                        userPrice += parseInt(emoticons[idx] * (100 - dis) / 100);
                    }
                })
                if (userPrice >= user[1]) {
                    tmp_cnt += 1;
                } else {
                    tmp_price += userPrice;
                }
            })
            if (plus_cnt < tmp_cnt) {
                plus_cnt = tmp_cnt;
                emo_price = tmp_price;
            } else if (plus_cnt === tmp_cnt) {
                emo_price = Math.max(emo_price, tmp_price);
            }
            return
        }
        
        for (let i = 0; i < 4; i++) {
            dis_lst.push([10, 20, 30, 40][i]);
            backtracking();
            dis_lst.pop();
        }
    }
    backtracking();
    return [plus_cnt, emo_price];
}