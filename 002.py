# 시험을 본 과목의 개수
# 각 과목의 시험 성적

n = input()
mylist = list(map(input.split()))
mymaxlist = max(mylist)

sum = sum(mylist)

print(sum * 100 / mymaxlist / int(n))