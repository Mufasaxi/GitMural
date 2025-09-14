import os
import subprocess
from datetime import datetime, timedelta
from letter_map import LETTER_MAP

output = "output.txt"

def get_user_input():
    string = input("Enter the string to print on GitHub contribution graph: ").strip()
    start_date = input("Enter the start date (YYYY-MM-DD) or leave empty for today: ").strip()
    intensity = int(input("Enter intensity (commits per day): "))
    if not start_date:
        start_date = str(date.today())
    return string, start_date, intensity


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


def create_commits(bitmap, start_date, intensity):
    start = datetime.strptime(start_date, "%Y-%m-%d")

    for week in range(len(bitmap[0])):
        for day in range(len(bitmap)):
            if bitmap[day][week] == "#":
                commit_date = start + timedelta(days=week*7+day)
                commit_date_str = commit_date.strftime("%Y-%m-%d 12:00:00")

                # Change a file to have something to commit
                placeholder_file = "placeHolder.txt"
                with open(placeholder_file, "a") as file:
                    file.write(f"{commit_date_str} ")

                env = os.environ.copy()
                env["GIT_AUTHOR_DATE"] = commit_date_str
                env["GIT_COMMITTER_DATE"] = commit_date_str

                for _ in range(intensity):
                    subprocess.run(["git", "add", placeholder_file], check=True)
                    subprocess.run  (
                        ["git", "commit", "--allow-empty", "-m", f"Commit for {commit_date_str}"],
                        check=  True,
                        env=env
                    )

    print("Created all commits")


if __name__ == "__main__":
    string, start_date, intensity = get_user_input()
    print(f"\nCreating bitmap for string '{string}'")
    bitmap = create_string_bitmap(string)

    print("\nBitmap preview:")
    for row in bitmap:
        print(row)

    # Print AND save to file
    print_to_file("output.txt", string)
    print("\nBitmap saved to output.txt")

    print(f"\nStart date is {start_date}")
    create_commits(bitmap, start_date, intensity)
