def merge_arry(a1,a2):
    a = a1+a2
    a.sort()
    l = len(a)
    x = l//2
    if l%2 == 0:
        print((a[x-1] + a[x])/2)
    
    else:
        print(a[x])
        
merge_arry([1,2],[3,4])
merge_arry([1,8,2],[4,5])