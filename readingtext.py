# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from cgitb import text
from fileinput import filename


def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename) as f:
        file = f.read()
    return file

def count_words(read_file_content):
    text = read_file_content("./story.txt")
    
    # [assignment] Add your code here
    words = text.split()
    count = dict()

    for word in words:
        if word in count:
            count[word] = count[word] + 1
        else:
            count[word] = 1
    return count
print(read_file_content("./story.txt"))
print(count_words(read_file_content))
