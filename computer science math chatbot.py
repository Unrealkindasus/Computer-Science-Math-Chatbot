import openai

# Set up your API credentials
openai.api_key = 'YOUR_API_KEY'

def chat_with_ai(message):
    response = openai.Completion.create(
        engine='davinci-codex',
        prompt=message,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=None,
        log_level='info'
    )

    return response.choices[0].text.strip()

print("AI: Hello! I specialize in computer science and math topics. How can I assist you today?")

while True:
    user_input = input("User: ")

    if user_input.lower() == 'exit':
        print("AI: Goodbye!")
        break

    chat_prompt = f"User: {user_input}\nAI:"

    ai_response = chat_with_ai(chat_prompt)
    print(f"AI: {ai_response}")


