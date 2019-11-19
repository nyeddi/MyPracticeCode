def findstem(arr): 
    n = len(arr) 
    s = min(arr, key=len)
    l = len(s) 
    res = "" 
    for i in range( l) : 
        #for j in range( i + 1, l + 1) : 
            stem = s[i:j]
            stem = s[0:i+1]
            k = 1
            for k in range(1, n): 
                #if stem not in arr[k]: 
                #   break
                if  not arr[k].startswith(stem): 
                    break
            if (k + 1 == n and len(res) < len(stem)):
               res = stem
               #print("response = ",res)

    return res 

if __name__ == "__main__": 
    
    arr = [ "grace", "gtraceful", 
            "gracefullll", "gracefully" ] 
    stems = findstem(arr) 
    print("output:", stems) 
