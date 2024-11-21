'''
Created on 8 nov 2024

@author: perez
'''

from __future__ import annotations
from typing import Generic, TypeVar, Callable
from abc import abstractmethod
from Agregado_lineal import Agregado_lineal

E = TypeVar('E')

class Cola(Agregado_lineal[E], Generic[E]):
    def __init__ (self) -> None:
        super().__init__()
        
    @staticmethod
    def of() -> Cola[E]:
        return Cola()
    
    def add(self, e: E) -> None:
        self._elements.insert(len(self._elements), e)
    
    def __str__(self) -> str:
        b:list[str] = map(str, self._elements)
        return 'Cola(' + ', '.join(b) + ')'
    
if __name__ == '__main__':
    pass
    