# **🔍 Validate & Extract Data with Python REGEX! 📝**  

## **👋 Welcome, Future Python Experts!**  
In this project, you will **discover the power of Regular Expressions (Regex)** by extracting, validating, and manipulating text in Python! 🐍  

By the end of this project, you’ll be able to:  
✅ Understand how **regular expressions** work.  
✅ Extract important data (emails, phone numbers, dates, etc.).  
✅ Validate user input using regex patterns.  
✅ Build a **useful tool** for text analysis!  

---

## **🛠️ Step 1: Set Up Your Project**  
📌 Open your favorite **Python editor (VS Code, PyCharm, or Jupyter Notebook)**.  
📌 Create a new **Python script** (e.g., `regex_project.py`).  

---

## **🖥️ Step 2: Extract an Email from Text**  
🔹 Your task is to **find and extract an email address** from a given text.  
🔹 Use the `re.search()` function with a **regex pattern** to match an email.  

```python
import re

def find_email(text):
    """
    This function should find and return an email address from the given text.
    Use re.search() with a regex pattern to match an email format.
    """
    # Write your regex pattern here

    # Search for the email in the text

    # Return the matched email (if found)
```

📌 **Test Case:**  
```python
text = "Hello! My email is student123@gmail.com and my phone number is +359 888-123-456."
print(find_email(text))  # Expected Output: student123@gmail.com
```

---

## **🔢 Step 3: Extract Multiple Emails & Phone Numbers**  
🔹 Your task is to **find all emails and phone numbers** in a given text.  
🔹 Use `re.findall()` to extract **multiple matches** at once!  

```python
import re

def extract_emails_and_phones(text):
    """
    This function should find and return all email addresses and phone numbers from the given text.
    Use re.findall() with proper regex patterns to match emails and phone numbers.
    """
    # Write your regex patterns here

    # Find all emails in the text

    # Find all phone numbers in the text

    # Return both lists (emails, phones)
```

📌 **Test Case:**  
```python
text = """
Contact us at support@company.com or sales@business.net.
For urgent inquiries, call +1-555-678-9999 or +44 123 4567 890.
"""
print(extract_emails_and_phones(text))  
# Expected Output: (['support@company.com', 'sales@business.net'], ['+1-555-678-9999', '+44 123 4567 890'])
```

---

## **🔐 Step 4: Validate User Input (Email & Password Checker)**  
🔹 Your task is to **validate email addresses and passwords**.  
🔹 A **valid email** should follow the format `example@domain.com`.  
🔹 A **strong password** must:  
   ✅ Be **at least 8 characters long**  
   ✅ Contain **one uppercase letter**  
   ✅ Contain **one number**  
   ✅ Contain **one special character (@$!%*?&)**  

```python
import re

def validate_email(email):
    """
    This function should check if the email is valid.
    Use re.match() with a regex pattern to match a correct email format.
    """
    # Write your regex pattern here

    # Return True if the email is valid, otherwise False


def validate_password(password):
    """
    This function should check if the password is strong.
    Use re.match() with a regex pattern to check for the required conditions.
    """
    # Write your regex pattern here

    # Return True if the password meets all conditions, otherwise False
```

📌 **Test Cases:**  
```python
print(validate_email("user@domain.com"))  # Expected Output: True  
print(validate_email("invalid-email"))    # Expected Output: False  

print(validate_password("Secure123!"))    # Expected Output: True  
print(validate_password("weakpass"))      # Expected Output: False  
```

---

## **🎯 Bonus Challenges (For Extra Learning!)**  
🚀 Want to **level up your regex skills**? Try these!  

✨ **Extract Dates** – Find dates in formats like **DD/MM/YYYY** or **MM-DD-YYYY**.  
✨ **Find URLs** – Extract all links (e.g., `https://example.com`) from text.  
✨ **Replace Words** – Replace all instances of a word (e.g., `"Python" → "Java"`).  

```python
import re

def replace_word(text, old_word, new_word):
    """
    This function should replace all occurrences of 'old_word' with 'new_word' in the given text.
    Use re.sub() for this task.
    """
    # Write your regex pattern here

    # Return the modified text
```

📌 **Test Case:**  
```python
text = "I love Python! Python is amazing!"
print(replace_word(text, "Python", "Java"))  
# Expected Output: "I love Java! Java is amazing!"
```

---

## **📌 Helpful Resources**  
🔗 [Python Regex Documentation](https://docs.python.org/3/library/re.html)  
📖 [Regex101 - Online Regex Tester](https://regex101.com/)  

---

## **📊 Grading Criteria**  
| Task                                      | Points |
|-------------------------------------------|--------|
| Successfully extracts emails & phones     | ✅ 20  |
| Validates user input correctly            | ✅ 30  |
| Uses regex creatively for extra tasks     | ✅ 20  |
| Implements at least one bonus challenge   | ✅ 30  |

---

## **🎉 Ready? Let’s Master REGEX! 🚀**  
This project is an **exciting way** to explore **pattern matching, text extraction, and data validation** using Python.  

**Happy Coding! 🐍🔥**  

---
