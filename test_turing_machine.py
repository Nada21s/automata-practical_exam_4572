
from turing_machine import turing_machine

def run_test(input_string, expected):
    result = turing_machine(input_string)
    verdict = "PASSED" if result == expected else "FAILED"
    status = "ACCEPTED (prime)" if result else "REJECTED (not prime)"
    print(f"Input: '{input_string.ljust(10)}' | Result: {status.ljust(30)} | Expected: {expected} | {verdict}")

# Test cases
run_test("11", True)         # Length 2, prime
run_test("1111", False)      # Length 4, not prime
run_test("11111", True)      # Length 5, prime
run_test("111", True)        # Length 3, prime
run_test("111111", False)    # Length 6, not prime
run_test("1", False)         # Length 1, not prime
run_test("", False)          # Empty input, reject
