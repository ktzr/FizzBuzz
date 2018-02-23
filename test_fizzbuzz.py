import unittest

from fizzbuzz import we_cant_test_this


class TestFizzBuzz(unittest.TestCase):

    def test_normal_fizzbuzz_number(self):
        res = we_cant_test_this(100, {3:'Fizz',5:'Buzz'},lambda number, trigger: number % trigger == 0)
        self.assertEqual(res[0], '1')
        self.assertEqual(res[3], '4')
        self.assertEqual(res[87], '88')

    def test_normal_fizzbuzz_fizz(self):
        res = we_cant_test_this(100, {3: 'Fizz', 5: 'Buzz'}, lambda number, trigger: number % trigger == 0)
        self.assertEqual(res[2], 'Fizz')
        self.assertEqual(res[5], 'Fizz')
        self.assertEqual(res[86], 'Fizz')

    def test_normal_fizzbuzz_buzz(self):
        res = we_cant_test_this(100, {3: 'Fizz', 5: 'Buzz'}, lambda number, trigger: number % trigger == 0)
        self.assertEqual(res[4], 'Buzz')
        self.assertEqual(res[9], 'Buzz')
        self.assertEqual(res[49], 'Buzz')

    def test_normal_fizzbuzz_fizzbuzz(self):
        res = we_cant_test_this(100, {3: 'Fizz', 5: 'Buzz'}, lambda number, trigger: number % trigger == 0)
        self.assertEqual(res[14], 'FizzBuzz')
        self.assertEqual(res[29], 'FizzBuzz')
        self.assertEqual(res[89], 'FizzBuzz')


if __name__ == '__main__':
    unittest.main()
