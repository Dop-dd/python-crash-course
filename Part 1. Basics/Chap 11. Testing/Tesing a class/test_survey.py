import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('english')
        self.assertIn('english', my_survey.responses)


    """ Let’s verify that three responses can be stored correctly """

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""

        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['english', 'spanish', 'german']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)



if __name__ == '__main__':
    unittest.main()