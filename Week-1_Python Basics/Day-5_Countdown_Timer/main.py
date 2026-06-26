#Countdown Timer

import time

#Step 1: Get the countdown time from the user
countdown_time = int(input("Enter the countdown time in seconds: "))

#Step 2: Countdown using a while loop
print("\n--- Countdown Timer ---")
while countdown_time > 0:
    print(countdown_time)
    time.sleep(1)  # Wait for 1 second
    countdown_time -= 1  # Decrease the countdown time by 1

#Step 3: Print Final Message
print("Countdown Complete!")