import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque()

# 인덱스를 하나씩 올리며 계속 찾아나감
for i in range(n):
    q.append(i + 1)

# 1보다 높은 수는 빼주고 맨 밑으로 옮김
while (len(q) > 1):
    q.popleft()
    q.append(q.popleft())

print(q.pop())