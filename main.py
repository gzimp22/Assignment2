"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    return round(annual_cost / SEMESTERS_PER_YEAR, 2)


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return round(annual_cost / MONTHS_PER_YEAR, 2)


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    semester = annual_cost / SEMESTERS_PER_YEAR
    return round(semester / CLASS_DAYS_PER_SEMESTER, 2)


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    semester = annual_cost / SEMESTERS_PER_YEAR
    return round(semester / credits, 2)


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    semester = annual_cost / SEMESTERS_PER_YEAR
    per_credit = semester / credits
    course_cost = per_credit * CS1430_CREDITS
    return round(course_cost / CS1430_MEETINGS_PER_SEMESTER, 2)


# ---- PROGRAM ----

def ask_positive_number(prompt, whole_number=False):
    """Keep asking until the user enters a number greater than zero."""
    while True:
        text = input(prompt).strip().replace("$", "").replace(",", "")
        try:
            value = int(text) if whole_number else float(text)
        except ValueError:
            print("Please enter a number.")
            continue
        if value <= 0:
            print("The number must be greater than zero.")
            continue
        return value

def main():
    annual_cost = ask_positive_number("Total cost for one year: $")
    credits = ask_positive_number("Credits this semester: ", whole_number=True)

    while True:
        print()
        print("=== College Cost Breakdown ===")
        print("1. Cost per semester")
        print("2. Cost per month")
        print("3. Cost per class day")
        print("4. Cost per credit")
        print("5. Cost per CS 1430 class period")
        print("6. Worth It? (hours of work to cover a class period)")
        print("Q. Quit")

        choice = input("Choose an option: ").strip().upper()

        if choice == "Q":
            break
        elif choice == "1":
            print(f"Each semester costs ${cost_per_semester(annual_cost):,.2f}.")
        elif choice == "2":
            print(f"Each month costs ${cost_per_month(annual_cost):,.2f}.")
        elif choice == "3":
            print(f"Each class day costs ${cost_per_day(annual_cost):,.2f}.")
        elif choice == "4":
            print(f"Each credit costs ${cost_per_credit(annual_cost, credits):,.2f}.")
        elif choice == "5":
            print(f"Each CS 1430 class period costs ${cost_per_class(annual_cost, credits):,.2f}.")
        elif choice == "6":
            wage = ask_positive_number("Your hourly wage: $")
            per_class = cost_per_class(annual_cost, credits)
            hours = per_class / wage
            print(f"One CS 1430 class period costs ${per_class:,.2f}.")
            print(f"At ${wage:,.2f} per hour, you work {hours:.2f} hours to pay for it.")
        else:
            print("Please choose 1 to 6, or Q to quit.")


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
