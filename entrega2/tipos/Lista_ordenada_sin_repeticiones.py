'''
Created on 8 nov 2024

@author: perez
'''

from __future__ import annotations
from typing import Generic, TypeVar, Callable
from abc import abstractmethod
from Agregado_lineal import Agregado_lineal
from sympy.assumptions.handlers import order
from sympy.polys import orderings

E = TypeVar('E')
R = TypeVar('R')

class Lista_ordenada_sin_repeticiones(Agregado_lineal[E], Generic[E, R]):
    def __init__(self, order:Callable[[E], R]) -> None:
        super().__init__()
        self.__order = order
        
    @staticmethod
    def of(order: Callable[[E], R]) -> Lista_ordenada_sin_repeticiones[[E], R]:
        return Lista_ordenada_sin_repeticiones(order)
    
    def __index_order(self, e: E) -> int:
        p:int = 0
        for i in self._elements:
            if self.__order(e) > self.__order(i):
                p += 1
        return p
    
    def add(self, e:E) -> None:
        if e in self._elements:
            pass
        else:
            self._elements.insert(self.__index_order(e), e)
        
    def __str__(self) -> None:
        b:list[str] = map(str, self._elements)
        return 'ListaOrdenadaSinRepeticiones(' + ', '.join(b) + ')'
        
if __name__ == '__main__':
    lista1:Lista_ordenada_sin_repeticiones[str] = Lista_ordenada_sin_repeticiones.of(lambda x: x) #Esta vez ordenado por orden alfabético
    
    lista1.add('casa')
    lista1.add('coche')
    lista1.add('la')
    lista1.add('esternocleidomastoideo')
    print(lista1)
    
    lista1.add('zapato')
    lista1.add('coche')
    print(lista1)