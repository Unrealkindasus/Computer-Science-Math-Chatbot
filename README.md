# Computer-Science-Math-Chatbot
This code implements a chatbot that specializes in computer science and math topics. It utilizes the OpenAI API to provide informative responses related to these subjects. The chatbot engages in a conversation with the user, answering questions and providing explanations in the fields of computer science and mathematics.

The code begins by setting up the OpenAI API credentials, requiring you to replace 'YOUR_API_KEY' with your actual OpenAI API key. This key authenticates your access to the OpenAI API services.

The chat_with_ai function serves as the core component of the chatbot. It takes a user message as input and uses the OpenAI API to generate a response. The openai.Completion.create method is called with appropriate parameters to interact with the davinci-codex language model. The response from the API is then extracted and returned as the output.

The chatbot starts by greeting the user and indicating its specialization in computer science and math. It then enters a loop, waiting for user input. The user's input is captured through the input function, allowing them to type their message. If the user enters "exit" (case-insensitive), the chatbot bids farewell and terminates the conversation.

For each user message, a chat prompt is constructed by combining the user's input with the AI's previous response. This ensures context preservation throughout the conversation. The chat_with_ai function is called, passing the chat prompt as a parameter, and the resulting AI response is printed.

The davinci-codex language model is particularly suited for computer science and math topics, capable of generating detailed and informative responses. The max_tokens parameter limits the length of the response generated by the API. The temperature parameter controls the randomness of the generated text, with lower values resulting in more deterministic responses. You can experiment with different values to adjust the AI's output.
