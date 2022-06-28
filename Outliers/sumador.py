def even(start , n):
    list_1=[]
    x=1
    while (len(list_1)<=n):
        if start % 2 == 0:
            list_1.append(start)
            x =+ 1
            start =+ 1
    return list_1

even(2,4)