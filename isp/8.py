data = [[1,0,0,1,0,1],
        [0,1,1,0,0,0],
        [1,1,0,0,0,0],
        [0,0,0,1,1,0],
        [0,0,0,1,0,0],
        [1,0,0,0,1,1]]
data_info = set()
from collections import deque
n,m = 6,6
count = 0
for i in range(n):
    for j in range(m):
        # data_info.append((i,j))
        if data[i][j] == 1 and (i,j) not in data_info:
            orders = deque()
            orders.append((i,j))
            data_info.add((i, j))
            while len(orders)>0:
                l = orders.popleft()

                if 0<=l[0]+1<n and data[l[0]+1][l[1]] == 1 and (l[0]+1,l[1]) not in data_info:
                    orders.append((l[0]+1,l[1]))
                    data_info.add((l[0]+1,l[1]))
                if 0<=l[0]-1<n and data[l[0] - 1][l[1]] == 1 and (l[0] - 1, l[1]) not in data_info:
                    orders.append((l[0] - 1, l[1]))
                    data_info.add((l[0] - 1, l[1]))
                if 0<=l[1]-1<m and data[l[0]][l[1]-1] == 1  and (l[0], l[1]-1) not in data_info:
                    orders.append((l[0], l[1]-1))
                    data_info.add((l[0], l[1]-1))
                if 0<=l[1]+1<m and  data[l[0]][l[1]+1] == 1 and (l[0], l[1]+1) not in data_info:
                    orders.append((l[0], l[1]+1))
                    data_info.add((l[0], l[1]+1))

            count+=1

print(count)


