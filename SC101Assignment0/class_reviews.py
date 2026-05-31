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
    has_sc001 = False
    sc001_max = 0
    sc001_min = 0
    sc001_total = 0
    sc001_count = 0

    # SC101
    has_sc101 = False
    sc101_max = 0
    sc101_min = 0
    sc101_total = 0
    sc101_count = 0

    while True:
        class_input = input("Which class? ").lower()
        if class_input == "-1":
            if not has_sc001 and not has_sc101:
                print("No class scores were entered")
                return
            break
        elif class_input == "sc001":
            score = int(input("Score: "))

            has_sc001 = True
            sc001_max = max(sc001_max, score)
            sc001_min = max(sc001_min, score)
            sc001_total += score
            sc001_count += 1
        elif class_input == "sc101":
            score = int(input("Score: "))

            has_sc101 = True
            sc101_max = max(sc101_max, score)
            sc101_min = max(sc101_min, score)
            sc101_total += score
            sc101_count += 1

    print_result("001", has_sc001, sc001_total, sc001_count, sc001_max, sc001_min)
    print_result("101", has_sc101, sc101_total, sc101_count, sc101_max, sc101_min)


def print_result(class_name, has_class, total, count, max_score, min_score):
    class_full_name = f"SC{class_name}"
    print(f"========={class_full_name}=========")
    if has_class:
        average = total/count
        print(f"Max ({class_name}): ",max_score)
        print(f"Min ({class_name}): ",min_score)
        print(f"Avg ({class_name}): ",average)
    else:
        print(f"No score for {class_full_name}")




# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
