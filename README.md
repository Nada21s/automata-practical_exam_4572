# automata_practical_exam_4572

## Section Number
Section 6

## Section Name
Theory of Computation

## Task Name
- Section 1: DFA Language Equivalence  
- Section 3: Turing Machine for Unary Strings with Prime Length

## Task Being Solved
- **Section 1 (DFA Language Equivalence)**: I implemented a program to check if two Deterministic Finite Automata (DFAs) accept the same language. The program checks if the start states are accepting states, ensures the alphabets match, and then recursively compares the transitions to see if they lead to the same type of states (final or intermediate).  
- **Section 3 (Turing Machine)**: I designed a Turing Machine that recognizes unary strings (strings of 1s) where the length is a prime number. The machine counts the number of 1s, checks if the count is prime, and accepts or rejects accordingly.

## Instructions on How to Run and Test the Code
- **Section 1**:
  - Make sure you have Python 3 installed on your system.
  - Save the code in `dfa_equivalence.py`.
  - Run the program using: `python dfa_equivalence.py`. It will print whether the example DFAs are equivalent.
  - To run the unit tests, use: `python test_dfa_equivalence.py`. This will test the examples and show if they pass or fail.
- **Section 3**:
  - Save the code in `turing_machine.py`.
  - Run the program using: `python turing_machine.py`. It will test an example string ("111") and print if it's accepted.
  - To run the unit tests, use: `python test_turing_machine.py`. This will test multiple cases and print the results for each.

## Full Source Code
- For Section 1:
  - `dfa_equivalence.py`: Contains the main code to check DFA equivalence with example DFAs.
  - `test_dfa_equivalence.py`: Contains unit tests for the DFA equivalence program.
- For Section 3:
  - `turing_machine.py`: Contains the Turing Machine implementation to check if the length of a unary string is prime.
  - `test_turing_machine.py`: Contains tests for the Turing Machine with various inputs.

## Requirements
- I didn't use any external libraries, so there's no dependencies. You can find an empty `requirements.txt` file in the repository just to meet the submission requirements.

## Test Cases
- **Section 1**:
  - **dfa1 vs dfa2**: Expected output: `True` (both accept strings with an even number of 'b's).
  - **dfa3 vs dfa4**: Expected output: `False` (dfa3 accepts even number of 'a's, dfa4 accepts even number of 'b's).
- **Section 3**:
  - Input "11": Expected output: `ACCEPTED` (length 2, prime).
  - Input "1111": Expected output: `REJECTED` (length 4, not prime).
  - Input "11111": Expected output: `ACCEPTED` (length 5, prime).
  - Input "111": Expected output: `ACCEPTED` (length 3, prime).
  - Input "111111": Expected output: `REJECTED` (length 6, not prime).
  - Input "1": Expected output: `REJECTED` (length 1, not prime).
  - Input "": Expected output: `REJECTED` (empty input).




