from typing import Callable, Union, Set, Tuple, TypeVar, List
from dataclasses import dataclass


State = int
SymbolStart = TypeVar('SymbolStart')
SymbolBlank = TypeVar('SymbolBlank')
Symbol = Union[SymbolStart, SymbolBlank, int]

MovementLeft = TypeVar('MovementRight')
MovementRight = TypeVar('MovementLeft')
Movement = Union[MovementLeft, MovementRight]


@dataclass
class TuringMachnine:
    alphabet: Set[Symbol]
    states: Set[State]
    initial_state: State
    halting_states: Set[State]
    transition_function: Callable[[State, Symbol], Tuple[State, Symbol]]

    
    def run(self, tape: List[Symbol], steps: int = 1) -> Tuple[State, List[Symbol]]:
        """
        Run for `steps` time steps.
        """
        
        state = self.initial_state
        position = 1
        
        for t in range(steps):
            symbol = tape[position]
            state, action = self.transition_function(state, symbol)
            
            assert state in self.states
            
            if action == MovementLeft:
                position -= 1
            
            elif action == MovementRight:
                position += 1
            
            elif action in self.alphabet:
                assert action != SymbolStart
                tape[position] = action
            
            else:
                raise ValueError('Invalid action encountered in state transition')
            
            if state in self.halting_states:
                break # Stop on halting states.
        
        return state, tape
