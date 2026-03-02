# daily_reminder.py

def get_task_info():
    task = input("Enter your task: ").strip()
    
    # Ensure valid priority using a loop
    while True:
        priority = input("Priority (high/medium/low): ").strip().lower()
        if priority in ("high", "medium", "low"):
            break
        else:
            print("Please enter a valid priority: high, medium, or low.")
    
    # Ensure valid time-bound response
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
        if time_bound in ("yes", "no"):
            break
        else:
            print("Please answer with 'yes' or 'no'.")
    
    return task, priority, time_bound


def generate_reminder(task, priority, time_bound):
    print("\n--- Reminder ---")
    
    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task. Try to complete it as soon as possible.")
        
        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task that should be done today.")
            else:
                print(f"Reminder: '{task}' is a medium priority task. Plan to do it soon.")
        
        case "low":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a low priority task, but it still needs to be done today.")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        
        case _:
            print("Invalid priority. Please try again.")


# Main script logic
if __name__ == "__main__":
    task, priority, time_bound = get_task_info()
    generate_reminder(task, priority, time_bound)
