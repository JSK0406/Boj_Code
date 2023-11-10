import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    max_weight, class_cnt = map(int, input().split())
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))
    lst3 = list(map(int, input().split()))
    lst4 = list(map(int, input().split()))

    sum_lst1 = []
    sum_lst2 = []

    for i in range(class_cnt):
        for j in range(class_cnt):
            sum_lst1.append(lst1[i] + lst2[j])
            sum_lst2.append(lst3[i] + lst4[j])
    
    sum_lst1.sort()
    sum_lst2.sort()

    ans = 999_999_999_9
    left, right = 0, len(sum_lst1) - 1
    while (left <= len(sum_lst1) - 1 and right >= 0):
        now_sum = sum_lst1[left] + sum_lst2[right]
        if (abs(max_weight - ans) < abs(max_weight - now_sum)):
            pass
        elif (abs(max_weight - ans) > abs(max_weight - now_sum)):
            ans = now_sum
        else:
            if (now_sum < ans):
                ans = now_sum
        if ans == max_weight:
            break;
        if (now_sum < max_weight):
            left += 1
        else:
            right -= 1
    print(ans)