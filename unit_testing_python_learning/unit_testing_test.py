'''
Uni testing and Test driven development in python started 08/11/2019 by Oliver B France

Levels of testing (lowest to highest importance):
1) Unit Test: Testing at the function level.
2) Component Testing - Testing is at the library and compiled binary level
3) System Testing - Tests the external interfaces of system which is a collection of sub-systems.
4) Performance Testing - Testing done at sub-system and system levels to verify timing and resource usages are acceptable.

---

1) Unit test:
- Tests individual functions.
- A test should be written for each test case for a function (all positive and negative test cases).
- Groups of tests can be combined into test suites for better organization.
- Executes in the development environment rather than the production environment.
- Execution of the test should be automated

A simple example is shown below
'''


import pytest

## production Code
#def str_len( theStr ):
#    return len(theStr)
#
## A Unit Test
#def test_string_length():
#    testStr = "1"               # Setup
#    result = str_len(testStr)   # Action
#    assert result == 1          # Assert

'''
Summary: 

An error will be raised with assert if the function is false

Unit tests are the first safety net for catching bugs before they get to the field.

Unit tests validate test cases for individual functions.

They should build and run in the developer's development environment

Unit tests should run fast!
'''


'''
What is Test Driven Development?
- A process where the developer takes personal responsibility for the quality of their code
- Unit test are written before the production code
- Dont write all the tests or production code at once
- Tests and production code are both written together in small bits of functionality


What are some of the Benefits of TDD?
- Gives you confidence to change the code
- Give you immediate feedback
- Document what the code is doing
- Drives good object oriented design.

TDD Beginnings
- Created by Kent Beck in the 1990's as part of the Extreme Programming software development process.
- He wrote the first TDD unit testing framework in Smalltalk called Sunit
- Collaborated with Erich Gamma to implement the first java unit testing framework Junit
- Junit has been the basis for many other xUnit testing frameworks written for other languages.

TDD workflow (Red, Green, Refactor)
- TDD has the following phases in its workflow:
    - Write a failing unit test (red phase)
    - write just enough production code to make that test pass (green phase)
    - Refactor the unit test and production code to make it clean (Refactor phase)
    - Repeat until the feature is complete.
    
Uncle BOB's 3 Law of TDD:
- You may not write any production code until you have written a failing unit test.
- You may not write more of a unit test than is sufficient to fail, and not compiling is failing.
- You may not write more production code than is sufficient to pass the currently failing unit test.

Current Progress: (Up to section two exercise - Quick Example TDD Session - The FizzBuzz Kata)
https://pwcanalytics.udemy.com/course/unit-testing-and-tdd-in-python/learn/lecture/8419048#overview

'''

'''
Section 3: Setting up pytest in pycharm

To set up the pytest configuration

"Run" >> "Edit Configurations" >> click on the + >> "Python Tests" >> "pytest"

Then give it a name and select ok.

Once done select run the entire script and this will bring up the red bar for the testing!

'''
## Run this get a pass or a fail.
#def test_AssertTrue():
#    assert True

'''
What is pytest?

- Pytest is a python unit tetin framework 
- Provides the ability to create Tests, Test Modules and Test Fixtures
- Uses the built-in Python assert statement
- Has command line parameters to help filter which tests are executed and in what order.

Creating a Test
- Tests are python function with "test" at the beginning of the function name.
- Tests do verification of values using the standard python assert statement.
- Similar tests can be grouped together by including them in the same module or class.

# test_SomeFunction.py
def test_someFunction():
    assert 1 == 1
    
'''
## Testing
#def test_assertTure():
#    assert True

'''
after creating the above run the following within the terminal 
'pytest -v'

This will return a version of the unit test within the terminal


Test Discovery:
-  Pytest will automatically discover tests when you execute based on a standard naming convention.
- Test functions should include 'test' at the beginning of the function name.
- Classes with tests in them should have 'test' at the beginning of the class name and not have an '__init__' method.
- Filenames of test modules should start or end with 'test'. (i.e. test_example.py or example_test.py)



*** Basically***:
- .py files must have 'test_' at the front or '_test' the end of the file for it to be detected using the command line test.
-  function within these .py files will have to have 'test' at the beginning of the function name.
- Classes must have 'test' at the beginning of the class


XUnit style setup and teardown:
- XUnit style setup/teardown functions will execute code before and after:
    - Test Modules
        - Def setup_module():
        - Def teardown_module():
    - Test Functions
        - Def setup_function():
        - Def teardown_function():
    - Test Classes
        - Def setup_class():
        - Def teardown_class():
    - Test Methods in Test Classes
        - Def setup_method():
        - Def teardown_method():
'''

# def setup_module(module):
#     print("Setup Module!")
#
# def teardown_module(module):
#     print("Teardown Module! ")
#
# def setup_function(function):
#     if function == test1:
#         print("\nSetting up test1!")
#     elif function == test2:
#         print("\nSetting up test 2!")
#     else:
#         print("\nSetting up unknown test!")
#
#
# def teardown_function(function):
#     if function == test1:
#         print("\nTearing down test1!")
#     elif function == test2:
#         print("\nTearing down test2!")
#     else:
#         print("\nTearing down unknown test!")
#
# def test1():
#     print('Executing test1!')
#     assert True
#
# def test2():
#     print('Executing test2!')

'''
ALTERNATIVE to XUnit

TEST FIXTURES:
- Test Fixtures allow for re-use of setup and teardown code across tests.
- The pytest.fixture decorator is applied to functions that are decorators.
- Individual unit tests can specify which fixtures they want executed
- The autouse parameter can be set to true to automatically execute a fixture before each test.
'''

# import pytest
#
# @pytest.fixture(autouse=True)
# def setup():
#     print("\nSetup")
#
# def test1(setup):
#     print("Executing test1!")
#
# @pytest.mark.usefixtures("setup")
# def test2():
#     print("Executing test2!")
#     assert True


'''
autouse=True gets all functions to use the setup
@pytest.mark.usefixtures("setup") gets specific function (stated line before it)
passing (setup) into the parameters of the test

Test Fixture Teardown
- Test Fixtures can each have their own optional teardown code which is called after a fixutre goes out of scope
- There are two methods for specifying teardown code. The "yield" keyword and the request-context object's "addfinalizer" methods

Test Fixture Teardown - Yield 
- When the 'Yield' keyword is used the code after the yield is executed after the fixture goes out of scope
- The "yeild" keyword is a replacement for the return keyword so any return values are also specified in the yield statement
'''
# @pytest.fixture():
# def setup():
#     print("Setup!")
#     yield
#     print("Teardown!")

'''
Test Fixture Teardown - addfinalizer.
- With addfinalizer method a teardown method is defined added via the request-context's addfinalizer method.
- Multiple finalization functions can be specified.
'''

# @pytest.fixture():
# def setup(request):
#     print("Setup!")
#     def teardown:
#         print("Teardown!")
#     request.addfinalizer(teardown)

'''
Test Fixtures Scope
- Test fixtures can have the following four different scopes which specify how often the fixture will be called:
    - Function - Run the fixture once for each test
    - Class - Run the fixture once for each class of tests
    - Module -  Run once when the module goes in scope
    - Session - The fixture is run when pytest starts.
    
Text Fixture Return Objects and Params 
    - Test Fixtures can optionally return data which can be used in the test.
    - The optional "params" array argument in the fixture decorator can be used to specify the data returned to the test.
    - When a "params" argument is specified then the test will be called one time with each value specified.
'''
# @pytest.fixture(params=[1,2])
# def setupData(request):
#     return request.param
#
# def test1(setupData):
#     print(setupData)

'''
Using Assert and testing exceptions
- Pytest allows the use of the built in python assert statement for performing verifications in a unit test.
- Comparison on all of the python data types can b e performed using the standard comparison operatiors: <,>,<=,>=,== and !=
- Pytest expands on the message retuned from assert failures to provide more context in the test results.

verifying Exceptions
- in some cases we want to verify that a function thorws an exception under certain conditions
- pytest provides the raises helper to perform this verification using the with keyword 
- if the specified exception is not raised in  the code block specified after the raises line then the test



Specifying what tests should run 
- By default PyTest will automatically discover and run all tests in all properly named modules from the current working directory and sub-directories
- There are several command ine arguments for controlling which discovered tests actually are executed.
    - moduleName - simply specify the module name to run only the tests in that module
    - DirectoryName/ - Runs any tests found in the specified directory.
    - K "EXPRESSION" - matches tests found that match the evaluatable expression in the string. The string values can include module, class 
    and function names (i.e TestClass and TestFunction)
    - -m expression - Matches tests found that have a pytest.mark decorator that matches the specified expression
    - -v Report in verbose mode
    - -q run in quiet modec(helpful when running hunderes of tests at once).
    - -s Don't capture console output
    - --ignore ignore the specified path when discovering tests  
    - --maxfail: stop after the specified number of fails
'''

