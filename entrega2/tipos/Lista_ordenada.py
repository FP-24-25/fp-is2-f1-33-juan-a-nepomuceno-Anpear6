'''
Created on 8 nov 2024

@author: perez
'''

from __future__ import annotations
from typing import Generic, TypeVar, Callable
from abc import abstractmethod
from sympy.assumptions.handlers import order
from Agregado_lineal import Agregado_lineal

E = TypeVar('E')
R = TypeVar('R')

class Lista_ordenada(Agregado_lineal[E], Generic[E, R]):
    def __init__(self, order:Callable[[E], R]) -> None:
        super().__init__()
        self.__order = order
        
    @staticmethod
    def of(order:Callable[[E], R]) -> Lista_ordenada[E, R]:
        return Lista_ordenada(order)
    
    def __index_order(self, e: E) -> int:
        p:int = 0
        for i in self._elements:
            if self.__order(e) > self.__order(i):
                p += 1
        return p
    
    def add(self, e:E) -> None:
        self._elements.insert(self.__index_order(e), e)
    
    def __str__(self) -> str:
        b:list[str] = map(str, self._elements)
        return 'ListaOrdenada(' + ', '.join(b) + ')'
    
if __name__ == '__main__':
    
    lista:Lista_ordenada[str] = Lista_ordenada.of(lambda x: len(x)) #Ordenado por tamaño de la palabra
    lista.add('casa')
    lista.add('coche')
    lista.add('la')
    lista.add('esternocleidomastoideo')
    print(lista)
    
    
    
    
    
    