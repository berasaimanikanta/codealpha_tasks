def chatbot():
    print("🤖 Chatbot: Hello! I’m a simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello":
            print("🤖 Chatbot: Hi!")
        elif user_input == "how are you":
            print("🤖 Chatbot: I'm fine, thanks! How about you?")
        elif user_input in ["bye", "exit", "quit"]:
            print("🤖 Chatbot: Goodbye! Have a nice day 😊")
            break
        else:
            print("🤖 Chatbot: Sorry, I don’t understand that.")

# Run the chatbot
chatbot()
