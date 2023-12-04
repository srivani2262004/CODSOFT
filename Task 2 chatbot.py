

data={
    "hi":"Hi there! I'm a friendly chatbot here to assist you?",
    "hello":"Hello! How can I assist you today?",
    "hey":"Hi! Im here to interact with you",
    "what is your name":"I'm Bonita,you can even call me Boni.",
    "where are you from":"I'm from the digital world,always ready to chat and interact!",
    "how are you":"I'm just a chatbot,Im always fine,wat about you.",
    "do you have any hobbies or interests?":"I'm always busy helping users, so my hobby is chatting with people like you!",
    "what did you eat today?":"I don't eat,but I can help you find delicious recipes and food-related information.",
    "what's your favorite color?":"I'm a chatbot,so I don't have personal preferences for colors.",
    "do you enjoy listening to music?":"I can't listen to music,but I'm here to chat about it, recommend you with some good music!",
    "bye":"Bye! Take care and have a great day!",
}
def get_response(user_input):
    for pattern,response in data.items():
        if pattern in user_input:
            return response
    return "I'm sorry,I didn't understand that.Can you please rephrase your sentence?"
print("Bonita: Hi! I'm a simple chatbot,I'm here to assist you!")
while True:
    user_input=input("Me: ")
    if user_input=='bye':
       print("Bonita: Goodbye! Have a great day!")
       break
    response=get_response(user_input)
    print("Bonita:",response)
