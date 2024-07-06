from PIL import Image, ImageTk
import tkinter as tk
import random

def set_background(widget, image_file_path):
    """This function sets the background image for a given widget."""
    img = Image.open(image_file_path)
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(widget, image=photo)
    label.image = photo  # To prevent garbage collection
    label.place(x=0, y=0, relwidth=1, relheight=1)

def clear_widgets(root):
    """This function will destroy any widgets you created."""
    for i in root.winfo_children():
        i.destroy()

# Function to generate a random exercise from a predefined list
def generate_random_exercise():
    exercises = ["full-body workout", "yoga session", "cardio routine", "strength training"]
    return random.choice(exercises)

def calculate_duolingo_lessons(hours_spent):
    # Assuming it takes 30 minutes to complete a Duolingo lesson
    minutes_for_one_lesson = 30
    total_minutes = hours_spent * 60
    return int(total_minutes / minutes_for_one_lesson)

def calculate_walk_distance(hours_spent):
    # Calculating the distance one could have walked, assuming the average person walks 5 km per hour
    average_walking_speed = 5
    return hours_spent * average_walking_speed

def calculate_reading_pages(hours_spent):
    # Calculating the amount of pages assuming the average person reads 40 pages per hour
    pages_per_hour = 40
    return int(hours_spent * pages_per_hour)

def calculate_watch_percentage(hours_spent):
    # Calculating percentage of how much of the Lord of the Rings franchise you could have watched
    total_minutes = 600
    percentage_watched = (hours_spent * 60 / total_minutes) * 100
    return percentage_watched

# Choosing a random activity from above and calculating the value based on player input
# Outputting a text with the finished numbers
def generate_random_activity(label, username, time_spent_on_instagram):
    # Clear the label content before updating
    label["text"] = ""
    # Ensure time_spent_on_instagram is a float
    try:
        time_spent_on_instagram = float(time_spent_on_instagram)
    except ValueError:
        label["text"] = "Invalid input for Instagram time."
        return  # Exit the function if the conversion fails

    activity_choice = random.choice(["reading", "watching", "walking", "duolingo", "exercise"])

    if activity_choice == "reading":
        label["text"] = f"{username},\nyou have spent {time_spent_on_instagram:.2f} hours\n on Instagram today.\nIn this time, you could have read \n{calculate_reading_pages(time_spent_on_instagram)} pages of your favorite book!"
    elif activity_choice == "watching":
        label["text"] = f"{username},\nyou have spent {time_spent_on_instagram:.2f} hours\n on Instagram today.\nIn this time, you could have watched\n{calculate_watch_percentage(time_spent_on_instagram):.2f}% of the whole Lord of the Rings franchise!\n AND THAT TAKES FOREVER"
    elif activity_choice == "walking":
        label["text"] = f"{username},\nyou have spent {time_spent_on_instagram:.2f} hours\n on Instagram today.\nIn this time, you could have walked\n{calculate_walk_distance(time_spent_on_instagram):.2f} km and taken in the fresh air!"
    elif activity_choice == "duolingo":
        label["text"] = f"{username},\nyou have spent {time_spent_on_instagram:.2f} hours\n on Instagram today.\nIn this time, you could have completed\n{calculate_duolingo_lessons(time_spent_on_instagram)} Duolingo lessons\n and made progress toward learning a new language!"
    elif activity_choice == "exercise":
        label["text"] = f"{username},\nyou have spent {time_spent_on_instagram:.2f} hours\n on Instagram today.\nIn this time, you could have completed a\n{generate_random_exercise()} workout!"

 # helper to create diary text file
def save_diary(title, diary):
    print(title)
    print(diary)
    with open(f"ScrollSenseDiaries/{title}.txt","w") as f:
        f.write(f"{diary}")
        f.close()
