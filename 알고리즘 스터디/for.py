arr = [[1,1,1,1,1],
       [2,2,2,2,2],
       [3,3,3,3,3],
       [4,4,4,4,4],
       [5,5,5,5,5],
]


#행우선
for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j])
        #print(arr[j][i]) 열우선으로 나타낼 수 있음

#열우선
for j in range(len(arr[0])):
    for i in range(len(arr)):
        print(arr[i][j])
