# daily_reminder.py

# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process and provide reminder
reminder = ""

match priority:
    case "high":
        if time_bound == "yes":
            reminder = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
        else:
            reminder = f"Reminder: '{task}' is a high priority task. Try to complete it as soon as possible."
    case "medium":
        if time_bound == "yes":
            reminder = f"Reminder: '{task}' is a medium priority task that should be done today."
        else:
            reminder = f"Reminder: '{task}' is a medium priority task. Plan to do it soon."
    case "low":
        if time_bound == "yes":
            reminder = f"Note: '{task}' is a low priority task, but it is time-bound. Don't forget to do it today!"
        else:
            reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority entered. Please use high, medium, or low."

# Simulate a reminder loop (for demonstration)
for i in range(1, 2):
    print(reminder)