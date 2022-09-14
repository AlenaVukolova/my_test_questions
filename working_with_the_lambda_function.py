from typing import*


def is_prime(numbe:int)-> bool:
    """Функция определяет является ли число простым.
    """
    add_divisors_of_a_number=set(list(map(lambda x: x if numbe%x==0 else None, (2,3,4,5,6,7,8,9))))
    return len(add_divisors_of_a_number) ==2 if numbe<10 else len(add_divisors_of_a_number)==1



def prime_numbers(first_n:int)-> Union[int,List[int]]:
    """Функция выводит первые n простых чисел.
    """
    prime_numbers=list(set(list(map(lambda x:x if is_prime(first_n) else 2, range(2,first_n**2)))))
    return 2 if first_n==1 else prime_numbers[:first_n]



def sum_of_two_nembers(list_of_numbers:List[int])-> Tuple[List[int]]:
    """Функция которая принмает список чисел и выводит те пары чисел сумма,
    которых равна 5.
    """
    couples=list(filter(None,set(list(map(lambda x: (x,5-x) if 5-x in list_of_numbers else None,list_of_numbers)))))
    return couples






print(sum_of_two_nembers([1,2,3,4,5,6,7,1,2,6,70]))







