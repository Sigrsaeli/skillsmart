
def odometer(N):
    sum = 0
    for i in range(len(N)):
        if i == 1:
            sum += N[i]*N[i-1]
        elif (i % 2 !=0) and (i != 1):
            sum += N[i-1]*(N[i] - N[i-2])
    return sum
