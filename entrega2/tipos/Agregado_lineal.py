'''
Created on 8 nov 2024

@author: perez
'''

from __future__ import annotations
from typing import Generic, TypeVar
from abc import ABC, abstractmethod

E = TypeVar('E')

class Agregado_lineal(Generic[E]):
    def __init__(self) -> None:
        self._elements:list[E] = []
    
    @property
    def size(self) -> int:
        return len(self._elements)
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0 
    
    @property
    def elements(self) -> list[E]:
        return self._elements  
    
    @abstractmethod
    def add(self, e:E) -> None:
        pass
    
    def add_all(self, ls:list[E]) -> None:
        for i in ls:
            self.add(i)
    
    def remove(self) -> E:
        assert len(self._elements) > 0, 'El agregado está vacío'
        e1:E = self._elements[0]
        del self._elements[0]
        return e1
    
    def remove_all(self) -> list[E]:
        removed_e:list[E] = []
        while not self.is_empty:
            removed_e.append(self.remove())
        return removed_e
        
if __name__ == '__main__':
    pass
        
