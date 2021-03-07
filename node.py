# This class will be used throughout data structures.
from typing import NewType, Optional, Generic, TypeVar
T = TypeVar('T')

class Node: 


    def __init__(self, value=Generic[T], next: Optional['Node'] = None) -> None:
        self.__value = value
        self.__next = next
        
    def get_value(self) -> Generic[T]:
        '''Get the value of the Node.'''
        return self.__value
    
    def get_next(self) -> 'Node':
        '''Get the next node.'''
        return self.__next 
    
    def set_value(self, value: Generic[T]) -> None:
        '''Set the current node's value.'''
        self.__value = value
    
    def set_next(self, next: 'Node' ) -> None:
        '''Set the current's node to another node '''
        self.__next = next
    