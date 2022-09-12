"""Функция, которая определяет отличается ли цвет и пол в запросе(x) от цвета и пола в рекомендации(y)"""

from typing import List
import mypy
colors=["blue","red","black","white","green","yellow","pink"]
gender=["girl","man","boy","boys","girls","woman"]

def color_gender(x:str,y:str) -> bool:
    """Функция принимает данные и в случае,если длина списка t(в нем хранятся все гендеры и цвета, которые нам встретились в запросе и рекомендации) равна двум,
    то рекомендация будет верной,если одно из слов будет гендером.
    Если длина спика t равна одному, то это может быть гендером (длина списка g будет равна 1), а может быть цветом (длина списка g равна 0)
    """
    s=set(x.split()+y.split())
    t:List[str]=list(filter(None,list(map(lambda x: x if x in colors or x in gender else None,s))))
    cg:List=list(filter(None,list(map(lambda x: x if x in gender else None,t))))
    return len(cg)==2 and len(g)==1 or len(cg)<2 and len(g)<2


print(color_gender("cats rad","blue cats"))

