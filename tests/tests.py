n = input().split()

for i in range(len(n)):
    n[i] = int(n[i])

d = n.pop()
for i in range(n[0]): 
    if i != d:
        if i - d == n[0] // 2 or d - i == n[0] // 2:  # The no. selected can be bigger or smaller than the other
            print(i)
