import os
from tkinter import *
from ttkthemes import *
import csv
import json
import datetime

class Shutdown:
    def __init__(self, main_window):
        # Main window setup
        self.main_window = main_window
        self.main_window.title("Shutdown")
        self.main_window.geometry("800x500")
        self.main_window.resizable(False, False)
        self.main_window.config(bg="#333")
        
        self.main_window.set_theme("alt")


        # Frames
        self.top_frame = Frame(self.main_window, bg="#333")
        self.middle_frame = Frame(self.main_window, bg="#444")
        self.middle_frame_label = Frame(self.main_window, bg="#333")
        self.bottom_frame = Frame(self.main_window, bg="#333")
        
        ##################################################################
        ## label for timer
        # Top frame
        self.label = Label(self.top_frame, text="Enter Timer for shutdown", font=("Arial", 20), bg="#333",fg="white")
        #packing
        self.label.pack()
        
        ##################################################################
        ## containes the timer entries: hours, minutes, seconds
        # Middle frame
        self.hours = Entry(self.middle_frame, width=5, bg="#444", fg="white", relief="flat",font=("Arial", 20))
        self.dots = Label(self.middle_frame, text=":", font=("Arial", 20), bg="#444", fg="white")
        self.mins = Entry(self.middle_frame, width=5, bg="#444", fg="white", relief="flat",font=("Arial", 20))
        self.dots2 = Label(self.middle_frame, text=":", font=("Arial", 20), bg="#444", fg="white")
        self.secs = Entry(self.middle_frame, width=5, bg="#444", fg="white", relief="flat",font=("Arial", 20))
        # Insert default text into entries
        self.hours.insert(0, "00")
        self.mins.insert(0, "00")
        self.secs.insert(0, "00")
        #packing
        self.hours.pack(padx=10,side="left")
        self.dots.pack(ipadx=5,side="left")
        self.mins.pack(ipadx=5,side="left")
        self.dots2.pack(ipadx=5,side="left")
        self.secs.pack(ipadx=5,side="left")

        
        ##################################################################
        ## label for message
        #middle frame for label
        self.message_label = Label(self.middle_frame_label, text="", bg="#333", fg="white")
        #packing
        self.message_label.pack(side="left")

        ##################################################################
        ## containes the buttons: shutdown, cancel, close
        # Bottom frame
        self.shutdown_button = Button(self.bottom_frame, text="Shutdown", font=("Arial", 20), command=self.shutdown, bg="#444", fg="white" ,relief="flat")
        self.cancel_button = Button(self.bottom_frame, text="Cancel", font=("Arial", 20), command=self.Cancel, bg="#444", fg="white", relief="flat")
        self.close_button = Button(self.bottom_frame, text="Close", font=("Arial", 20), command=self.main_window.quit, bg="#444", fg="white", relief="flat")
        # packing
        self.shutdown_button.pack(side="left", padx=10)
        self.cancel_button.pack(side="left", padx=10)
        self.close_button.pack( side="left", padx=10)
        
        ##################################################################
        
        # Pack the frames
        self.top_frame.pack( padx=50, pady=30)
        self.middle_frame.pack(ipadx=10,ipady=10, padx=50, pady=30)
        self.middle_frame_label.pack(ipadx=10,ipady=10, padx=50, pady=20)
        self.bottom_frame.pack(padx=50, pady=10)
        
        
      
        
    # Timer function
    def timer(self):
        try:
            hours = int(self.hours.get()) if self.hours.get() else 0
            minutes = int(self.mins.get()) if self.mins.get() else 0
            seconds = int(self.secs.get()) if self.secs.get() else 0
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
        self.message_label.config(text=message)
        self.log(f"{time//3600}:{time%3600//60}:{time%60}", "Shutdown")
        return message
    
    # Cancel shutdown function
    def Cancel(self):
        message=""
        os.system("shutdown -a")
        self.message_label.config(text="Shutdown canceled")
        self.log("-", "Cancel")
        return message
    
    
    
    
    # logging the shutdown and cancel
    
    def file(self):
        #check for direcotry and create it if not exist
        if not os.path.exists(r"C:\ProgramData\ShutdownTimer"):
            os.makedirs(r"C:\ProgramData\ShutdownTimer")
        #check for  csv file and create it if not exist
        if not os.path.exists("C:\ProgramData\ShutdownTimer\log.csv"):
            with open(r"C:\ProgramData\ShutdownTimer\log.csv", "w") as file:
                writer = csv.writer(file)
                writer.writerow(["Date", "Time", "Action"])
        #check for json file and create it if not exist
        if not os.path.exists(r"C:\ProgramData\ShutdownTimer\count.json"):
            with open(r"C:\ProgramData\ShutdownTimer\count.json", "w") as file:
                json.dump({"Shutdown":0,"Cancel":0}, file)
        return True
    
    def log_Count(self,message):
        temp_data = {"Shutdown":0,"Cancel":0}
        with open(r"C:\ProgramData\ShutdownTimer\count.json", "r") as file:
            data = json.load(file)
            if message == "Shutdown":
                temp_data["Shutdown"] = data["Shutdown"] + 1
            elif message == "Cancel":
                temp_data["Cancel"] = data["Cancel"] + 1
        with open(r"C:\ProgramData\ShutdownTimer\count.json", "w") as file:
            json.dump(temp_data, file)
        return True
    
    def log(self,time, message):
        #check for file
        self.file()
        # log message
        with open("C:\ProgramData\ShutdownTimer\log.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([datetime.datetime.now(),time, message])
        # log count
        self.log_Count(message)
        return True
        
    
        
        
        
    
        
    
if __name__ == "__main__":
    root = ThemedTk()
    shutdown = Shutdown(main_window=root)
    root.mainloop()

