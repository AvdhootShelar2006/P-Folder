# Rule-Based Chatbot Using Pattern Matching Part B

import re


class RuleBasedChatbot:
    def __init__(self):
        self.rules = {
            r"\b(hi|hello|hey)\b": "Hello! How can I help you?",
            r"\bhow are you\b": "I am fine! How are you?",
            r"\b(your name|who are you)\b": "I am a simple rule-based chatbot.",
            r"\bhelp\b": "Sure! Tell me what you need help with.",
            r"\btime\b": "I cannot check the current time.",
            r"\b(bye|goodbye|exit)\b": "Goodbye! Have a nice day!"
        }

    def get_response(self, user_input):
        for pattern, response in self.rules.items():
            if re.search(pattern, user_input.lower()):
                return response
        return "Sorry, I don't understand that. Please try again."

    def chat(self):
        print("Chatbot: Hello! Start chatting with me. Type 'exit' to stop.")
        while True:
            user_input = input("You: ")
            response = self.get_response(user_input)
            print("Chatbot:", response)
            if re.search(r"\b(bye|goodbye|exit)\b", user_input.lower()):
                break


if __name__ == "__main__":
    chatbot = RuleBasedChatbot()
    chatbot.chat()
