import unittest
from dfa_equivalence import are_dfas_equivalent, dfa1, dfa2, dfa3, dfa4

class TestDFALanguageEquivalence(unittest.TestCase):
    def test_dfa1_dfa2_equivalent(self):
        """Test if dfa1 and dfa2 are equivalent (should return True).
        Both accept strings with an even number of 'b's."""
        self.assertTrue(are_dfas_equivalent(dfa1, dfa2))

    def test_dfa3_dfa4_not_equivalent(self):
        """Test if dfa3 and dfa4 are not equivalent (should return False).
        dfa3 accepts even number of 'a's, dfa4 accepts even number of 'b's."""
        self.assertFalse(are_dfas_equivalent(dfa3, dfa4))

if __name__ == "__main__":
    unittest.main()