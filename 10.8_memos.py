known = {0:0, 1:1}

def fibonnaci_memo(n):
    if n in known:
        return known[n]
    else:
        result = fibonnaci_memo(n-1) + fibonnaci_memo(n-2)
        known[n] = result
        return result
    
#print(fibonnaci_memo(10))

#print(known)

print(fibonnaci_memo(5))
