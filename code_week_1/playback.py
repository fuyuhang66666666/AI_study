"""
Some people have a habit of lecturing speaking rather quickly, and it’d be nice to slow them down, a la YouTube’s 0.75 playback speed,
 or even by having them pause between words.

In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that same input, 
replacing each space with ... (i.e., three periods).
"""


"""
str.replace(old, new, /, count=-1)
Return a copy of the string with all occurrences of substring old replaced by new. If count is given, 
only the first count occurrences are replaced. If count is not specified or -1, then all occurrences are replaced. For example:

Copy
'spam, spam, spam'.replace('spam', 'eggs')
'eggs, eggs, eggs'
'spam, spam, spam'.replace('spam', 'eggs', 1)
'eggs, spam, spam'
Changed in version 3.13: count is now supported as a keyword argument.
"""

def main():
    text = input("请输入你的文本：")
    print(replace_space(text))

def replace_space(text):
    return text.replace(" ", "...")

if __name__ == "__main__":
    main()
