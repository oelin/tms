from turing_machine import *


read = 0
copy_0 = 1
copy_1 = 2
then_rewind = 3
rewind = 4
decode = 5
halting_state = 6


def f(state, symbol):
    
    if state == read:
        if symbol == 0: return (state, 2)
        if symbol == 1: return (state, 3)
        if symbol == 2: return (copy_0, MovementRight)
        if symbol == 3: return (copy_1, MovementRight)

    if state == copy_0 or state == copy_1:
        if symbol == SymbolBlank:
            if state == copy_0: return (then_rewind, 2)
            if state == copy_1: return (then_rewind, 3)
        
        return (state, MovementRight)
    
    if state == then_rewind:
        if symbol == 0 or symbol == 1:
            return (rewind, MovementLeft)
        
        if symbol == SymbolStart:
            return (decode, MovementRight)
        
        return (then_rewind, MovementLeft)
    
    if state == rewind:
        if symbol == 0 or symbol == 1:
            return (rewind, MovementLeft)
        
        return (read, MovementRight)

    if state == decode:
        if symbol == SymbolBlank:
            return (halting_state, symbol)
        
        if symbol == 2: return (state, 0)
        if symbol == 3: return (state, 1)
    
        return (state, MovementRight)
        

copy_string = TuringMachine(
    alphabet = {S, B, 0, 1, 2, 3},
    states = {0, 1, 2, 3, 4, 5, 6},
    initial_state = read,
    halting_states = {halting_state, },
    transition_function = f,
)
