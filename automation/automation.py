import re


# (xxx) yyy-zzzz, yyy-zzzz, xxx-yyy-zzzz, etc.
# phone numbers with missing area code should presume 206
# phone numbers should be stored in xxx-yyy-zzzz format.

def is_valid_email(sequence):
  # https://www.datacamp.com/community/tutorials/python-regular-expression-tutorial
  pattern = r'([\w\.-]+)@([\w\.-]+)'
  if re.match(pattern, sequence):
    return True
  else: 
    return False

def is_valid_phone_number(sequence):
    # http://regexlib.com/Search.aspx?k=phone
    # pattern = r"^(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?$"
    pattern = r"(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?"
  
    if re.match(pattern, sequence):
        return True
    else:
        return False


def read_file(path_file_to_read):
    try:
        with open(path_file_to_read,'r') as my_file:
                contents = my_file.read()
        return contents
    except:
        print('Error on reading the file.')

def extract_information():
    # read the fil
    path_file_to_read = "assets/potential-contacts.txt"    
    # put everyword in a list
    # content_list = read_file(path_file_to_read).split()
    content = read_file(path_file_to_read)
    # print(content_list[0:300])
    # return
    # Analyce each word, if is email or phone number, add to set or list
    # for word in content_list:
    #     print(word)
    #     if is_valid_email(word):
    #         print('email: ', word)
    #     if is_valid_phone_number(word):
    #         print('phone: ', word)

    # at the end, sort the lists
    # store the info on a file
    

    #'addresses' is a list that stores all the possible match
    addresses = re.findall(r'[\w\.-]+@[\w\.-]+', content)
    for address in addresses: 
        print(address)
    



if __name__ == "__main__":  
  extract_information()  
  # num ="'wrong.092-32-8829She'"
    # num ='(425)996-2146'
  # print( is_valid_phone_number(num))
    # num ='425-996-2146'
    # print( is_valid_phone_number(num))
    # num ='958-967-1821x12205'
    # print( is_valid_phone_number(num))
    # num ='425996-2146'
    # print( is_valid_phone_number(num))
    # num ='001-746-186-9687x72605'
    # print( is_valid_phone_number(num))
    # num ='+1-776-470-3636x20415'
    # print( is_valid_phone_number(num))
    # num ='368-358-0083'
    # print( is_valid_phone_number(num))
    # num ='+1-701-212-0428x18995'
    # print( is_valid_phone_number(num))
    # num ='001-746-186-9687x72605'  
    # print( is_valid_phone_number(num))

    # mail ="hernandezaudrey@hotmail.com"
    # print(is_valid_email(mail))
    # mail ="jellison@campbell.com"
    # print(is_valid_email(mail))
    # mail ="hsampson@gibson-jackson.com"
    # print(is_valid_email(mail))
    # mail ="mary90@yahoo.com"
    # print(is_valid_email(mail))
    # mail ="robertsonkristina@cole-cannon.org"
    # print(is_valid_email(mail))
    # mail ="dking@mcdonald-adams.com"
    # print(is_valid_email(mail))
    