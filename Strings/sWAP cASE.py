def swap_case(s):
    
    new = ""
    for i in s:
        if i.isupper() :
            new += i.lower()  # when upper swap to lower
        else:
            new += i.upper()  # else swap to upper

    return new


