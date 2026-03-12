import random
responses = {
    "hello" : ["hello! how i can help you today"],
     "hi" : ["hi there!"],
     "how are you" : ["I'm good"],
     "bye" : ["goodbye! have a good day"],
}
def chatbot():
    while True:
        user_input = input("you: ").lower()
        if user_input == "exit":
            print("chatbot: goodbye!")
            break


        if user_input in responses:
            response = random.choice(responses[user_input])
        else:
            response = "sorry, I can't understand"

        print("chatbot:", response)
#example
chatbot()
