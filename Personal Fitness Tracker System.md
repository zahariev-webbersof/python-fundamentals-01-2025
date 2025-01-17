# **Personal Fitness Tracker System 🏋️‍♂️**  

![health-fitness-app1200](https://github.com/user-attachments/assets/5241747a-49f6-4dcb-8aca-b86717997b22)

## 🌟 **Project Goal**  
The goal of this project is to create a fitness tracker system that enables users to:  
- Log workouts and calorie intake.   
- Track their daily progress.  
- Reset daily progress and receive motivational feedback.  

This project focuses on using **Python basics** like strings, lists, loops, conditionals, and functions, giving students practical coding experience.

---

## ✅ **Project Requirements**  

### 📌 **Tasks to Implement**  
1. **Log Workout**  
   Allow users to log the type of workout and duration (e.g., "Running" for 30 minutes).  

2. **Log Calorie Intake**  
   Allow users to log calorie intake for meals.  

3. **View Progress**  
   Display the total workout time and calorie intake for the day with motivational feedback.  

4. **Reset Progress**  
   Clear all workout and calorie data for the day.  

5. **Set Daily Goals**  
   Allow users to set goals for daily workout duration and calorie intake.  

6. **Encouragement System**  
   Provide feedback based on whether the daily goals are met.  

---

## ✅ **Additional Functions to Implement**  
### **log_workout**  
- Purpose: Add workout type and duration to the `workouts` list.  
- Input: Workout type (string), duration (float).  

### **log_calorie_intake**  
- Purpose: Add calorie intake to the `calories` list.  
- Input: Calories consumed (float).  

### **view_progress**  
- Purpose: Calculate and display total workout time and calories for the day.  
- Input: None.  

### **reset_progress**  
- Purpose: Clear all workout and calorie data for a fresh start.  
- Input: None.  

### **set_daily_goals**  
- Purpose: Allow users to set their goals for workout duration and calorie intake.  
- Input: Workout goal (float), calorie goal (float).  

### **encouragement_system**  
- Purpose: Check progress against goals and provide motivational feedback.  
- Input: None.

---

## ✅ **Code Skeleton**

```python
# Personal Fitness Tracker System 🏋️‍♂️

# Lists to store fitness data
workouts = []  # To store workout types and durations
calories = []  # To store calorie intake for meals

# Variables for daily goals
workout_goal = 0  # Daily workout goal in minutes
calorie_goal = 0  # Daily calorie intake goal

def log_workout(workout_type, duration):
    """
    Log a workout.
    - Append the workout type and duration to the workouts list.
    - Print a confirmation message.
    """
    pass

def log_calorie_intake(calories_consumed):
    """
    Log calorie intake for a meal.
    - Append the calorie amount to the calories list.
    - Print a confirmation message.
    """
    pass

def view_progress():
    """
    Display a summary of the user's progress for the day.
    - Calculate the total workout time and total calories.
    - Print motivational feedback.
    """
    pass

def reset_progress():
    """
    Clear all data from the workouts and calories lists.
    - Print a confirmation message.
    """
    pass

def set_daily_goals(workout_minutes, calorie_limit):
    """
    Set daily goals for workout time and calorie intake.
    - Update the global variables workout_goal and calorie_goal.
    - Print a confirmation message.
    """
    pass

def encouragement_system():
    """
    Provide motivational feedback based on progress and goals.
    - Compare current totals to the daily goals.
    - Print encouragement messages.
    """
    pass

def main():
    """
    Main function to interact with the user.
    """
    print("Welcome to the Personal Fitness Tracker System 🏋️‍♂️\n")
    
    while True:
        # Display menu options
        print("1. Log Workout")
        print("2. Log Calorie Intake")
        print("3. View Progress")
        print("4. Reset Progress")
        print("5. Set Daily Goals")
        print("6. Exit")
        
        # Prompt user for their choice
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            # Prompt for workout type and duration
            pass
        elif choice == '2':
            # Prompt for calories consumed
            pass
        elif choice == '3':
            # Call view_progress function
            pass
        elif choice == '4':
            # Call reset_progress function
            pass
        elif choice == '5':
            # Prompt for daily goals
            pass
        elif choice == '6':
            # Print a goodbye message and break the loop
            print("Thank you for using the Fitness Tracker. Stay healthy! 💪")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
```

---

## ✅ **How to Add the Project to GitHub**

### 📌 **Steps to Add Your Project to GitHub Using GitHub Desktop**

1. **Download and Install GitHub Desktop**  
   - If you don't already have GitHub Desktop installed, download it from the [official GitHub Desktop website](https://desktop.github.com/).  
   - Install the program and sign in with your GitHub account.

2. **Create a New GitHub Repository**  
   - Open GitHub Desktop.  
   - Go to `File > New Repository`.  
   - Fill in the details:  
     - **Name**: Give your repository a name, e.g., `fitness-tracker`.  
     - **Description**: Add a brief description, e.g., "A personal fitness tracker system built with Python."  
     - **Local Path**: Choose a folder on your computer where the repository will be stored.  
     - **Git Ignore Template**: Choose `Python` from the dropdown to exclude unnecessary files.  
   - Click **Create Repository**.

3. **Add Your Project Files**  
   - Copy your project files into the local repository folder you just created.  
   - Open GitHub Desktop, and you’ll see the changes detected under the **Changes** tab.

4. **Commit Your Changes**  
   - Add a message in the "Summary" box, e.g., `Initial commit: Added fitness tracker files`.  
   - Click **Commit to main**.

5. **Publish Your Repository to GitHub**  
   - Click the **Publish Repository** button in GitHub Desktop.  
   - Check the box **Keep this code private** if you want the repository to be private (only you can see it).  
   - Click **Publish Repository**.

6. **Push Updates to GitHub**  
   - Whenever you make changes to your project, GitHub Desktop will detect them.  
   - Add a new **Summary** for your changes, e.g., `Updated log_workout function`.  
   - Click **Commit to main**.  
   - Click **Push origin** to upload your changes to GitHub.

7. **View Your Repository Online**  
   - Open GitHub in your browser and navigate to your account.  
   - You’ll see your project listed under your repositories.  


---

## ✅ **Additional Notes for Students**  
1. **Documentation**: Add comments to your code explaining each function.  
2. **Error Handling**: Check for invalid inputs (e.g., negative numbers).  
3. **Testing**: Test your system with different inputs to ensure it works correctly.  
4. **Creativity**: Feel free to enhance the system with additional features like tracking hydration levels or sleep hours.  

Good luck, and happy coding! 🚀
