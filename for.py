def even_or_odd(x):
    even=[]
    odd=[]
    for i in x:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return "четные:",even, "нечетные:",odd


