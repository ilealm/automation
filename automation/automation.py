import re


# (xxx) yyy-zzzz, yyy-zzzz, xxx-yyy-zzzz, etc.
# phone numbers with missing area code should presume 206
# phone numbers should be stored in xxx-yyy-zzzz format.

def read_file(path_file_to_read):
    try:
        with open(path_file_to_read,'r') as my_file:
                contents = my_file.read()
        return contents
    except:
        print('Error on reading the file.')

def get_valid_phone_numbers(content):
  # (\d{10})$)|(^(\d{6}-\d{4})$)|(^\d{3}[\s-]\d{3}[\s-]\d{4}$)|(^\d{3}[\s-]\d{7}$)|(^\(\d{3}\)\s?\d{3}[\s-]\d{4}
  # this is mine
  """
  Regex obtained from : # http://regexlib.com/Search.aspx?k=phone
    # pattern = r"^(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?$"
    pattern = r"(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?"
  """
  pattern = r'\b([A-Za-z0-9])*.?([A-Za-z0-9]+)@([A-Za-z0-9])*.((com)|(net)|(org))'
  return  re.findall(r'[\w\.-]+@[\w\.-]+', content)


def is_valid_email(sequence):
  # re.search(r'([\w\.-]+)@([\w\.-]+)'
  pattern = r'([\w\.-]+)@([\w\.-]+)'
  if re.match(pattern, sequence):
    return True
  else: 
    return False
  




def extract_information():
    email_list = []
    phones_list = []
    path_file_to_read = "assets/potential-contacts.txt"    
    
    # content = read_file(path_file_to_read)
    content_list = read_file(path_file_to_read).split()
    
    for word in content_list:
        print(word)
        if is_valid_email(word) : email_list.append(word)

    print(email_list)
    
    # emails = get_valid_emails(content)
    # print(emails)
    # print(emails[1])
    # print(emails[2])
    



if __name__ == "__main__":  
  extract_information()  
