import unittest
import exerciseapp

# Run all tests in class via command "python -m unittest .\testsuite\test_app.py -v"

#Test exerciseapp.app
class ExerciseAppTest(unittest.TestCase):

        def test_add(self): # test method names begin with 'test'
            self.assertEqual(1+2, 3)

if __name__ == "__main__":
    unittest.main()
