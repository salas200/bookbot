from stats import num_words
from stats import char_count

def get_book_text(file_path):
    with open(file_path) as f:
        book_text = f.read()

    return book_text



def main():
    text = get_book_text("books/frankenstein.txt")
    final_number = num_words(text)
    message = f"{final_number} words found in the document"
    nums = char_count(text)
    print(message)
    print(nums)

main()



        
    


