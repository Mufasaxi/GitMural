from datetime import date
from letter_map import LETTER_MAP

output = "output.txt"

def get_user_input():
    string = input("Enter the string to print on GitHub contribution graph: ").strip()
    start_date = input("Enter the start date (YYYY-MM-DD) or leave empty for today: ").strip()
    if not start_date:
        start_date = str(date.today())
    return string, start_date


def print_to_file(filename: str, string: str):
    hash_string = create_string_bitmap(string)
    with open(filename, "w") as output_file:
        for row in hash_string:
            output_file.write(row + "\n")


def create_string_bitmap(string: str):
    ROWS = 7
    hash_string = ["" for _ in range(ROWS)]

    for row in range(ROWS):
        for i, letter in enumerate(string):
            hash_string[row] += LETTER_MAP[letter.upper()][row]
            if i < len(string) - 1:
                hash_string[row] += " "
    return hash_string


def create_commits(bitmap, start_date):
    for week in range(len(bitmap[0])):
        for day in range(len(bitmap)):
            if bitmap[day][week] == "#":
                # Replace with actual commit code later
                print(f"commit on day:{day} week:{week}")


if __name__ == "__main__":
    string, start_date = get_user_input()
    print(f"\nCreating bitmap for string '{string}'")
    bitmap = create_string_bitmap(string)

    print("\nBitmap preview:")
    for row in bitmap:
        print(row)

    # Print AND save to file
    print_to_file("output.txt", string)
    print("\nBitmap saved to output.txt")

    print(f"\nStart date is {start_date}")
    create_commits(bitmap, start_date)
