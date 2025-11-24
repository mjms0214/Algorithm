N = int(input())

arr_list = []
for i in range(N):
    arr_list.append(int(input()))
    
arr_list.sort()

for i in range(N):
    arr_list[i] = arr_list[i]*(N-i)
 
print(max(arr_list))
    
