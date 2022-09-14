from typing import List,Tuple


def even_or_odd(list_of_numbers:List[int])-> \
    Tuple[str, List[int], str, List[int]]:
    """Данная ф-я определяет являются ли числа
    из входящего списка четными или нет и возвращает два
    списка, в первом из них четные числа, во втором нет"""
    even=[]
    odd=[]
    for number in list_of_numbers:
        if number%2==0:
            even.append(number)
        else:
            odd.append(number)
    return "четные:",even, "нечетные:",odd


