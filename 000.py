n = int(input())
num_list = []

for i in range(n):
    num_list.append(int(input()))

num_list_sec = sorted(num_list)

for i in range(len(num_list)):
    print(num_list_sec[i])