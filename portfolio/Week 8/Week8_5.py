import sys

def check_spelling(text_file, word_list_file):
    with open(word_list_file, 'r') as word_list:
        valid_words = set()
        for entry in word_list:
            valid_words.add(entry.strip().lower())  

    with open(text_file, 'r') as text:
        text_words = set()
        for line in text:
            # Split line into words and strip punctuation
            for word in line.split(): 
                cleaned_word = ''.join(e for e in word if e.isalnum())  
                text_words.add(cleaned_word.lower()) 

    invalid_words = text_words - valid_words

    if len(invalid_words) > 0:
        print("Words that are not available in the dictionary:")
        for word in invalid_words:
            print(word)
    else:
        print("Every word is found in the dictionary.")

def check():
    if len(sys.argv) != 3:
        print("Please enter the text file and word list file to check.")
    else:
        text_file_path = sys.argv[1]
        word_list_path = sys.argv[2]
        check_spelling(text_file_path, word_list_path)

check()
