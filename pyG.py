m = int(input("row:"))
n = int(input("col:"))
for r in range(m):
    for c in range(n):
        if c == 0 or (c==m-2 and (r!=1 and r!=2))or ((r == 0 or r == m-1) and(c>0 and c<n-2))  or (r == int(m/2) and (c == n-2 or c==n-1)):
            print("*",end="")
        else:
            print(end=" ")
    print()
