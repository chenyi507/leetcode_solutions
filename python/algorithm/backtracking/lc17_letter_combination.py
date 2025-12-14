import unittest
from typing import List

class Solution:
    def __init__(self):
        self.letter_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz' 
        }

    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        letters = ""

        self.helper(res, letters, digits, 0)
        
        return res

    def helper(self, res: List[str], letters: str, digits: str, idx: int):
        if idx == len(digits):
            res.append(letters[:])
            return
        
        letter_lst = self.letter_dict[digits[idx]]

        for l in letter_lst:
            letters += l
            self.helper(res, letters, digits, idx + 1)
            letters = letters[:-1]
    

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        digits = "23"
        target = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        self.assertEqual(sorted(self.solution.letterCombinations(digits)), sorted(target))

if __name__ == '__main__':
    unittest.main()     