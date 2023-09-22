import time

scale = 10
print("Starting ", end="")
for i in range(scale):
    print(".", end="")
    time.sleep(1)
print("\rStarting ... Done!")
