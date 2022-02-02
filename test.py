N = input()
N_integer = list(map(int,input().split()))

sol = max(N_integer) - min(N_integer)
print(sol)
#print(N)
#print(N_integer)
