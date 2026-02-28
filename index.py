
num_list = list(map(int, input().split(",")))
largest_num = int(input())
num_list = sorted(num_list,reverse = True)
print(num_list[largest_num-1])
