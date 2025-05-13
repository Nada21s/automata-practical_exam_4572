
# Turing Machine that accepts binary strings of 1s if their length is a **prime number**.
# Example: "11" (length 2) → ACCEPTED

def turing_machine(input_string):
    # Initialize the tape: copy input and add a blank symbol at the end
    tape = list(input_string) + ['B']
    position = 0                   # Tape head position
    state = 'q0'                   # Start state
    blank = 'B'                    # Blank symbol
    mark = 'X'                     # Used to mark read '1's

    # Transition loop: continue until reaching an accept (q3) or reject (q4) state
    while state not in ['q3', 'q4']:
        current_symbol = tape[position]

        # q0: Start reading the input
        if state == 'q0':
            if current_symbol == '1':
                tape[position] = mark  # Mark the first '1'
                state = 'q1'
                position += 1
            elif current_symbol == blank:
                state = 'q2'  # If input is empty, go check length (edge case)
            else:
                return False  # Invalid symbol

        # q1: Continue marking all '1's
        elif state == 'q1':
            if current_symbol == '1':
                tape[position] = mark
                position += 1
            elif current_symbol == blank:
                state = 'q2'  # Finished reading, go check primality
            else:
                return False

        # q2: Check if number of marked 'X's is prime
        elif state == 'q2':
            if current_symbol == blank:
                position -= 1  # Go back one cell before the blank
                if position < 0:
                    state = 'q4'  # Reject if input was empty or invalid
                continue
            elif current_symbol == mark:
                # Count how many '1's were marked (i.e. input length)
                length = sum(1 for x in tape if x == mark)

                # Reject if length is 0 or 1 (not prime)
                if length <= 1:
                    state = 'q4'
                    break

                # Check divisibility from 2 to sqrt(length)
                is_divisible = False
                for d in range(2, int(length ** 0.5) + 1):
                    if length % d == 0:
                        is_divisible = True
                        break

                # Accept if not divisible (prime), reject otherwise
                state = 'q4' if is_divisible else 'q3'
                break

    # Return True only if machine reached the accept state
    return state == 'q3'


# Example usage
if __name__ == "__main__":
    example = "111"  # Length 3 is prime
    result = turing_machine(example)
    print(f"Input: '{example}' | Result: {'ACCEPTED' if result else 'REJECTED'}")