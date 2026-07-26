import tkinter as tk
from plyer import notification

# Function to handle button click and show notification
def send_notification():
    user_input = entry.get()  # Get text from the entry box
    if user_input:
        # Create a notification with the user's input
        notification.notify(
            title="Notification Sent!",
            message=f"You entered: '{user_input}'",
            app_name="Input Notifier",
            app_icon="path_to_your_icon.ico",  # Optional: path to an icon file
            timeout=10
        )
        print(f"User entered: {user_input}") # For console debug
        root.destroy()  # Close the pop-up window
    else:
        # Inform the user to enter something
        notification.notify(
            title="No Input",
            message="Please enter some text before clicking.",
            app_name="Input Notifier",
            timeout=5
        )

# Create the main window
root = tk.Tk()
root.title("Entry Box Notification")
root.geometry("300x150")

# Create a label
label = tk.Label(root, text="Enter something to notify:")
label.pack(pady=10)

# Create an entry box
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Create a button that triggers the notification
button = tk.Button(root, text="Send Notification", command=send_notification)
button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
