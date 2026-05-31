"""
File: class_reviews.py
Name:
-------------------------------
At the beginning of the program, the user is asked to enter
a class name, either SC001 or SC101. The input should be
case-insensitive.

If the user enters "-1" as the class name, the program will
calculate and display the maximum, minimum, and average
values among all the collected inputs.
"""
def main():
    # SC001
    hasSC001 = False
    sc001Max = 0
    sc001Min = 0
    sc001Total = 0
    sc001Count = 0

    # SC101
    hasSC101 = False
    sc101Max = 0
    sc101Min = 0
    sc101Total = 0
    sc101Count = 0

    while True:
        classInput = input("Which class? ").lower()
        if classInput == "-1":
            if not hasSC001 and not hasSC101:
                return print("No class scores were entered")
            break
        elif classInput == "sc001":
            score = int(input("Score: "))

            hasSC001 = True
            sc001Max = max(sc001Max, score)
            sc001Min = max(sc001Min, score)
            sc001Total += score
            sc001Count += 1
        elif classInput == "sc101":
            score = int(input("Score: "))

            hasSC101 = True
            sc101Max = max(sc101Max, score)
            sc101Min = max(sc101Min, score)
            sc101Total += score
            sc101Count += 1

    printResult("001", hasSC001, sc001Total, sc001Count, sc001Max, sc001Min)
    printResult("101", hasSC101, sc101Total, sc101Count, sc101Max, sc101Min)


def printResult(className, hasClass, total, count, max, min):
    classFullName= f"SC{className}"
    print(f"========={classFullName}=========")
    if hasClass:
        average = total/count
        print(f"Max ({className}): ",max)
        print(f"Min ({className}): ",min)
        print(f"Avg ({className}): ",average)
    else:
        print(f"No score for {classFullName}")




# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
