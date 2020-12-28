from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))


# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)


# #내가 짠 코드 - 조금 더 복잡함
# # Down, Up, Right, Left
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
# result = 0
#
# def dfs():
#     global result
#     q = deque([])
#     flag = True
#     while flag:
#         for row, line in enumerate(graph):
#             if 0 in line:
#                 result += 1
#                 col = line.index(0)
#                 q.append((row, col))
#                 while q:
#                     x, y = q.popleft()
#                     graph[x][y] = 1
#                     for i in range(4):
#                         nx = x + dx[i]
#                         ny = y + dy[i]
#                         if 0 <= nx < n and 0 <= ny < m:
#                             if graph[nx][ny] == 0:
#                                 q.append((nx, ny))
#         flag = False
#         for row in graph:
#             if 0 in row:
#                 flag = True
#                 break
#     print(result)
#
#
# dfs()
