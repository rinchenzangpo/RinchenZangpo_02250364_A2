
def linear_search(student_ids, target):
    comparisons = 0
    for index, sid in enumerate(student_ids):
        comparisons += 1
        if sid == target:
            return index + 1, comparisons
    return -1, comparisons


def binary_search(sorted_scores, target):
    left = 0
    right = len(sorted_scores) - 1
    comparisons = 0

    while left <= right:
        mid = (left + right) // 2
        comparisons += 1

        if sorted_scores[mid] == target:
            return mid + 1, comparisons
        elif target < sorted_scores[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1, comparisons


def main():
    student_ids = [
        1001, 1005, 1002, 1008, 1003, 1010, 1004, 1009, 1007, 1012,
        1015, 1006, 1011, 1013, 1014, 1016, 1017, 1018, 1019, 1020
    ]

    sorted_scores = [45, 52, 58, 63, 67, 72, 75, 78, 82, 85, 88,
                     90, 92, 95, 98, 100, 102, 104, 105, 110]

    while True:
        print("\n=== Searching Algorithms Menu ===")
        print("Select a search operation (1-3):")
        print("1. Linear Search - Find Student ID")
        print("2. Binary Search - Find Score")
        print("3. Exit program")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"\nSearching in the list: {student_ids}")
            try:
                target = int(input("Enter Student ID to search: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            position, comparisons = linear_search(student_ids, target)

            if position != -1:
                print(f"Result: Student ID {target} found at position {position} "
                      f"Comparisons made: {comparisons}")
            else:
                print(f"Result: Student ID {target} not found "
                      f"Comparisons made: {comparisons}")

        elif choice == "2":
            print(f"\nSorted scores: {sorted_scores}")
            try:
                target = int(input("Enter score to search: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            position, comparisons = binary_search(sorted_scores, target)

            if position != -1:
                print(f"Result: Score {target} found at position {position} "
                      f"Comparisons made: {comparisons}")
            else:
                print(f"Result: Score {target} not found "
                      f"Comparisons made: {comparisons}")

        elif choice == "3":
            print("Thank you for using the search program!")
            break

        else:
            print("Invalid choice! Please enter 1, 2, or 3.")
            continue

        again = input("\nWould you like to perform another search? (y/n): ").lower()
        if again != 'y':
            print("Thank you for using the search program!")
            break


# Run program
if __name__ == "__main__":
    main()
