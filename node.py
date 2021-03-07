from typing import NewType, Optional, Generic, TypeVar
T = TypeVar('T')

class Node: 

    '''
    Class that holds a value and points to another Node class.
     
    Parameters:
        value (Generic[T]) : The value of the Node
        next ('Node')      : The next Node to point to
    '''

    def __init__(self, value=Generic[T], next: Optional['Node'] = None) -> None:
        '''
        Initialize the Node class with a value and a pointer to the next node.
      
        Parameters:
            value (Generic[T]) : The value of the Node
            next ('Node')      : The next Node to point to
      
        Returns:
            None
        '''
        
        self.__value = value
        self.__next = next
        
    def get_value(self) -> Generic[T]:
        '''
        Get the value of the Node.
        
        Returns:
            Generic[T] : The value of the current Node
        '''
        
        return self.__value
    
    def get_next(self) -> 'Node':
        '''
        Get the next node.
        
        Returns:
            'Node' : The Node that the current node points to
        '''
        
        return self.__next 
    
    def set_value(self, value: Generic[T]) -> None:
        '''
        Set the current node's value.
        
        Parameters:
            value (Generic[T]) : The new value of the current Node
        
        Returns:
            None
        '''
        
        self.__value = value
    
    def set_next(self, next: 'Node' ) -> None:
        '''
        Set the current's node to another node. Changes where the Node points to.
        
        Paremeters:
            next ('Node') : Change the current Node's next value to another Node
        
        Returns:
            None
        '''
        
        self.__next = next
    