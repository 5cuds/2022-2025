import pyautogui
import time

# Function to get RGB value under the mouse cursor
def get_rgb_at_mouse():
    # Get the current mouse position
    x, y = pyautogui.position()
    # Get the RGB value of the pixel at that position
    rgb = pyautogui.screenshot().getpixel((x, y))
    return x, y, rgb

# Loop to continuously display RGB values
try:
    while True:
        x, y, rgb = get_rgb_at_mouse()
        print(f"Mouse Position: ({x}, {y}), RGB: {rgb}")
        time.sleep(0.5)  # Delay to prevent spamming the output
except KeyboardInterrupt:
    print("Stopped.")
