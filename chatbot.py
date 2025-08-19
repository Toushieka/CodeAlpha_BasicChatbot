def chatbot():
    print("Chatbot: Hi! Please type to start, type 'bye' to quit.")

    while True:
        user_input = input("User: ").lower()

        if user_input == "hello":
            print("Chatbot: Hi!")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: Please type something that I understand.")

# Starting the chatbot
chatbot()
