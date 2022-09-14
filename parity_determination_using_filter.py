from typing import List


def even_or_odd(list_of_numbers:List[int])-> List[int]:
    """
    Данная ф-я определяет является ли число четным или нет.
    """
    even=list(filter(lambda i: i%2==0,list_of_numbers))
    odd=list(filter(lambda i: i%2!=0,list_of_numbers))
    return "четные:", even, "нечетные:", odd
print(even_or_odd([2,3,4,5]))