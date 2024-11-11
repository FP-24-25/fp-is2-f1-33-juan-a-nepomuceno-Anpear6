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
from Lista_ordenada_sin_repeticiones import Lista_ordenada_sin_repeticiones

E = TypeVar('E')
R = TypeVar('R')

if __name__ == '__main__':
    
    print('TEST DE LISTA ORDENADA SIN REPETICIÓN:\n\n_________________________________________________________')
    
    print('\nCreación de una lista con criterio de orden lambda x: -x\n')
    orden:callable[[E], R]
    lista_sr:Lista_ordenada_sin_repeticiones = Lista_ordenada_sin_repeticiones.of(lambda x : -x)
    
    print('Se añaden: 23, 47, 47, 1, 2, -3, 4 y 5. En ese orden\n')
    lista_sr.add(23)
    lista_sr.add(47)
    lista_sr.add(47)
    lista_sr.add(1)
    lista_sr.add(2)
    lista_sr.add(-3)
    lista_sr.add(4)
    lista_sr.add(5)
    
    print('Resultado de la lista ordenada sin repetición:', lista_sr, '\n\n_________________________________________________________')
    
    c:int = lista_sr.remove()
    print('\nEl elemento eliminado al utilizar remove():', c, '\n\n_________________________________________________________')
    
    d:list = lista_sr.remove_all()
    print('\nElementos eliminados utilizando remove_all():', d, '\n\n_________________________________________________________')
    
    print('\nComprobando si se añaden los números en la posición correcta...\n')
    lista_sr.add(23)
    lista_sr.add(47)
    lista_sr.add(47)
    lista_sr.add(1)
    lista_sr.add(2)
    lista_sr.add(-3)
    lista_sr.add(4)
    lista_sr.add(5)
    
    lista_sr.add(0)
    print('Lista después de añadirle el 0:', lista_sr, '\n')
    
    lista_sr.add(0)
    print('Lista después de añadirle el 0:', lista_sr, '\n')
    
    lista_sr.add(7)
    print('Lista después de añadirle el 7:', lista_sr)