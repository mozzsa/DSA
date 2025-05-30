def rob_with_path(houses):
    n= len(houses)
    if n==0:
        return 0,[]
    if n==1:
        return houses[0],[0]
    
    dp = [0]*n
    dp[0]=houses[0]
    dp[1]=max(houses[0],houses[1])
    
    for i in range(2,n):
        dp[i] = max(dp[i-1], dp[i-2] + houses[i])

    # Backtrack to find the path
    path =[]
    i=n-1
    while i>=0:
        if i==0 :
            path.append(i)
            break   
        if dp[i] == dp[i-1]:
            i -= 1 # Skip this house
        else :
            path.append(i)
            i -= 2
    path.reverse()  # Reverse to get the correct order
    return dp[-1], path

#constant space solution
def rob_with_path_constant_space(houses):
  prev1, prev2 = 0, 0
  for value in houses:
    current = max(prev1, prev2 + value)
    prev2 = prev1
    prev1 = current



