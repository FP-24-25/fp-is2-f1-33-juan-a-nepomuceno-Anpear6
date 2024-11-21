'''
Created on 8 nov 2024

@author: perez
'''

from __future__ import annotations
from typing import Generic, TypeVar, Callable
from abc import abstractmethod
from Agregado_lineal import Agregado_lineal

E = TypeVar('E')

class Pila(Agregado_lineal[E]):
    def __init__(self):
        super().__init__()
    
    @staticmethod
    def of() -> Pila[E]:
        return Pila()
    
    def add(self, e:E) -> None:
        self._elements.insert(0, e)

if __name__ == '__main__':
    pass
    