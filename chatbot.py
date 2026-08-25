print("~" * 60)
print("             STUDENT ASSISTANT CHATBOT")
print("~" * 60)

print("\nBot: Hello! Welcome to Student Assistant.")
print("Bot: I can help you with Python, courses, internships")
print("Bot: and other common questions.")

# Show menu only once
print("\n" + "-" * 60)
print("Please choose an option:")
print("1. Learn about Python")
print("2. View available courses")
print("3. Internship information")
print("4. Working hours")
print("5. Contact information")
print("6. About the chatbot")
print("7. Help")
print("8. Exit")
print("-" * 60)

while True:

    user_input = input("You: ").strip().lower()

    # OPTION 1
    if user_input == "1":
        print("\nBot: Python is a beginner-friendly programming language.")
        print("Bot: It is used for web development, automation,")
        print("Bot: data science, artificial intelligence, and more.")

    # OPTION 2
    elif user_input == "2":
        print("\nBot: Some popular technology courses are:")
        print("Bot: 1. Python Programming")
        print("Bot: 2. Web Development")
        print("Bot: 3. Data Science")
        print("Bot: 4. Artificial Intelligence")

    # OPTION 3
    elif user_input == "3":
        print("\nBot: An internship provides practical experience.")
        print("Bot: It helps students develop technical and")
        print("Bot: professional skills through real-world projects.")

    # OPTION 4
    elif user_input == "4":
        print("\nBot: Our working hours are Monday to Friday.")
        print("Bot: 9:00 AM to 5:00 PM.")

    # OPTION 5
    elif user_input == "5":
        print("\nBot: For assistance, please contact the")
        print("Bot: internship coordinator or organization.")

    # OPTION 6
    elif user_input == "6":
        print("\nBot: I am Student Assistant.")
        print("Bot: I am a rule-based chatbot created using Python.")
        print("Bot: I use predefined rules and keyword matching")
        print("Bot: to answer user questions.")

    # OPTION 7
    elif user_input == "7":
        print("\nBot: I can help you with:")
        print("Bot: Python")
        print("Bot: Courses")
        print("Bot: Internship information")
        print("Bot: Working hours")
        print("Bot: Contact information")
        print("Bot: About the chatbot")

    # OPTION 8
    elif user_input == "8":
        print("\nBot: Thank you for asking me!")
        print("Bot: Thank you for using Student Assistant.")
        print("Bot: Goodbye!")
        print("=" * 60)
        break

    # GREETINGS
    elif user_input in ["hi", "hello", "hey"]:
        print("\nBot: Hello! Nice to meet you.")
        print("Bot: How can I help you?")

    # PYTHON WORD
    elif "python" in user_input:
        print("\nBot: Python is a beginner-friendly programming language.")
        print("Bot: It is widely used in AI, data science and web development.")

    # COURSE WORD
    elif "course" in user_input:
        print("\nBot: Available courses include Python, Web Development,")
        print("Bot: Data Science and Artificial Intelligence.")

    # INTERNSHIP WORD
    elif "internship" in user_input:
        print("\nBot: An internship gives you practical experience")
        print("Bot: and helps develop your professional skills.")

    # THANK YOU
    elif user_input in ["thanks", "thank you", "thankyou"]:
        print("\nBot: You're welcome!")

    # INVALID INPUT
    else:
        print("\nBot: I don't understand that input.")
        print("Bot: Please try another input.")

    # Show this after every answer except when exiting
    print("\nBot: Give another input or press 8 to exit.")
    