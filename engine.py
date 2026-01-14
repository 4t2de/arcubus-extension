import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class AnalysisEngine:
    def __init__(self):
        self.model = "openai/gpt-oss-20b"
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def get_next_question(self, company, user_input=None):
        """
        Maintains state for each question. Sends the context every call.
        """
        if user_input:
            company.context.append({"role": "user", "content": user_input})

        system_message = {
            "role": "system",
            "content": f"""You are a business analyst. You are interviewing a user about the company: {company.name}.
            Company context: {company.description}
            Goal: Ask one open-ended, vague question at a time to understand what the user wants to know.
            Maintain context of the conversation. Do not repeat yourself."""
        }

        messages = [system_message] + company.context

        response = self.client.chat.completions.create(
            messages = messages,
            model = self.model,
            temperature = 0.7
        )

        ai_question = response.choices[0].message.content

        company.context.append({"role": "assistant", "content": ai_question})
        return ai_question

    def get_final_summary(self, company):
        """
        Collates the entire transcript into one single answer.
        """
        summary_instruction = {
            "role": "system",
            "content": """Collate the entire preceding conversation into a single, high-level executive summary about the company, not the user.
            Focus on the user's interests. Do not use tables. Provide the output in small, concise bullet points.
            Your main goal is to provide details about the company based on the user's answers."""
        }

        messages = [summary_instruction] + company.context

        response = self.client.chat.completions.create(
            messages = messages,
            model = self.model,
            temperature = 0.2
        )
        return response.choices[0].message.content
