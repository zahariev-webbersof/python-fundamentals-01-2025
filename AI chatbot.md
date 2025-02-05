## **🧠 AI Chatbot – Python Project**  

![AI-chat-5](https://github.com/user-attachments/assets/b9800ed8-2833-4718-b33a-9d1676abc38f)


### **🎯 Learning Goals**  
1. **Understand Core Programming Concepts**: Loops, functions, and conditional statements.  
2. **Work with Data Structures**: Lists and dictionaries for chatbot responses.  
3. **Improve String Manipulation Skills**: Handling user input effectively.  
4. **Enhance Debugging Skills**: Test responses for different user inputs.  
5. **Learn Modular Programming**: Write reusable and structured functions.  

---

## **📁 Project Structure**  
```plaintext
AI_Chatbot/
├── chatbot.py          # Main chatbot program
├── responses.py        # Predefined chatbot responses
├── README.md           # Project documentation
├── test/               # Folder for testing scripts
│   ├── test_chatbot.py # Unit tests for chatbot
├── submission/         # Folder for GitHub URLs
│   ├── student1.txt    # URL of Student 1's GitHub repository
│   ├── student2.txt    # URL of Student 2's GitHub repository
└── .gitignore          # Excludes unnecessary files
```

---

## **📜 Step-by-Step Instructions**  

### **1️⃣ Build the Chatbot's Core**  
#### **Features:**  
✅ **User Greetings** – The bot greets users based on time of day.  
✅ **Predefined Responses** – The bot responds to common questions.  
✅ **User Input Handling** – The bot understands keywords.  
✅ **Learning Mode** – The bot can store new responses.  
✅ **Exit Option** – Users can type "bye" to exit.  

---

### **2️⃣ Python Code Skeleton**  

### **Advanced AI Chatbot Skeleton 🤖**

```python
import random
import datetime

# TODO: Define a dictionary with predefined responses for common user inputs.
responses = {}

# TODO: Implement a function to get a random response based on user input.
def get_response(user_input):
    pass  # Replace with logic to match user input to predefined responses.

# TODO: Implement a function to greet the user based on the current time.
def greet_user():
    pass  # Replace with logic to determine morning, afternoon, or evening greeting.

# TODO: Implement the main chatbot function that handles user interactions.
def chatbot():
    print("🤖 Chatbot: " + greet_user())
    print("🤖 Chatbot: How can I assist you today? (Type 'bye' to exit)")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("🤖 Chatbot: Goodbye! Have a great day!")
            break
        print("🤖 Chatbot:", get_response(user_input))

# TODO: Ensure the chatbot function runs only when the script is executed directly.
if __name__ == "__main__":
    chatbot()
```

---

### **3️⃣ Testing the Chatbot 🧪**  
Students should:  
✅ Test the chatbot with different greetings.  
✅ Try asking new questions and see how the bot responds.  
✅ Teach the chatbot new responses and check if it remembers.  

---

### **4️⃣ Submission Process (GitHub)**  
1️⃣ Create a GitHub repository named `AI_Chatbot`.  
2️⃣ Upload `chatbot.py`, `responses.py`, and `README.md`.  
3️⃣ Push changes and generate a GitHub repository link.  
4️⃣ Submit the link in `submission.txt`.  

---

### **🚀 Next Steps**  
- Add a **learning mode** where the chatbot remembers new responses.  
- Implement a **sentiment analysis** feature to make the bot more human-like.  
- Connect to an API to fetch **live information (weather, news, etc.)**.  

---
