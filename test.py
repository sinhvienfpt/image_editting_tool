n = int(input())

a = [1 for i in range(n)]
a[0] = 0
a[1] = 0

total = 0
for i in range(2,n):
    if a[i] == 1 :
        total += i
        j = 2*i
        while j <= n :
            a[j] = 0
            j += i
            
            
print(total)