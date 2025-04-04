# Version 1: For multiple solutions
def backtrack(candidate):

    # Base case: If the candidate is a solution, output it
    if candidate is a solution:
        return candidate

    # Iterate through all possible next candidates
    for next_candidate in candidates:
        # Check if the next candidate is valid
        if is_valid(next_candidate):
            # Place the next candidate
            place(next_candidate)
            # Recursively call backtrack with the new candidate
            backtrack(next_candidate)
            # Remove the candidate to backtrack and try other possibilities
            remove(next_candidate)

def solve():

    # Start with an initial empty candidate
    initial_candidate = []

    # Begin the backtracking process
    backtrack(initial_candidate)



# Version 2: if you only want 1 solution (function will end when it reaches a solution)
def backtrack(candidate):

    # Base case: If the candidate is a solution, output it
    if candidate is a solution:
        return True

    # Iterate through all possible next candidates
    for next_candidate in candidates:

        # Check if the next candidate is valid
        if is_valid(next_candidate):

            # Place the next candidate
            place(next_candidate)

            # Recursively call backtrack with the new candidate
            if backtrack(next_candidate):
                output(candidate)
	
            # Remove the candidate to backtrack and try other possibilities
            remove(next_candidate)

    return False

def solve():

    # Start with an initial empty candidate
    initial_candidate = []
    
    # Begin the backtracking process
    backtrack(initial_candidate)
