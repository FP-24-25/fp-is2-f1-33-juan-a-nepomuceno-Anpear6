'''
Created on 8 nov 2024

@author: perez
'''

from __future__ import annotations
from typing import Generic, TypeVar, Callable
from abc import abstractmethod
from Agregado_lineal import Agregado_lineal

P = TypeVar('P')
E = TypeVar('E')

class Cola_de_prioridad (Generic[E, P]):
    def __init__(self) -> None:  
        self._elements:list[E] = []
        self._priorities:list[P] = []
        
    def size(self) -> int:
        return len(self._elements)
    
    def is_empty(self) -> bool:
        return self.size() == 0
    
    def elements(self) -> list[E]:
        return self._elements
    
    def add(self, e: E, priority: P) -> None:
        p:int = 0
        for i in self._priorities:
            if priority > i:
                p += 1
        self._priorities.insert(p, priority)
        self._elements.insert(p, e)
        
    def add_all(self, ls:list[tuple[E, P]]) -> None:
        for t in ls:
            self.add(t[0], t[1])

    def remove(self) -> E:
        assert len(self._elements) > 0, 'El agregado está vacío'
        
        removed_e:E = self._elements[0]
        
        del self._elements[0]
        del self._priorities[0]
        
        return removed_e
    
    def remove_all(self) -> list[E]:
        assert not self.is_empty(), 'El agregado está vacío'
        
        removed_ls:list[E] = []
        
        while not self.is_empty():
            removed_ls.append(self.remove())
            
        return removed_ls
    
    def index_order(self, p:P) -> int:
        p:int = 0
        
        for i in self._priorities:
            if i > p:
                p += 1
        
        return p
    
    def remove_e(self, e:E) -> None:
        assert not self.is_empty(), 'El agregado está vacío'
        
        i:int = self._elements.index(e)
        del self._elements[i]
        del self._priorities[i]
    
    def decrease_priority(self, e:E, new_priority:P) -> None:
        e_index:int = self._elements.index(e)
        e_priority:P = self._priorities[e_index]
        
        if new_priority > e_priority:
            self.remove_e(e)
            self.add(e, new_priority)
            
    def __str__(self) -> str:
        b:list[str] = map(str, self._elements)
        return 'ColaPrioridad(' + ', '.join(b) + ')'
        
if __name__ == '__main__':
    
    tareas:Cola_de_prioridad = Cola_de_prioridad()
    tareas.add('comer', 2)
    tareas.add('estudiar', 4)
    print(tareas)
    
    tareas.add_all([('duchar', 5), ('hablar', 6), ('dormir', 3)])
    print(tareas)
    
    print(tareas.index_order(4))
    print(tareas)
    tareas.decrease_priority('estudiar', 8)
    print(tareas)
    
    print(tareas.remove())
    print(tareas)
    
    print(tareas.remove_all())
    print(tareas)
    
    
    

