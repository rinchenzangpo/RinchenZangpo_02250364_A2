
def bubble_sort(names):
    n = len(names)
    sorted_list = names[:]  # copy original
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
    return sorted_list



def insertion_sort(scores):
    sorted_scores = scores[:]  # copy original
    for i in range(1, len(sorted_scores)):
        key = sorted_scores[i]
        j = i - 1
        while j >= 0 and key < sorted_scores[j]:
            sorted_scores[j + 1] = sorted_scores[j]
            j -= 1
        sorted_scores[j + 1] = key
    return sorted_scores


recursive_calls = 0

def quick_sort(prices):
    global recursive_calls
    recursive_calls += 1

    if len(prices) <= 1:
        return prices

    pivot = prices[len(prices) // 2]
    left = [x for x in prices if x < pivot]
    middle = [x for x in prices if x == pivot]
    right = [x for x in prices if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)



def main():
    student_names = [
        "Kado", "Bobchu", "Zamu", "Nado", "Lemo", "Chimi", "Deki",
        "Sonam", "Pema", "Jigme", "Tashi", "Karma", "Wangmo",
        "Tshering", "Dorji"
    ]

    test_scores = [
        78, 45, 92, 67, 88, 54, 73, 82, 91, 59,
        76, 85, 48, 93, 71, 89, 57, 80, 69, 62
    ]

    book_prices = [
        450, 230, 678, 125, 890, 320, 410, 150,
        275, 560, 690, 85, 305, 720, 510
    ]

    while True:
        print("\n=== Sorting Algorithms Menu ===")
        print("Select a sorting operation (1-4):")
        print("1. Bubble Sort - Sort Student Names")
        print("2. Insertion Sort - Sort Test Scores")
        print("3. Quick Sort - Sort Book Prices")
        print("4. Exit program")

        choice = input("Enter your choice: ")

     
        if choice == "1":
            print(f"\nOriginal names: {student_names}")
            print("Performing Bubble Sort...")
            sorted_names = bubble_sort(student_names)
            print(f"Sorted names: {sorted_names}")

      
      
        elif choice == "2":
            print(f"\nOriginal scores: {test_scores}")
            print("Performing Insertion Sort...")
            sorted_scores = insertion_sort(test_scores)
            print(f"Sorted scores: {sorted_scores}")

            # Display top 5
            print("\nTop 5 Scores:")
            top_five = sorted_scores[-5:]  # last 5 in ascending list
            top_five.reverse()  # highest to lowest
            for i, score in enumerate(top_five, start=1):
                print(f"{i}. {score}")

        
        elif choice == "3":
            global recursive_calls
            recursive_calls = 0  # reset counter

            print(f"\nOriginal prices: {book_prices}")
            print("Performing Quick Sort...")
            sorted_prices = quick_sort(book_prices)

            print(f"Sorted prices: {sorted_prices}")
            print(f"Recursive calls: {recursive_calls}")

       
        elif choice == "4":
            print("Thank you for using the sorting program!")
            break

        else:
            print("Invalid choice! Please select 1-4.")
            continue

        # Continue or exit
        again = input("\nWould you like to perform another sort? (y/n): ").lower()
        if again != "y":
            print("Thank you for using the sorting program!")
            break


# Run the program
if __name__ == "__main__":
    main()
