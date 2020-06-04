import re


# (xxx) yyy-zzzz, yyy-zzzz, xxx-yyy-zzzz, etc.
# phone numbers with missing area code should presume 206
# phone numbers should be stored in xxx-yyy-zzzz format.

def is_valid_email(sequence):
  # re.search(r'([\w\.-]+)@([\w\.-]+)'
  pattern = r'([\w\.-]+)@([\w\.-]+)'
  if re.match(pattern, sequence):
    return True
  else: 
    return False

def is_valid_phone_number(sequence):
    # print(sequence)
    # Format (xxx) yyy-zzzz
    # Format xxx-yyy-zzzz
    pattern = r"Cookie"
    # pattern = r'{3}'
    if re.match(pattern, sequence):
      print("Match!")
    else: print("Not a match!")


def test():
    # \w - Lowercase w. Matches any single letter, digit or underscore.
    # \s - Lowercase s. Matches a single whitespace character like: space, newline, tab, return.
    # r => This is called a raw string literal. It changes how the string literal is interpreted. Such literals are stored as they appear.
    # \d - Lowercase d. Matches decimal digit 0-9.
    # ^ - Caret. Matches a pattern at the start of the string.
    # $ - Matches a pattern at the end of string.
    # re.search(r'Number: [0-6]', 'Number: 5').group()[a-zA-Z0-9] - Matches any letter from (a to z) or (A to Z) or (0 to 9). 
    # Characters that are not within a range can be matched by complementing the set. 
    # If the first character of the set is ^, all the characters that are not in the set will be matched.
    # + - Checks for one or more characters to its left.
    # * - Checks for zero or more characters to its left.
    # ? - Checks for exactly zero or one character to its left.
    pattern = r"Cookie"
    sequence = "Cookie"
    if re.match(pattern, sequence):
      print("Match!")
    else: print("Not a match!")

    # num = '(425) 996-21-46'
    num = "111-222-3333"
    # is_valid_phone_number(sequence)
    # sequence = 'iris_leal@hotmail.com'
    sequence = 'name.lastname@domain.net'
    is_valid_email(sequence)
    print(is_valid_email(""))



if __name__ == "__main__":
    test()
    print('So far, so good')