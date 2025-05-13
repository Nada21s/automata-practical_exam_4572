def are_dfas_equivalent(dfa1, dfa2):
    # Step 1: Check if start state is also an accept state in both DFAs
    # Returns False if either start state is not an accept state
    if (dfa1["start_state"] not in dfa1["accept_states"] or 
        dfa2["start_state"] not in dfa2["accept_states"]):
        return False
    # Check if alphabets of both DFAs are identical
    if dfa1["alphabet"] != dfa2["alphabet"]:
        return False
    
    # Step 2: Check transitions with visited set to avoid infinite recursion
    # Use a set to track visited state pairs to prevent loops
    visited = set()
    states1 = list(dfa1["states"])
    states2 = list(dfa2["states"])
    start1, start2 = dfa1["start_state"], dfa2["start_state"]
    
    def is_final(state, dfa):
        # Check if a state is a final (accept) state
        return state in dfa["accept_states"]
    
    def check_transitions(current1, current2):
        # Base case: if pair already visited, return True to avoid infinite recursion
        pair = (current1, current2)
        if pair in visited:
            return True
        visited.add(pair)
        
        for symbol in dfa1["alphabet"]:
            # Get next states for the current symbol in both DFAs
            next1 = dfa1["transitions"].get((current1, symbol))
            next2 = dfa2["transitions"].get((current2, symbol))
            # If any transition is undefined, return False
            if next1 is None or next2 is None:
                return False
            # Classify next states as FS (Final State) or IS (Intermediate State)
            type1 = "FS" if is_final(next1, dfa1) else "IS"
            type2 = "FS" if is_final(next2, dfa2) else "IS"
            # If classifications differ, DFAs are not equivalent
            if type1 != type2:
                return False
            # Recursively check next states
            if not check_transitions(next1, next2):
                return False
        return True
    
    return check_transitions(start1, start2)

# Example DFAs for Section 1
dfa1 = {
    "states": {"q0", "q1", "q2"},
    "alphabet": {"a", "b"},
    "transitions": {("q0", "a"): "q0", ("q0", "b"): "q1", ("q1", "a"): "q2", ("q1", "b"): "q0", ("q2", "a"): "q1", ("q2", "b"): "q2"},
    "start_state": "q0",
    "accept_states": {"q0"}
}

dfa2 = {
    "states": {"q3", "q4", "q5", "q6"},
    "alphabet": {"a", "b"},
    "transitions": {("q3", "a"): "q3", ("q3", "b"): "q4", ("q4", "a"): "q5", ("q4", "b"): "q3", ("q5", "a"): "q6", ("q5", "b"): "q5", ("q6", "a"): "q5", ("q6", "b"): "q3"},
    "start_state": "q3",
    "accept_states": {"q3"}
}

dfa3 = {
    "states": {"q0", "q1"},
    "alphabet": {"a", "b"},
    "transitions": {("q0", "a"): "q1", ("q0", "b"): "q0", ("q1", "a"): "q0", ("q1", "b"): "q1"},
    "start_state": "q0",
    "accept_states": {"q0"}
}

dfa4 = {
    "states": {"q2", "q3"},
    "alphabet": {"a", "b"},
    "transitions": {("q2", "a"): "q2", ("q2", "b"): "q3", ("q3", "a"): "q3", ("q3", "b"): "q2"},
    "start_state": "q2",
    "accept_states": {"q2"}
}

if __name__ == "__main__":
    # Test the function 
    result = are_dfas_equivalent(dfa1, dfa2)
    print("Are the DFAs equivalent? (dfa1 vs dfa2)", result)

    result = are_dfas_equivalent(dfa3, dfa4)
    print("Are the DFAs equivalent? (dfa3 vs dfa4)", result)