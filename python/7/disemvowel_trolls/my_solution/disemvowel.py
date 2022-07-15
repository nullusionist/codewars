def disemvowel(string_):
    n = string_
    for x in string_.lower():
        if x in ('a','e','i','o','u','0'):
            n = n.replace(x,"")
    return n