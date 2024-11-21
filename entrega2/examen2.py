'''
Created on 21 nov 2024

@author: perez
'''

from __future__ import annotations
from typing import Generic, TypeVar, Callable
from abc import abstractmethod
from Agregado_lineal import Agregado_lineal

E = TypeVar('E')

#Ejercicio 1

class ColaConLimite(Agregado_lineal[E], Generic[E]):
    def __init__ (self, capacidad:int) -> None:
        super().__init__()
        self._capacidad = capacidad
    
    @staticmethod    
    def of(capacidad:int) -> ColaConLimite[E]:
        return ColaConLimite(capacidad)
    
    def add (self, e:E) -> None:
        if len(self._elements) < self._capacidad:
            self._elements.insert(len(self._elements), e)
        else:
            raise OverflowError('La cola está llena')
        
    def is_full(self) -> bool:
        return len(self._elements) == self._capacidad
        
if __name__ == '__main__':
    # Test de la clase ColaConLimite (Ejercicio 1)
    cola = ColaConLimite.of(3) #Instanciamos la cola
    
    print(cola.is_empty) #Comprobamos que está vacía
    
    cola.add('Tarea 1')  
    cola.add('Tarea 2')
    cola.add('Tarea 3') #Añadimos el límite de elementos a la cola
   
    print(cola.is_full()) #Comprobamos que está llena
     
    try:                            #Probamos a añadir un elemento a la lista llena para comprobar que el control de errores funciona
        cola.add('Tarea 4')
    except OverflowError as e:
        print(e)
    
    print(cola.remove())    #Eliminamos y mostramos el primer elemento de la cola
    
    print(cola.remove_all())  #Eliminamos el resto de elementos
    print(cola.is_empty)        #Comprobamos que la cola está vacía
    
    cola = ColaConLimite.of(5) #Instanciamos una nueva cola con capacidad 5
    
    print(cola.is_empty) #Comprobamos que está vacía
    
    cola.add(0)
    cola.add(1)
    cola.add(2)
    cola.add(-2)
    cola.add(-1) 
    
    #Hemos comprobado anteriormente que el control de errores funciona correctamente 
    
    print(cola.contains(0))     #Probamos el método contains
    print(cola.contains(8))
    
    print(cola.find(lambda x: x == 0))   #Probamos el método find
    
    print(cola.filter(lambda x: x < 1))    #Probamos el método filter
    