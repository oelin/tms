from turing_machine import *


writing_state = 0
halting_state = 1

def f(state, symbol):
    if symbol == 1:
        return (state, MovementRight) # Move to the right
    
    if symbol == 0:
        return (state, 1) # Fill in with a one
    
    if symbol == SymbolBlank:
        return (halting_state, SymbolBlank) # Halt


fill_with_ones = TuringMachnine(
    alphabet = {SymbolStart, SymbolBlank, 0, 1},
    states = {writing_state, halting_state},
    initial_state = 0,
    halting_states = {halting_state,},
    transition_function = f
)
