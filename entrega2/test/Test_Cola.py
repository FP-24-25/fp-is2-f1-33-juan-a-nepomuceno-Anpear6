'''
Created on 8 nov 2024

@author: perez
'''

from __future__ import annotations
from typing import Generic, TypeVar, Callable
from abc import abstractmethod
from Agregado_lineal import Agregado_lineal
from Cola import Cola

if __name__ == '__main__':
    
    print('TEST DE COLA:\n\n_________________________________________________________')
    
    print('\nCreación de una cola vacía a la que se añaden con un solo\nmétodo los números: 23, 47, 1, 2, -3, 4, 5')
    micola:Cola = Cola.of()
    
    ls:list = [23, 47, 1, 2, -3, 4, 5]
    micola.add_all(ls)
    
    print('\nResultado de la cola:', micola, '\n\n_________________________________________________________')
    
    x:list = micola.remove_all()
    print('\nElementos eliminados utilizando remove_all():', x)
    
    