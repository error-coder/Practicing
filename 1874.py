import sys

input = sys.stdin.readline
n = int(input())
stack = []
result = []
cnt = 1
tmp = True

for i in range(n):
    num = int(input())

    while cnt <= num : # cnt의 수를 오름차순 증가, stack 리스트에 추가
        stack.append(cnt)
        result.append('+')
        cnt += 1

    if stack[-1] == num: # stack 마지막 값과 입력값이 같으면
        stack.pop()
        result.append('-')
    else: # 같지 않으면 tmp => false로 바꾸고 for문 탈출
        print('NO')
        tmp = False
        break

if tmp == True: # 가능할때 result 리스트 출력
    for i in result:
        print(i)