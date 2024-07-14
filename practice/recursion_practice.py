# Recursion add
    
def rec_add(num):
    if num == 10:
        return num
    else:
        print(num)
        return num + rec_add(num+1)
    


print(rec_add(0)) 
        