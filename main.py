import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)



from stats import num_words
from stats import char_count
from stats import sorted_dict

file_path = sys.argv[1]

def get_book_text(file_path):
    with open(file_path) as f:
        book_text = f.read()

    return book_text



def main():
    text = get_book_text(file_path)
    final_number = num_words(text)
    message = f"Found {final_number} total words"
    nums = char_count(text)
    new_nums = sorted_dict(nums)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(message)
    print("--------- Character Count -------")
    for k in new_nums:
        if k["char"].isalpha():
            print(f"{k['char']}: {k['num']}")

    print("============= END ===============")


main()



        
    


