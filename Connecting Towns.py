
t = int(input().strip())
for t_itr in range(t):
    n = int(input().strip())
    routes = list(map(int, input().rstrip().split()))
    pro=1
    for i in routes:
        pro*=i
    print(pro%1234567)
