import unittest
import exerciseapp.app as app

# Run all tests in class via command "python -m unittest .\testsuite\test_app.py -v"

#Test exerciseapp.app
class ExerciseAppTest(unittest.TestCase):

        def test_HelloWorld(self): # test method names begin with 'test'
            self.assertEqual(app.hello_world(), "<h1>Hello World!</h1>")


if __name__ == "__main__":
    unittest.main()
