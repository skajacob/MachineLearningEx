def even(start, n):
    # write your code here
    list_1=[]
    while(len(list_1) <=n):  
        if start % 2 == 0:
            list_1.append(start)
        start =+ 1 
    return list_1

even(2,4)