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
    prompt = "Generate Python Selenium code to test the login functionality of a web application."
    print("[Automation Agent Output]:\n")
    print(ask_model(prompt))
