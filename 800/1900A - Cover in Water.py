t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    s = input()
    
    flag = True
    count = 0
    
    for i in range(n):
        # Count total dots
        if s[i] == '.':
            count += 1
            
        # Check for three dots in a row
        if i > 0 and i < n - 1:
            if s[i-1] == '.' and s[i] == '.' and s[i+1] == '.':
                print(2)
                flag = False
                break
                
    if flag == True:
        print(count)