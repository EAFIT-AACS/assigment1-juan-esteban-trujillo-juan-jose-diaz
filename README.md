[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/95BWY5mA)
# Assignment-1---Formal-Languages

# DFA Equivalence Finder

## Student Information
- **Names:** Juan Jose Diaz Roidriguez - Juan Esteban Trujillo
- **Class Number:** 7309

## System and Tools Used
- **Operating System:** Windows 11
- **Programming Language:** Python 
- **Tools Used:** Vs code, git to upload the project

## Execution Instructions
1. Make sure you have Python 3 installed on your system.
2. Save the script as `DFAEquivalenceFinder.py`.
3. Open a terminal or command prompt in the directory where the script is located.
4. Run the following command:
   ```sh
   DFAEquivalenceFinder.py
   ```
5. To validate that the system does function, enter this input:
4
6
a b
1 2 5
0 1 2
1 3 4
2 4 3
3 5 5
4 5 5
5 5 5
6
a b
3 4 5
0 1 2
1 3 4
2 4 3
3 5 5
4 5 5
5 5 5
6
a
1 4
0 1
1 2
2 3
3 4
4 5
5 0
4
a b
0 1
0 1 2
1 1 2
2 3 1
3 3 3

## Algorithm Explanation
This program implements the minimization algorithm presented in Kozen 1997, Lecture 14. Given a Deterministic Finite Automaton (DFA) with no inaccessible states, the algorithm identifies equivalent states that can be collapsed to obtain a minimized automaton. The steps are as follows:

1. **Reading the DFA:**
   - The user specifies the number of DFAs.
   - For each DFA:
     - The number of states is entered.
     - The alphabet is input with validation to ensure they are lowercase letters.
     - The final states are specified.
     - Transition functions are read and stored.

2. **Detecting Equivalent States:**
   - An equivalence table is initialized where all states are assumed to be equivalent.
   - **Marking Phase:** Pairs of states are marked as non-equivalent if one is final and the other is not.
   - **Refinement Phase:** Transitions are checked, and states leading to non-equivalent states are marked accordingly.
   - The final list of equivalent states is generated.

3. **Displaying Results:**
   - The program prints the list of equivalent state pairs for each DFA.
   - If no equivalent states exist, it explicitly states so.

This approach efficiently determines DFA state equivalence, aligning with the minimization procedure described in Kozen 1997, Lecture 14.
