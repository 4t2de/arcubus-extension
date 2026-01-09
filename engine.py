class DiscoveryEngine:
    def __init__(self, companies):
        self.pool = companies

    def _ai_match_logic(self, company, question_text, user_answer):
        """
        Currently, this is just a placeholder, to be
        replaced with an actual LLM call.
        LLM call to be used to narrow down the list
        of companies using the company descriptions and
        the user answers to the questions.
        """
        prompt = f"""
        Company name: {company.name}
        Company description: {company.description}
        User was asked: {question_text}
        User answered: {user_answer}

        Does this company satisfy the user's requirement?
        Answer only with 'YES' or 'NO'.
        """
        pass # for now

    def filter_pool(self, question_text, user_answer):
        survivors = []

        for company in self.pool:
            if self._ai_match_logic(company, question_text, user_answer):
                survivors.append(company)

        self.pool = survivors

    def get_results(self):
        return self.pool
