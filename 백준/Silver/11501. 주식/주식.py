import sys
input = sys.stdin.readline

T = int(input())  # 테스트 케이스 수

# 주식 하나 산다
# 원하는 만큼 판다
# 아무것도 안한다

# 거꾸로
# 해당 날에 원하는 대로 산다 => 최대 N
# 해당 날에 하나 판다

# 0 1 2 3 4
# 1 2 3 2 1

# 가장 높은 거 뽑고 => 왼쪽꺼 다 팔고

ans_lst = []
for _ in range(T):
    N = int(input())  # 날의 수
    price_lst = list(map(int, input().split()))  # 주식 정보
    
    price_lst.reverse()

    high_price = price_lst[0]

    ans = 0
    for now_price in price_lst[1:]:
        if high_price <= now_price:
            high_price = now_price
        else:
            ans += high_price - now_price
    ans_lst.append(ans)

for ans in ans_lst:
    print(ans)