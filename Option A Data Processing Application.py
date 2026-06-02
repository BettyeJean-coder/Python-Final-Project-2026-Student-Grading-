# Option A Data Processing Application
# CLASS ITPRG-158-MPLS-SP26
# YEAR 2026
# STUDENT: BETTYE J TAYLOR 
# PROFESSOR NICHELLE MANUEL
# TIME OF COMPLETION: 4/27/2026
# TIME SPENT: 1 HOUR AND 30 MINUTES
# PROGRAM DESCRIPTION: This program reads student names and scores from a file, calculates letter grades, and generates a report with average, highest, and lowest scores.
# PYTHON VERSION: 3.14


def get_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


def read_scores(filename):
    students = []

    try:
        file = open(filename, 'r')

        for line in file:
            parts = line.strip().split(',')

            name = parts[0]
            score = int(parts[1])

            students.append((name, score))

        file.close()

    except FileNotFoundError:
        print("Error: File not found.")
    except ValueError:
        print("Error: Invalid score format.")

    return students


def display_report(students):
    if len(students) == 0:
        print("No student data to display.")
        return

    total = 0
    highest = students[0]
    lowest = students[0]

    print("\nStudent Report:")
    print("-" * 30)

    for student in students:
        name = student[0]
        score = student[1]

        total += score

        if score > highest[1]:
            highest = student

        if score < lowest[1]:
            lowest = student

        grade = get_letter_grade(score)

        print(f"{name}: {score} ({grade})")

    average = total / len(students)

    print("\nSummary:")
    print("-" * 30)
    print(f"Average Score: {average:.2f}")
    print(f"Highest Score: {highest[0]} with {highest[1]}")
    print(f"Lowest Score: {lowest[0]} with {lowest[1]}")


def main():
    filename = "scores.txt"

    students = read_scores(filename)

    display_report(students)


if __name__ == "__main__":
    main()
