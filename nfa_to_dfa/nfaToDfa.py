class NFAtoDFAConverter:
    def __init__(self, nfa_states, nfa_alphabet, nfa_transition_function, nfa_initial_state, nfa_final_states):
        self.nfa_states = nfa_states
        self.nfa_alphabet = nfa_alphabet
        self.nfa_transition_function = nfa_transition_function
        self.nfa_initial_state = nfa_initial_state
        self.nfa_final_states = nfa_final_states

        self.dfa_states = []
        self.dfa_transition_function = {}
        self.dfa_initial_state = None
        self.dfa_final_states = []

    def epsilon_closure(self, states):
        stack = list(states)
        closure = set(states)

        while stack:
            state = stack.pop()
            if state in self.nfa_transition_function and '' in self.nfa_transition_function[state]:
                for next_state in self.nfa_transition_function[state]['']:
                    if next_state not in closure:
                        closure.add(next_state)
                        stack.append(next_state)

        return closure

    def convert(self):
        initial_closure = self.epsilon_closure({self.nfa_initial_state})
        self.dfa_initial_state = frozenset(initial_closure)
        unmarked_states = [self.dfa_initial_state]
        self.dfa_states.append(self.dfa_initial_state)

        while unmarked_states:
            dfa_state = unmarked_states.pop()
            self.dfa_transition_function[dfa_state] = {}

            for symbol in self.nfa_alphabet:
                if symbol == '':
                    continue
                
                new_state = set()
                for nfa_state in dfa_state:
                    if nfa_state in self.nfa_transition_function and symbol in self.nfa_transition_function[nfa_state]:
                        new_state.update(self.nfa_transition_function[nfa_state][symbol])

                closure = self.epsilon_closure(new_state)
                dfa_closure_state = frozenset(closure)

                if dfa_closure_state not in self.dfa_states:
                    self.dfa_states.append(dfa_closure_state)
                    unmarked_states.append(dfa_closure_state)

                self.dfa_transition_function[dfa_state][symbol] = dfa_closure_state

        for dfa_state in self.dfa_states:
            if any(state in self.nfa_final_states for state in dfa_state):
                self.dfa_final_states.append(dfa_state)

    def print_dfa(self):
        print("DFA States:", [set(state) for state in self.dfa_states])
        print("DFA Initial State:", set(self.dfa_initial_state))
        print("DFA Final States:", [set(state) for state in self.dfa_final_states])
        print("DFA Transition Function:")
        for state in self.dfa_transition_function:
            for symbol in self.dfa_transition_function[state]:
                print(f"  {set(state)} --{symbol}--> {set(self.dfa_transition_function[state][symbol])}")

    def write_dfa_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write("DFA States:\n")
            f.write("\n".join(str(set(state)) for state in self.dfa_states) + "\n")
            f.write("DFA Initial State:\n")
            f.write(str(set(self.dfa_initial_state)) + "\n")
            f.write("DFA Final States:\n")
            f.write("\n".join(str(set(state)) for state in self.dfa_final_states) + "\n")
            f.write("DFA Transition Function:\n")
            for state in self.dfa_transition_function:
                for symbol in self.dfa_transition_function[state]:
                    f.write(f"{set(state)} --{symbol}--> {set(self.dfa_transition_function[state][symbol])}\n")

def read_nfa_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    states = set()
    alphabet = set()
    transition_function = {}
    initial_state = None
    final_states = set()

    for line in lines:
        if line.startswith("states:"):
            states = set(line.strip().split()[1:])
        elif line.startswith("alphabet:"):
            alphabet = set(line.strip().split()[1:])
        elif line.startswith("initial:"):
            initial_state = line.strip().split()[1]
        elif line.startswith("final:"):
            final_states = set(line.strip().split()[1:])
        elif line.startswith("transition:"):
            continue
        else:
            parts = line.strip().split()
            state = parts[0]
            symbol = parts[1]
            next_state = parts[2]

            if state not in transition_function:
                transition_function[state] = {}
            if symbol not in transition_function[state]:
                transition_function[state][symbol] = set()
            transition_function[state][symbol].add(next_state)

    return states, alphabet, transition_function, initial_state, final_states

# Read the NFA from .txt file
nfa_file = 'nfa.txt'
nfa_states, nfa_alphabet, nfa_transition_function, nfa_initial_state, nfa_final_states = read_nfa_from_file(nfa_file)

# Convert NFA to DFA with the convertor class
converter = NFAtoDFAConverter(nfa_states, nfa_alphabet, nfa_transition_function, nfa_initial_state, nfa_final_states)
converter.convert()

# Write the DFA to file
dfa_file = 'dfa.txt'
converter.write_dfa_to_file(dfa_file)
