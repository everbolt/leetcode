from math import sqrt

def solution(n):
    def euler(n): #Ref: Chai Wah Wu, Sep 08 2021
        m = int(sqrt(24*n+1))
        return 0 if m**2 != 24*n+1 else ((-1)**((m-1)//6) if m % 6 == 1 else (-1)**((m+1)//6))
    
    data_step, data_euler = {0: 1}, {}
    def step(n):
        if n in data_step:
            return data_step[n]
        else:
            total = 0
            for k in range(1, int(sqrt(n))+1):
                if k not in data_step:
                    data_step[n-k**2] = step(n-k**2)
                total += ((-1) ** (k + 1) * data_step[n-k**2])
            if n not in data_euler:
                data_euler[n] = euler(n)
            data_step[n] = data_euler[n] + 2 * total    
            return data_step[n]
    return step(n) - 1
    
print(solution(200))