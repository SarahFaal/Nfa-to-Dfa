<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>NFA to DFA Converter</h1>
    <p>
        This repository contains a Python implementation of a class that converts a Non-deterministic Finite Automaton (NFA)
        into a Deterministic Finite Automaton (DFA). It also includes helper functions for reading an NFA from a file and writing
        the resulting DFA to another file.
    </p>
    <h2>Features</h2>
    <ul>
        <li><strong>NFA to DFA conversion:</strong> Handles ε-transitions (epsilon transitions) and ensures accurate computation of DFA states, transitions, and final states.</li>
        <li><strong>Input and Output:</strong> 
            <ul>
                <li>Reads the NFA definition from a <code>.txt</code> file.</li>
                <li>Writes the resulting DFA to a <code>.txt</code> file.</li>
            </ul>
        </li>
        <li><strong>Visualization:</strong> The <code>print_dfa</code> method provides a detailed view of the DFA in a readable format.</li>
    </ul>
    <h2>Installation</h2>
    <p>Ensure you have Python 3.x installed. No additional dependencies are required for this script.</p>
    <h2>Usage</h2>
    <h3>1. Define the NFA</h3>
    <p>Prepare a <code>.txt</code> file that describes your NFA. The file should follow this structure:</p>
    <pre>
states: q0 q1 q2 ...
alphabet: a b ...
initial: q0
final: q2 ...
transition:
q0 a q1
q1 b q2
q1 ε q0
    </pre>
    <ul>
        <li><strong>states:</strong> A list of all NFA states.</li>
        <li><strong>alphabet:</strong> A list of input symbols (excluding ε for epsilon transitions).</li>
        <li><strong>initial:</strong> The initial state of the NFA.</li>
        <li><strong>final:</strong> The final states of the NFA.</li>
        <li><strong>transition:</strong> State transitions in the format <code>&lt;state&gt; &lt;symbol&gt; &lt;next_state&gt;</code>. Use <code>ε</code> to represent epsilon transitions.</li>
    </ul>
    <h3>2. Run the Script</h3>
    <ol>
        <li>Save the NFA in a file (e.g., <code>nfa.txt</code>).</li>
        <li>Run the script to read the NFA, convert it to a DFA, and write the DFA to a file:
            <pre>
nfa_file = 'nfa.txt'
dfa_file = 'dfa.txt'
nfa_states, nfa_alphabet, nfa_transition_function, nfa_initial_state, nfa_final_states = read_nfa_from_file(nfa_file)

converter = NFAtoDFAConverter(nfa_states, nfa_alphabet, nfa_transition_function, nfa_initial_state, nfa_final_states)
converter.convert()
converter.write_dfa_to_file(dfa_file)
            </pre>
        </li>
    </ol>
    <h3>3. Output DFA</h3>
    <p>The resulting DFA is written to the specified output file (e.g., <code>dfa.txt</code>) in the following format:</p>
    <pre>
DFA States:
{q0, q1}
{q2}
...
DFA Initial State:
{q0}
DFA Final States:
{q2}
...
DFA Transition Function:
{q0} --a--> {q1}
{q1} --b--> {q2}
...
    </pre>
    <h3>4. Print DFA (Optional)</h3>
    <p>You can print the DFA to the console using:</p>
    <pre>
converter.print_dfa()
    </pre>
    <h3>Example NFA File</h3>
    <pre>
states: q0 q1 q2
alphabet: a b
initial: q0
final: q2
transition:
q0 a q1
q1 b q2
q1 ε q0
    </pre>
</body>
</html>
