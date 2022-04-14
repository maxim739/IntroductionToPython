# Here we will be able to prove that our classes will work properly, which is much like testing a function
# If your classes pass tests, then you can be confident in your code and make sure new additions wont break your class

# There are a variety of different assert methods, look at the test document in this file to see the whole list
# Python provides a wide arrange of tests to see if many conditions are True or False in use for testing


# Class to test
# Testing a class is similar to testing a function, where ytesting tests methods in the class with few differences
# The class we are going to test is in the file survey.py
# Here we will write a program that uses this class
from Survey import AnonymousSurvey

# Define a question and make a survey
question = "What language did you first learn to speak? "
my_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
my_survey.show_question()
print("Enter 'q' at any time to quit:\n ")
while True:
    response = input("Language: ")
    if response == 'q':
        break

    my_survey.store_response(response)

# Show the survey results
print("\nThank you to everyone who participated in the survey! ")
my_survey.show_results()

# This program defines the question asked and creates an AnonymousSurvey object with that question
# The program calls show_question to display the question when prompted
# show_results is called to show the results of the survey

# There are other improvements we can make to the Survey function, which could result in changes
# To make sure the program doesn't act weird now we can use testing


# Testing the AnonymousSurvey Class
# Now we will write a test which verifies one aspect of the anonymoussurvey class
# We will verify that a single response to the survey question is stored properly
# We will use the assertIn() method to determine if a solution is in a list of responses
import unittest  # Import unittest module


class TestAnonymousSurvey(unittest.TestCase):  # Call test case TestAnonymousSurvey inheriting from unittest.TestCase
    """Tests for the class Anonymous Survey"""  # First method tests if a response ends up in the responses list

    def test_store_single_response(self):  # Descriptive name to show what we are testing
        """Test that a single response is stored correctly"""
        question = "What language did you first learn to speak? "
        my_survey = AnonymousSurvey(question)  # Create instance of class and store a response with store_response()
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)  # Check that response was stored in my_survey.responses

    # Now we can create another method which tests for more than one response
    def test_store_three_responses(self):
        """Test that three individual responses are stored correctly"""
        question = "What language did you first learn to speak? "
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']	# Create a list with three different responses
        for response in responses:	# Call store_response on all responses in responses
            my_survey.store_response(response)
        for response in responses:	# Assert each response in another loop
            self.assertIn(response, my_survey.responses)

# Now we will use the setUp() Method so we don't have to keep creating new instances of examples in each test
# Now we will use setUp() to create a survey instance and a set of responses which can be used further down
    def setUp(self):
        """Create a survey and a set of responses for use in all test methods"""
        question = "Which language did you first learn to speak? "
        self.my_survey = AnonymousSurvey(question)	# This creates a survey instance
        self.responses = ['English', 'Spanish', 'Mandarin']	# This creates a list of responses

# These are prefixed by 'self' so that they can be used anywhere in the class, not only in that function

    def test_store_single_responses_withsetup(self):	# First response in list responses is verified stored correctly
        """Test that a single response is stored properly"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses_withsetup(self):	# Verified all responses in responses stored correctly
        """Test that three responses are stored correctly"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()
