import argparse
from letter_map import LETTER_MAP

output = "output.txt"

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--string", help="string to print on github contribution graph")
    args = parser.parse_args()
    return args


def print_to_file(filename:str, string:str):
    hash_string = create_string_bitmap(string)
    with open(filename, "w") as output_file:
        for row in hash_string:
            output_file.write(row+"\n")


def create_string_bitmap(string:str):
    ROWS = 7
    hash_string = ["" for _ in  range(ROWS)]

    for  row in range(ROWS):
        for i, letter in enumerate(string):
            hash_string[row] += LETTER_MAP[letter.upper()][row]
            if i < len(string) - 1:
                hash_string[row] += " "
    return hash_string




if __name__ == "__main__":
    args = get_args()
    print(f"creating bitmap for string '{args.string}'")
    bitmap = create_string_bitmap(args.string)
    print("\nBitmap preview:")
    for row in bitmap:
        print(row)
    
    # Save to file
    print_to_file("output.txt", args.string)
    print(f"\nBitmap saved to output.txt")


