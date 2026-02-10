

t = int(input())

for _ in range(t):
    s = input()
    print(s)
# -------------------

a, b = map(int, input().split())


# ------------------
n = int(input())
arr = list(map(int, input().split()))



r,c=map(int,input().split())
matrix=[]
for _ in range(r):
    row=list(map(int,input().split()))
    matrix.append(row)


print(matrix)