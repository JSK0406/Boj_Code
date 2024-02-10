# 퍼즐들의 노드들의 좌표를 저장 => 절대 좌표로
# ex (2, 1 / 2, 2 / 1, 2 / 3, 2) => (1, 0 / 1, 1 / 0, 1 / 2, 1)
# row와 col의 각각의 최소값을 모든 좌표에서 빼줌

from collections import deque
import copy

def solution(game_board, table):
    answer = 0
    row, col = len(game_board), len(game_board[0])
    
    # 퍼즐 좌표를 저장하는 것
    def bfs(map_lst, zero_one):
        puzzles = []
        puzzle_visited_lst = [[0 for _ in range(col)] for _ in range(row)]
        for r in range(row):
            for c in range(col):
                if map_lst[r][c] == zero_one and not puzzle_visited_lst[r][c]:
                    puzzle_save = []
                    q = deque()
                    q.append((r, c))
                    puzzle_visited_lst[r][c] = 1
                    while q:
                        now_row, now_col = q.popleft()
                        puzzle_save.append([now_row, now_col])
                        for nr, nc in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                            next_row, next_col = now_row + nr, now_col + nc
                            if 0 <= next_row < row and 0 <= next_col < col:
                                if map_lst[next_row][next_col] == zero_one:
                                    if not puzzle_visited_lst[next_row][next_col]:
                                        q.append((next_row, next_col))
                                        puzzle_visited_lst[next_row][next_col] = 1
                    puzzles.append(puzzle_save)
                    
        return puzzles
    
    puzzle_lst = bfs(table, 1)  # 평탄화된 퍼즐들의 집합

    def to_abs(lst):
        min_row, min_col = 999_999_999, 999_999_999
        for r, c in lst:
            min_row = min(min_row, r)
            min_col = min(min_col, c)
        for idx in range(len(lst)):
            lst[idx][0] -= min_row
            lst[idx][1] -= min_col
        return lst
    
    def rotate_puzzle(lst):
        for j in range(len(lst)):
                lst[j][0], lst[j][1] = lst[j][1], -lst[j][0]
        return lst
        
    
    board_puzzles = bfs(game_board, 0)

    puzzle_used_lst = [0 for _ in range(len(puzzle_lst))]  # 퍼즐의 사용 여부
    
    for bi in range(len(board_puzzles)):
        bp = board_puzzles[bi]
        is_done = False
        for _ in range(4):
            if is_done:
                break
            bp = sorted(to_abs(rotate_puzzle(bp)), key=lambda x:(x[0], x[1]))
            for ti in range(len(puzzle_lst)):
                if puzzle_used_lst[ti]:
                    continue
                tp = sorted(to_abs(puzzle_lst[ti]), key=lambda x:(x[0], x[1]))
                if bp == tp:
                    answer += len(tp)
                    puzzle_used_lst[ti] = 1
                    is_done = True
                    break
        
    return answer