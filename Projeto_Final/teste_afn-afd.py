class State:
   def __init__(self, is_final):
       self.is_final = is_final
       self.transitions = {}

class AFND:
   def __init__(self):
       self.states = []
       self.start_state = None

   def add_state(self, is_final):
       state = State(is_final)
       self.states.append(state)
       return state

   def add_transition(self, start_state, symbol, end_state):
       start_state.transitions[symbol] = end_state

class AFD:
   def __init__(self):
       self.states = []
       self.start_state = None

   def add_state(self, is_final):
       state = State(is_final)
       self.states.append(state)
       return state

   def add_transition(self, start_state, symbol, end_state):
       start_state.transitions[symbol] = end_state

def convert_to_dfa(afnd):
   dfa = AFD()
   dfa.start_state = afnd.start_state
   stack = [afnd.start_state]
   while stack:
       state = stack.pop()
       if state not in dfa.states:
           dfa.add_state(state.is_final)
       for symbol, end_states in state.transitions.items():
           for end_state in end_states:
               if end_state not in dfa.states:
                  stack.append(end_state)
               dfa.add_transition(state, symbol, end_state)
   return dfa
