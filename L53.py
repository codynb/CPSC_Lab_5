#theauthorsaremaggiedunnandcodybrownL53
number = int(input("pick a number to test if it is perfect \n"))

def test_perfect(number):
    x = 0
    for y in range(1,number):
        if number % y == 0:
            x = x + y
    if x == number:
        print("True")
    else:
        print("False")

test_perfect(number)
