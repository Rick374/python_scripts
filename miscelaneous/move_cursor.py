import pyautogui
import time

pyautogui.FAILSAFE = False

class MouseMover:
    def __init__(self, move_amount=10, wait_time=5):
        self.move_amount = move_amount
        self.wait_time = wait_time
        self.screen_width, self.screen_height = pyautogui.size()

    def move_mouse(self):
        while True:
            # Get the current mouse position
            original_x, original_y = pyautogui.position()

            # Calculate the new position
            new_x = original_x + self.move_amount
            new_y = original_y + self.move_amount

            # Check if the new position is out of screen bounds
            if new_x >= self.screen_width:
                new_x = 0
            if new_y >= self.screen_height:
                new_y = 0

            # Move the mouse to the new position
            pyautogui.moveTo(new_x, new_y)

            # Click the mouse
            pyautogui.click()

            # Move the mouse back to the original position
            pyautogui.moveTo(original_x, original_y)

            # Wait for the specified time
            time.sleep(self.wait_time)

# Create a MouseMover object
mouse_mover = MouseMover()

# Start moving the mouse
mouse_mover.move_mouse()

