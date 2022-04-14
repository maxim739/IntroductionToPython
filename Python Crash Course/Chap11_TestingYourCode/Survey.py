class AnonymousSurvey:
    """Collect anonymous answers to survey question"""

    def __init__(self, question):  # Here class starts with survey question + creates an empty list to store responses
        """Store a question, and prepare to store a response"""
        self.question = question
        self.responses = []

    def show_question(self):  # This method prints the survey question
        """Show the survey question"""
        print(self.question)

    def store_response(self, new_response):  # This adds a new response to the response list
        """Store a single response to a survey"""
        self.responses.append(new_response)

    def show_results(self):  # This method prints all the responses stored in the list
        """Show all the responses that have been given"""
        print("Survey results: ")
        for response in self.responses:
            print(f"- {response}")

# To create an instance for this class all you have to do dis provide a question,
# and display the responses with show_question(), and store a response with store_response()
# Then you can view responses with show_results()
