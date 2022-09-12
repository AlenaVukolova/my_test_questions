def even_or_odd(x):
    even=list(filter(lambda i: i%2==0,x))
    odd=list(filter(lambda i: i%2!=0,x))
    return "четные:", even, "нечетные:", odd
print(even_or_odd([2,3,4,5]))