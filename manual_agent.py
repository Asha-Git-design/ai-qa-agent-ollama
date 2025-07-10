# manual_agent.py
import ollama


def ask_model(prompt):
    response = ollama.chat(
        model='llama3',
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response['message']['content']


if __name__ == "__main__":
    prompt = "Write manual test cases for login functionality in a web application"
    print("[Manual Agent Output]:\n")
    print(ask_model(prompt))
