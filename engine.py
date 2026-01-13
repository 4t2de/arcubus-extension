import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class DiscoveryEngine:
    def __init__(self, companies):
        self.pool = companies
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def _ai_match_logic(self, company, question_text, user_answer):
        # We define a very strict prompt for the reasoning model
        prompt = f"""
        Evaluate if the company matches the user's requirement.

        Company: {company.name}
        Description: {company.description}
        Question Asked: {question_text}
        User Answer: {user_answer}

        Decision Criteria: Does the company description align with the user's answer?
        Output: 'YES' or 'NO' only.
        """

        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are a binary classifier. You only output YES or NO."
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model="openai/gpt-oss-20b",
                temperature=0,
            )

            # Extract and clean the response
            raw_answer = chat_completion.choices[0].message.content.strip().upper()

            # Robust check for "YES"
            return "YES" in raw_answer

        except Exception as e:
            # If the specific model fails, we print the error for debugging
            print(f"Error calling AI for {company.name}: {e}")
            return False

    def filter_pool(self, question_text, user_answer):
        survivors = []
        print(f"\n--- AI is sieving {len(self.pool)} companies ---")

        for company in self.pool:
            if self._ai_match_logic(company, question_text, user_answer):
                survivors.append(company)

        self.pool = survivors

    def get_results(self):
        return self.pool
