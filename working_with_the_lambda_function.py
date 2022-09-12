


def is_prime(a):
    n=set(list(map(lambda x: x if a%x==0 else 0, (2,3,4,5,6,7,8,9))))
    return len(n) ==2 if a<10 else len(n)==1

def before(x):
        d=list(set(list(map(lambda x:x if is_prime(x) else 2, range(2,x**2)))))
        return 2 if x==1 else d[:x]

def sum_of_two_nembers(f):
    c=list(filter(None,set(list(map(lambda x: (x,5-x) if 5-x in f else None,f)))))
    return c






print(sum_of_two_nembers([1,2,3,4,5,6,7,1,2,6,70]))







