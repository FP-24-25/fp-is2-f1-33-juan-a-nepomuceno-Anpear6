'''
Created on 8 nov 2024

@author: perez
'''

from __future__ import annotations
from Agregado_lineal import Agregado_lineal
from Lista_ordenada import Lista_ordenada
from typing import Generic, TypeVar, Callable
from abc import abstractmethod
from sympy.assumptions.handlers import order

E = TypeVar('E')
R = TypeVar('R')

if __name__ == '__main__':
    print('TEST DE LISTA ORDENADA: \n \n_____________________________\n')
    
    orden:Callable[[E], R] = lambda x: x
    
    print(f'Creación de una lista con criterio de orden lambda x: x')
    mi_lista:Lista_ordenada[int] = Lista_ordenada.of(orden)
    print('\nLista vacía:', mi_lista)
    
    print('\nSe añade: 3, 1, 2. En el mismo orden.\n')
    mi_lista.add(3)
    mi_lista.add(1)
    mi_lista.add(2)
    
    print('Resultado de la lista:', mi_lista, '\n\n______________________________')
    
    a:int = mi_lista.remove()
    print('\nEl elemento eliminado al utilizar remove():', a, '\n\n______________________________')
    
    b = mi_lista.remove_all()
    print('\nElementos eliminados utilizando remove_all():', b, '\n\n______________________________')
    
    print('\nComprobando si se añaden los números en la posición correcta...\n')
    mi_lista.add(3)
    mi_lista.add(1)
    mi_lista.add(2)
    
    mi_lista.add(0)
    print('Lista después de añadirle el 0:', mi_lista)
    
    mi_lista.add(10)
    print('\nLista después de añadirle el 10:', mi_lista)
    
    mi_lista.add(7)
    print('\nLista después de añadirle el 7:', mi_lista)
    
    
    
    
    