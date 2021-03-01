def energy(n,w):
    
    
    if len(n) == 3:
        return w[0]*w[2]
    
    else:
        max_value = 0
        
        for i in range(len(n)-2):
            
            if w[i]*w[i+2] >max_value:
                max_value = n[i+1]*n[i-1]
                idx = i
        del w[idx+1]
        w.append(0)


    return max_value + energy(n-1)


n=list(range(int(input())))
w=[1,2,3,4]

print(energy(n,w))





    
        