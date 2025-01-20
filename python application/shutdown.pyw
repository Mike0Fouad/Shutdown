import os
import tkinter as tk
from PIL import Image, ImageTk
import csv
import json
import datetime
import sys

class Shutdown:
    def __init__(self, main_window):
        
        # Main window setup
        self.main_window = main_window
        self.main_window.title("Shutdown")
        self.main_window.geometry("330x500")
        self.main_window.resizable(False, False)
        self.main_window.config(bg="#333")
        
        if getattr(sys, 'frozen', False):
            app_path = sys._MEIPASS
        else:
            app_path = os.path.dirname(__file__)
        
        self.icon_path = os.path.join(app_path, 'assets', 'icon.ico')
        self.main_window.iconbitmap(self.icon_path)

        # Background picture
        self.background_path = os.path.join(app_path, 'assets', 'Wallpaper.png')
        self.background_image = Image.open(self.background_path)
        self.background = ImageTk.PhotoImage(self.background_image)
        
        # Canvas setup with background image
        self.canvas = tk.Canvas(self.main_window, width=self.background.width(), height=self.background.height(), highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.background, anchor="nw")

        ##################################################################
        
        # Top text (Title)
        self.canvas.create_text(165, 50, text="Enter Timer for Shutdown", font=("Times New Roman", 15,"bold"), fill="red")
        
        ##################################################################
        
        # Middle frame (time entry)
        self.create_frame(80, 120, 250, 180, radius=30, color="#333")
        self.entry_frame = tk.Frame(self.main_window, bg="#333")

        # Create the entry widgets
        self.hours = self.create_entry(self.entry_frame, "00")
        self.colon_label(135, 150) 
        self.minutes= self.create_entry(self.entry_frame, "00")
        self.colon_label(195, 150) 
        self.seconds = self.create_entry(self.entry_frame, "00")

        # Place the entry frame on the canvas
        self.canvas.create_window(165, 150, window=self.entry_frame)
        
        ##################################################################
        
        # Middle frame label (feedback to the user)
        self.message_label = self.canvas.create_text(165, 200, text="", font=("Times New Roman", 12,"bold"), fill="white")
        
        ##################################################################
        
        # Bottom frame content (Buttons)
        self.create_button(100, 300, "Shutdown", self.shutdown)
        self.create_button(165, 300, "Cancel", self.cancel)
        self.create_button(230, 300, "Close", self.main_window.quit)

    ##################################################################
    
    # Helper methods
    ## create a rounded rectangle frame using arc and rectangles
    def create_frame(self, x1, y1, x2, y2, radius, color):
        
        self.canvas.create_arc(x1, y1, x1 + radius * 2, y1 + radius * 2, start=90, extent=90, fill=color, outline="")
        self.canvas.create_arc(x2 - radius * 2, y1, x2, y1 + radius * 2, start=0, extent=90, fill=color, outline="")
        self.canvas.create_arc(x1, y2 - radius * 2, x1 + radius * 2, y2, start=180, extent=90, fill=color, outline="")
        self.canvas.create_arc(x2 - radius * 2, y2 - radius * 2, x2, y2, start=270, extent=90, fill=color, outline="")
        self.canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2, fill=color, outline="")
        self.canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, fill=color, outline="")
        
    ## create an entry widget
    def create_entry(self, frame, default_text):
        entry = tk.Entry(frame, width=2, bg="#333", fg="white", relief="flat", font=("Times New Roman", 20,"bold"))
        entry.insert(0, default_text)
        entry.pack(side="left", padx=5)
        return entry
    
    ## create a colon label to separate the hours, minutes, and seconds
    def colon_label(self, x, y):
        label = tk.Label(self.entry_frame, text=":", font=("Times New Roman", 20,"bold"), bg="#333", fg="red")
        label.pack(side="left")
        return label

    ## create a button widget
    def create_button(self, x, y, text, command):
        # Draw rounded rectangle
        self.create_frame(x - 50, y - 15, x + 40, y + 15, radius=10, color="#333")
        # Add the Button widget
        button = tk.Button(self.main_window, text=text, font=("Times New Roman", 10,"bold"), command=command, bg="#333", fg="red", relief="flat")
        # Bind the button to change color on hover
        button.bind("<Enter>", lambda e: button.config(bg="red", fg="white"))
        button.bind("<Leave>", lambda e: button.config(bg="#333", fg="red"))
        # Place the button on the canvas
        self.canvas.create_window(x, y, window=button)
        
    ##################################################################
      
        
    # Timer function (convert hours, minutes, and seconds to seconds)
    def timer(self):
        try:
            hours = int(self.hours.get()) if self.hours.get() else 0
            minutes = int(self.minutes.get()) if self.minutes.get() else 0
            seconds = int(self.seconds.get()) if self.seconds.get() else 0
            return hours * 3600 + minutes * 60 + seconds
        except:
            return False
    
    # Shutdown function
    def shutdown(self):
        time = self.timer() if self.timer() else 0
        message =""
        if time == 0:
            message = "Error: please ReEnter the wanted time"
        else:
            os.system("shutdown -a")
            os.system(f'shutdown -s -t {time}')
            message = f"Shutdown after {time//3600} hours {time%3600//60} minutes {time%60} seconds"
        
        self.canvas.itemconfig(self.message_label, text= message)
        self.log(f"{time//3600}:{time%3600//60}:{time%60}", "Shutdown")
        return message
    
    # Cancel shutdown function
    def cancel(self):
        message=""
        os.system("shutdown -a")
        self.canvas.itemconfig(self.message_label, text="Shutdown canceled!")
        self.log("-", "Cancel")
        return message
    
    
    
    
    # logging the shutdown and cancel
    
    def file(self):
        #check for direcotry and create it if not exist
        if not os.path.exists("C:\\ProgramData\\ShutdownTimer"):
            os.makedirs("C:\\ProgramData\\ShutdownTimer")
        #check for  csv file and create it if not exist
        if not os.path.exists("C:\\ProgramData\\ShutdownTimer\\log.csv"):
            with open("C:\\ProgramData\\ShutdownTimer\\log.csv", "w") as file:
                writer = csv.writer(file)
                writer.writerow(["Date", "Time", "Action"])
        #check for json file and create it if not exist
        if not os.path.exists("C:\\ProgramData\\ShutdownTimer\\count.json"):
            with open("C:\\ProgramData\\ShutdownTimer\\count.json", "w") as file:
                json.dump({"Shutdown":0,"Cancel":0}, file)
        return True
    
    def log_Count(self,message):
        temp_data = {"Shutdown":0,"Cancel":0}
        with open("C:\\ProgramData\\ShutdownTimer\\count.json", "r") as file:
            data = json.load(file)
            if message == "Shutdown":
                temp_data["Shutdown"] = data["Shutdown"] + 1
            elif message == "Cancel":
                temp_data["Cancel"] = data["Cancel"] + 1
        with open("C:\\ProgramData\\ShutdownTimer\\count.json", "w") as file:
            json.dump(temp_data, file)
        return True
    
    def log(self,time, message):
        #check for file
        self.file()
        # log message
        with open("C:\\ProgramData\\ShutdownTimer\\log.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([datetime.datetime.now(),time, message])
        # log count
        self.log_Count(message)
        return True
        
    
        
        
        
    
        
    
if __name__ == "__main__":
    root = tk.Tk()
    shutdown = Shutdown(main_window=root)
    root.mainloop()
    


