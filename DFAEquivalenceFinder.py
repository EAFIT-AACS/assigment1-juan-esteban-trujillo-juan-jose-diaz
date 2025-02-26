# Function that reads a DFA from the standard input.
def readDFA():
    DFAs = []

    nDFA = int(input())
    
    # Read the number of states, the alphabet, the final states and the transitions of each DFA.
    for i in range(nDFA):
        nStates = int(input())

        while True:
            alphabet = input("").split()
    
            if all(c.isalpha() and c.islower() and len(c) == 1 for c in alphabet):
                break
            print(" Error: Only lowercase letters (a-z) are allowed. Try again.")
            
        finalStates = set(map(int, input().split()))

        transitions = {state: {} for state in range(nStates)}  

        
        for state in range(nStates):
            values = list(map(int, input().split()))

            for j, symbol in enumerate(alphabet):
                    transitions[values[0]][symbol] = int(values[j+1])
        
        # Add the DFA to the list of DFAs.
        DFAs.append((nStates, alphabet, finalStates, transitions))

    return DFAs

def findEquivalents(nStates, alphabet, finalStates, transitions):
    # Create a table to store the equivalent states.
    equivalenceTable = [[True] * nStates for i in range(nStates)]
    
    equivalentStates = []
    
    # Mark the states that are different, where one is final and the other is not or vice versa (First Filter).
    for i in range(nStates):
        for j in range(i+1, nStates):
            if (i in finalStates and j not in finalStates) or (i not in finalStates and j in finalStates):
                equivalenceTable[i][j] = equivalenceTable[j][i] = False
    
    # Mark the states that are equivalent (Second Filter).
    changes = True
    while changes:
        changes = False
        for i in range(nStates):
            for j in range(i+1, nStates):
                if equivalenceTable[i][j] == True:
                    for symbol in alphabet:
                        state_i = transitions[i][symbol]
                        state_j = transitions[j][symbol]
                        if equivalenceTable[state_i][state_j] == False:
                            equivalenceTable[i][j] = equivalenceTable[j][i] = False
                            changes = True
                            break
    
    # Add the equivalent states to the list.
    for i in range(nStates):
        for j in range(i+1, nStates):
            if equivalenceTable[i][j] == True:
                equivalentStates.append((i, j))
    
    return equivalentStates
    
# Main function.
DFAs = readDFA()

for i, (nStates, alphabet, finalStates, transitions) in enumerate(DFAs):
    
    equivalents = findEquivalents(nStates, alphabet, finalStates, transitions)
    
    print(f"\n✅ Equivalent states found in automaton {i+1}: ✅")
    if len(equivalents)>0:
        for pair in equivalents:
            print(pair)
    else:
        print("No equivalent states.")