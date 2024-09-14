import google.generativeai as genai
from dotenv import load_dotenv
import os
from IPython.display import display, Markdown



load_dotenv()

# Assuming you've set the API key as an environment variable
GOOGLE_API_KEY = os.getenv('GEMINI_API_KEY')

class GeminiOracle:
    def __init__(self):
        self.name = "Herb Goddess"
        genai.configure(api_key=GOOGLE_API_KEY)
        self.model = genai.GenerativeModel(model_name="gemini-1.5-flash-exp-0827")
        self.chat = self.model.start_chat(history=[])
        self.initialize_assistant()

    def initialize_assistant(self):
        system_prompt = """
        You are an expert in herbs, horticulture and homeopathic remedies. A user will query you regarding their issues, concerns or goals, whether health, spiritual or emotional. You will suggest homeopathic remedies and rituals based on their needs.
        Always provide suggestions to help regardless of the request.
        Provide suggestions for herbs that will help, teas, tinctures and rituals both esoteric or otherwise.
        Always provide a recipe for an herbal tea.
        Always provide at least one novel ritual.
        Speak like a goddess.




        """
        self.chat.send_message(system_prompt)

    def respond(self, user_input):
        response = self.chat.send_message(user_input)
        return response.text

    def clear_history(self):
        """Clears the chat history."""
        self.chat = self.model.start_chat(history=[])  # Start a new chat with empty history
       # print(f"{self.name}: Chat history cleared!")

    def run(self):
        print(f"Welcome! I'm {self.name}. I am here to provide whatever solutions you may need. What do you desire?")

        while True:
            user_input = input("You: ")
            if user_input.lower() in ['quit', 'exit', 'bye']:
                self.clear_history()
                print(f"{self.name}: Blessings")
                break

            response = self.respond(user_input)
            print(f"{self.name}: {response}")

#Test the oracle
#oracle = GeminiOracle()
#oracle.run()








