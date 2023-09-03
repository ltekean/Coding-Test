N,data = int(input()),[*map(int,input().split())]+[0]

presum = [0]
for i in range(N):
  presum.append(presum[-1]+data[i])

stack,result = [],0
for i in range(N+1):
  h = data[i]
  j = i
  while stack and stack[-1][0]>=h:
    h1,j = stack.pop()
    result = max(result,(presum[i]-presum[j])*h1)
  stack.append((h,j))
print(result)