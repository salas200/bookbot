from stats import num_words
from stats import char_count
from stats import sorted_dict

file_path = "books/frankenstein.txt"
def get_book_text(file_path):
    with open(file_path) as f:
        book_text = f.read()

    return book_text



def main():
    text = get_book_text(file_path)
    final_number = num_words(text)
    message = f"{final_number} words found in the document"
    nums = char_count(text)
    new_nums = sorted_dict(nums)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(message)
    print("--------- Character Count -------")
    for k, v in new_nums

main()



        
    


