import random

BOTTOM_NUMBER = 1
TOP_NUMBER = 100

random_number = random.randrange(BOTTOM_NUMBER, TOP_NUMBER)

selection = TOP_NUMBER // 2
left = BOTTOM_NUMBER
right = TOP_NUMBER
while True:
    if random_number == selection:
        print("FOUND")
        break
    if random_number > selection:
        print("SMALLER")
        left = selection
    if random_number < selection:
        print("BIGGER")
        right = selection
    selection = (left + right) // 2