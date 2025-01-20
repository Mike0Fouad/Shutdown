# Shutdown Timer Application

A Python-based desktop application that allows users to set a timer for automatically shutting down their system. The application features a user-friendly graphical interface built with Tkinter, system command integration for shutting down or canceling the shutdown, and logging functionality.

## Features

- **Set a timer** for system shutdown.
- **Cancel scheduled shutdown**.
- **User-friendly GUI** with a modern design.
- **Logging** of shutdown and cancel events (stored in CSV and JSON files).
- **Background image** and custom fonts for a polished look.

## Technologies Used

- **Python** (Main programming language)
- **Tkinter** (For GUI development)
- **PIL** (For handling images)
- **OS module** (For system commands)
- **CSV/JSON** (For logging and data persistence)

## Installation

### Prerequisites

Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Steps to Run the Application

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/Shutdown-Timer.git
   cd Shutdown-Timer
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
3. **Running the Application**:
   for .pyw file
   ```bash
   pythonw shutdown.pyw

## Running on other platforms

  The `.exe` file only runs on Windows. you can Run the `.pyw` file on macOS and Linux

# Usage

- Enter the desired time for shutdown in hours, minutes, and seconds.
- Click the "Shutdown" button to schedule the shutdown.
- Click "Cancel" to cancel any scheduled shutdown.
- The application will display a message showing the status of the shutdown or cancellation.
- Logging: Every shutdown and cancel action is logged in log.csv and a count is maintained in count.json.

# Screenshots
![image](https://github.com/user-attachments/assets/45e2819d-87fb-44c2-b93c-4ce8ef276951)
![image](https://github.com/user-attachments/assets/576a7dca-728f-40fc-931f-1ade1125211c)
![image](https://github.com/user-attachments/assets/0afb9c7c-797c-4f34-8e54-e4685da09dad)
![image](https://github.com/user-attachments/assets/18285651-be9a-4d8a-9d82-044d9c5988dc)

# Acknowledgments
- Thanks to the [Tkinter](https://wiki.python.org/moin/TkInter) library for GUI development.
- Thanks to [Pillow](https://pillow.readthedocs.io/en/stable/) for handling images in Python.
   
