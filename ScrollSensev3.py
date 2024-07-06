import tkinter as tk
from tkinter import *
from src.helpers import set_background, clear_widgets, generate_random_activity, save_diary
from PIL import Image, ImageTk

# create the gui frame
root = tk.Tk()
root.title("ScrollSense")
# size the size of the frame
screen_width = 350
screen_height = 750

# so that you cant resize the screen
root.minsize(screen_width, screen_height)
root.maxsize(screen_width, screen_height)

# creating a startpage with Text and Input Boxes
def create_startpage(root):
    global username, instagram_time
    clear_widgets(root)
    intro_frame = tk.Frame(root, bg="white", bd=0)
    intro_frame.place(relwidth=1, relheight=1)

    image_file_path = 'images/ScrollSenseScreenshot1.jpg'
    set_background(intro_frame, image_file_path)

    intro_label = tk.Label(intro_frame, text="Welcome to the ScrollSense Prototype!\nPlease enter your name:",
                           bg="#ADCDCC", font=("Helvetica", 14))
    intro_label.place(relx=0.5, rely=0.5, anchor="center")

    name_entry = tk.Entry(intro_frame, font=("Helvetica", 12))
    name_entry.place(relx=0.5, rely=0.55, anchor="center")

    daily_time_label = tk.Label(intro_frame, text="Please tell me your daily time on Instagram\n(in Hours):",
                                bg="#ADCDCC", font=("Helvetica", 14))
    daily_time_label.place(relx=0.5, rely=0.6, anchor="center")

    daily_time_entry = tk.Entry(intro_frame, font=("Helvetica", 12))
    daily_time_entry.place(relx=0.5, rely=0.65, anchor="center")

    newpage_button = tk.Button(root, text="CLICK HERE TO GO TO THE NEXT PAGE", font=("Ubuntu", 14, "bold"),
                               command=lambda: fetch_and_move(name_entry, daily_time_entry, root))
    newpage_button.place(relx=0.5, rely=0.925, anchor="center")

# this function is to get and store the name variable
def fetch_and_move(name_entry, daily_time_entry, root):
    global username, instagram_time
    username = name_entry.get()
    instagram_time = daily_time_entry.get()
    create_mobilepage(root)

create_startpage(root)

# this is to create a page that resembles a mobile phone, there you "open instagram"
def create_mobilepage(root):

    clear_widgets(root)

    intro_frame = tk.Frame(root, bg="white", bd=0)
    intro_frame.place(relwidth=1, relheight=1)

    image_file_path = "images/ScrollSensev3Screenshot2.jpg"
    set_background(intro_frame, image_file_path)
    
    image = Image.open("images/InstagramLogo.png")
    image = image.resize((70, 70))
    image=ImageTk.PhotoImage(image)
    insta_button= tk.Button(root, image = image, command = lambda: create_loadingpage(root))
    insta_button.photo = image
    insta_button.place(relx= 0.5, rely= 0.53, anchor= "center")
    
    click_here_label = tk.Label(intro_frame, text="Open Instagram via clicking\non the App icon",
                                bg="#ECC7AD", font=("Helvetica", 14))
    click_here_label.place(relx=0.5, rely=0.2, anchor="center")

# the loading page is just a makeshift animation that i made by loading in another background after .3 seconds
def create_loadingpage(root):
    clear_widgets(root)

    intro_frame = tk.Frame(root, bg="white", bd=0)
    intro_frame.place(relwidth=1, relheight=1)
    intro_frame.after(300, lambda: create_loadingpage2(root))
    image_file_path = 'images/ScrollSenseLoading.jpg'
    set_background(intro_frame, image_file_path)
        
def create_loadingpage2(root):
    clear_widgets(root)

    intro_frame = tk.Frame(root, bg="white", bd=0)
    intro_frame.place(relwidth=1, relheight=1)
    intro_frame.after(300, lambda: create_loadingpage3(root))
    image_file_path = 'images/ScrollSenseLoading2.jpg'
    set_background(intro_frame, image_file_path)
    
def create_loadingpage3(root):
    clear_widgets(root)

    intro_frame = tk.Frame(root, bg="white", bd=0)
    intro_frame.place(relwidth=1, relheight=1)
    intro_frame.after(300, lambda: create_loadingpage4(root))
    image_file_path = 'images/ScrollSenseLoading3.jpg'
    set_background(intro_frame, image_file_path)
    
def create_loadingpage4(root):
    clear_widgets(root)

    intro_frame = tk.Frame(root, bg="white", bd=0)
    intro_frame.place(relwidth=1, relheight=1)
    intro_frame.after(300, lambda: create_decisionpage(root))
    image_file_path = 'images/ScrollSenseLoading4.jpg'
    set_background(intro_frame, image_file_path)
 
# on the decisionpage you get to decide whether you want to open instagram or not   
def create_decisionpage(root):
    clear_widgets(root)

    intro_frame = tk.Frame(root, bg="white", bd=0)
    intro_frame.place(relwidth=1, relheight=1)

    image_file_path = 'images/ScrollSensev3Screenshot3.jpg'

    set_background(intro_frame, image_file_path)
    
    yes_button = tk.Button(root, text="YES", font=("Helvetica", 14, "bold"), bg="GREEN",
                            command=lambda: create_doomscrolling1(root))
    yes_button.place(relx=0.268, rely=0.615, anchor="center")
    
    no_button = tk.Button(root, text="NO", font=("Helvetica", 14, "bold"), bg="RED",
                            command=lambda: create_diary_page(root))
    no_button.place(relx=0.732, rely=0.615, anchor="center")
    
    warning_label = tk.Label(intro_frame)
    generate_random_activity(warning_label, username, instagram_time)
    warning_label.place(relx=0.5, rely=0.33, anchor="center")
    
    generate_button = tk.Button(intro_frame, text="Generate Another Option", bg="#ADCDCC",
                                command=lambda: generate_random_activity(warning_label, username, instagram_time))
    generate_button.place(relx=0.5, rely=0.45, anchor="center")


# if you decide to open instagram you come to my Doomscrolling simulation, filled with a fine collection of memes :)
def create_doomscrolling1(root):
    clear_widgets(root) 
    
    intro_frame = tk.Frame(root, bg="white", bd=0)
    intro_frame.place(relwidth=1, relheight=1)
    img = Image.open(f'images/ssmeme1.JPG')
    img = img.resize((300, 350))
    img = ImageTk.PhotoImage(img)
    image_label = tk.Label(intro_frame, image= img)
    image_label.photo = img
    image_label.place(relx=0.5, rely=0.4, anchor="center")
    
    next_button = tk.Button(root, text="Next meme", font=("Helvetica", 14, "bold"),
                            command=lambda: create_doomscrolling2(root))
    next_button.place(relx=0.5, rely=0.9, anchor='center')
    
def create_doomscrolling2(root):
    clear_widgets(root) 
    
    intro_frame = tk.Frame(root, bg="white", bd=0)
    intro_frame.place(relwidth=1, relheight=1)
    img = Image.open(f'images/ssmeme2.JPG')
    img = img.resize((300, 350))
    img = ImageTk.PhotoImage(img)
    image_label = tk.Label(intro_frame, image= img)
    image_label.photo = img
    image_label.place(relx=0.5, rely=0.4, anchor="center")
    
    next_button = tk.Button(root, text="Next meme", font=("Helvetica", 14, "bold"),
                            command=lambda: create_doomscrolling3(root))
    next_button.place(relx=0.5, rely=0.9, anchor='center')
    
def create_doomscrolling3(root):
    clear_widgets(root) 
    
    intro_frame = tk.Frame(root, bg="white", bd=0)
    intro_frame.place(relwidth=1, relheight=1)
    img = Image.open(f'images/ssmeme3.JPG')
    img = img.resize((300, 350))
    img = ImageTk.PhotoImage(img)
    image_label = tk.Label(intro_frame, image= img)
    image_label.photo = img
    image_label.place(relx=0.5, rely=0.4, anchor="center")
    
    next_button = tk.Button(root, text="Next meme", font=("Helvetica", 14, "bold"),
                            command=lambda: create_doomscrolling4(root))
    next_button.place(relx=0.5, rely=0.9, anchor='center')
    

def create_doomscrolling4(root):
    clear_widgets(root) 
    
    intro_frame = tk.Frame(root, bg="white", bd=0)
    intro_frame.place(relwidth=1, relheight=1)
    img = Image.open(f'images/ssmeme4.JPG')
    img = img.resize((300, 350))
    img = ImageTk.PhotoImage(img)
    image_label = tk.Label(intro_frame, image= img)
    image_label.photo = img
    image_label.place(relx=0.5, rely=0.4, anchor="center")
    
    next_button = tk.Button(root, text="Next meme", font=("Helvetica", 14, "bold"),
                            command=lambda: create_doomscrolling_stopper(root))
    next_button.place(relx=0.5, rely=0.9, anchor='center')
  
# this doomscrolling stopper should show how my program interferes with you when youre endlessly scrolling
# if you decide that you want to continue scrolling it sends you to the first meme again  
def create_doomscrolling_stopper(root):
    clear_widgets(root) 
    
    intro_frame = tk.Frame(root, bg="white", bd=0)
    intro_frame.place(relwidth=1, relheight=1)
    img = Image.open(f'images/Doomscrollingstopper.JPG')
    img = img.resize((300, 350))
    img = ImageTk.PhotoImage(img)
    image_label = tk.Label(intro_frame, image= img)
    image_label.photo = img
    image_label.place(relx=0.5, rely=0.4, anchor="center")
    
    continue_button = tk.Button(root, text="continue", font=("Helvetica", 14, "bold"),
                            command=lambda: create_doomscrolling1(root))
    continue_button.place(relx=0.3, rely=0.9, anchor='center')    
    
    stop_button = tk.Button(root, text="stop", font=("Helvetica", 14, "bold"),
                            command=lambda: create_diary_page(root))
    stop_button.place(relx=0.6, rely=0.9, anchor='center')   
    
# the diary page is the page where you land if you decide against opening instagram or against doomscrolling
# here you can (as the name suggests) write a diary entry about why you closed the app
# the text file you write there will be locally saved with the title as the files name
# this has been created with the help of a DigiLab tutor, not on my own
def create_diary_page(root):
    clear_widgets(root)

    intro_frame = tk.Frame(root, bg="white", bd=0)
    intro_frame.place(relwidth=1, relheight=1)

    image_file_path = 'images/ScrollSenseDiary.jpg'
    set_background(intro_frame, image_file_path)

    title_entry = tk.Entry(intro_frame, font=("Helvetica", 12))
    title_entry.insert("end", "title: ")
    title_entry.place(relx=0.5, rely=0.5, anchor="center")
    
    diary_entry = tk.Text(intro_frame, width=30, height=10)
    diary_entry.insert("end", "enter text here: ")
    diary_entry.place(relx=0.5, rely=0.7, anchor="center")

    submit_button = tk.Button(root, text="SUBMIT", font=("Helvetica", 14, "bold"),
                              command=lambda: save_diary(title_entry.get(), diary_entry.get("1.0", "end-1c")))
    submit_button.place(relx=0.5, rely=0.85, anchor='center')
    
    previous_diaries_button = tk.Button(root, text="PREVIOUS DIARIES", font=("Helvetica", 14, "bold"),
                              command=lambda: create_previous_diary_page(root))
    previous_diaries_button.place(relx=0.5, rely=0.9, anchor='center')
    
 
# this is the page where your previous diaries should be shown, this hasnt been implemented. 
# i would have liked to do this, but it seemed to be very tricky to open a file on somebodys computer.
# so i just created a few little placeholders to show what it would look like. 
def create_previous_diary_page(root):
    clear_widgets(root)

    intro_frame = tk.Frame(root, bg="white", bd=0)
    intro_frame.place(relwidth=1, relheight=1)
    
    monday_button = tk.Button(root, text="Monday 25th, March", font=("Ubuntu", 14, "bold"),
                               command=lambda: create_monday_page(root))
    monday_button.place(relx=0.5, rely=0.4, anchor="center")
    
    tuesday_button = tk.Button(root, text="Tuesday 26th, March", font=("Ubuntu", 14, "bold"),
                               command=lambda: create_tuesday_page(root))
    tuesday_button.place(relx=0.5, rely=0.5, anchor="center")

    wednesday_button = tk.Button(root, text="Wednesday 27th, March", font=("Ubuntu", 14, "bold"),
                               command=lambda: create_wednesday_page(root))
    wednesday_button.place(relx=0.5, rely=0.6, anchor="center")
    
    
    back_to_diaries_button = tk.Button(root, text="back", font=("Helvetica", 14, "bold"),
                              command=lambda: create_diary_page(root))
    back_to_diaries_button.place(relx=0.5, rely=0.9, anchor='center')
    
    image_file_path = 'images/ScrollSensev3previousdiaries.jpg'
    set_background(intro_frame, image_file_path)
    
def create_monday_page(root):
    clear_widgets(root)

    intro_frame = tk.Frame(root, bg="white", bd=0)
    intro_frame.place(relwidth=1, relheight=1)
    
    image_file_path = 'images/ScrollSensev3previousdiaries.jpg'
    set_background(intro_frame, image_file_path)
    
    monday_title_label = tk.Label(intro_frame, text="Title: Monday 25th, March",
                           bg="#ADCDCC", font=("Helvetica", 20))
    monday_title_label.place(relx=0.5, rely=0.35, anchor="center")
    
    monday_text_label = tk.Label(intro_frame, text="Today, I made a conscious decision to not open\nInstagram.The app showed me an insightful message,\nreminding me that thetime I spend scrolling could have\nbeen used to almost watch the entire\nLord of the Rings franchise. It struck a chord\nwith me. Instead of mindlessly browsing, I decided\n to embark on an epic journey Through Middle-earth.\nThe richness of Tolkiens world captivated me far more\nThan endless reels and stories ever could.\nI felt a sense of accomplishment and fulfillment,\nknowing I spent my time on something meaningful\nand enriching.",
                           bg="#ADCDCC", font=("Helvetica", 14))
    monday_text_label.place(relx=0.5, rely=0.6, anchor="center")
    
    back_to_diaries_button = tk.Button(root, text="back", font=("Ubuntu", 14, "bold"),
                               command=lambda: create_previous_diary_page(root))
    back_to_diaries_button.place(relx=0.5, rely=0.9, anchor="center")
    
def create_tuesday_page(root):
    clear_widgets(root)

    intro_frame = tk.Frame(root, bg="white", bd=0)
    intro_frame.place(relwidth=1, relheight=1)
    
    image_file_path = 'images/ScrollSensev3previousdiaries.jpg'
    set_background(intro_frame, image_file_path)
    
    tuesday_title_label = tk.Label(intro_frame, text="Title: Tuesday 26th, March",
                           bg="#ADCDCC", font=("Helvetica", 20))
    tuesday_title_label.place(relx=0.5, rely=0.35, anchor="center")
    
    tuesday_text_label = tk.Label(intro_frame, text="This morning, I found myself doomscrolling again,\nlost in an endless cycle of negative\nnews and meaningless content.\nSuddenly, the doomscrolling stopper\npopped up, jolting me out of my trance. It made\nme realize how much of my precious time I was\nwasting. I took a deep breath and put my\nphone down. Instead of getting sucked into the\ndigital abyss, I decided to focus on something\nproductive and uplifting. I went for a walk,\nenjoyed nature, and even started a new book.\nThe day felt longer, fuller, and far more\nrewarding.",
                           bg="#ADCDCC", font=("Helvetica", 14))
    tuesday_text_label.place(relx=0.5, rely=0.6, anchor="center")
    
    back_to_diaries_button = tk.Button(root, text="back", font=("Ubuntu", 14, "bold"),
                               command=lambda: create_previous_diary_page(root))
    back_to_diaries_button.place(relx=0.5, rely=0.9, anchor="center")

def create_wednesday_page(root):
    clear_widgets(root)

    intro_frame = tk.Frame(root, bg="white", bd=0)
    intro_frame.place(relwidth=1, relheight=1)
    
    image_file_path = 'images/ScrollSensev3previousdiaries.jpg'
    set_background(intro_frame, image_file_path)
    
    wednesday_title_label = tk.Label(intro_frame, text="Title: Wednesday 27th, March",
                           bg="#ADCDCC", font=("Helvetica", 20))
    wednesday_title_label.place(relx=0.5, rely=0.35, anchor="center")
    
    wednesday_text_label = tk.Label(intro_frame, text="I almost fell into the\nold habit of opening Instagram\nwithout thinking. It was just a reflex,\nsomething I did automatically. But\ntoday, the app intervened with a gentle\nreminder. It made me pause and reconsider.\nI realized I didn’t actually need to check Instagram;\nit was just a mindless habit. I quit\nthe app before even opening it and chose to\ndo something more intentional. I spent the\nnext hour working on my hobbies and even\nhad a meaningful conversation with a friend.\nBreaking that automatic response felt empowering,\nand it reminded me to be more\nmindful of my actions.",
                           bg="#ADCDCC", font=("Helvetica", 14))
    wednesday_text_label.place(relx=0.5, rely=0.6, anchor="center")
    
    back_to_diaries_button = tk.Button(root, text="back", font=("Ubuntu", 14, "bold"),
                               command=lambda: create_previous_diary_page(root))
    back_to_diaries_button.place(relx=0.5, rely=0.9, anchor="center")


root.mainloop()
