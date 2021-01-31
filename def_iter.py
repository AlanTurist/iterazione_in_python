def iter(n):
    sum = 0
    sum1 = 0
    
    for i in range(0,n,1):
        sum += 7*pow(10,i)
        for j in range(1,n,1):
            sum1 = (pow(10,j+1)-10-(9*j))/81
            
    x = sum + sum1
    return x