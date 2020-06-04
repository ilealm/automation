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

def is_valid_phone_number(sequence):
  # (\d{10})$)|(^(\d{6}-\d{4})$)|(^\d{3}[\s-]\d{3}[\s-]\d{4}$)|(^\d{3}[\s-]\d{7}$)|(^\(\d{3}\)\s?\d{3}[\s-]\d{4}
  # this is mine
  """
  Regex obtained from : # http://regexlib.com/Search.aspx?k=phone
    
  """
  pattern = r'\b([A-Za-z0-9])*.?([A-Za-z0-9]+)@([A-Za-z0-9])*.((com)|(net)|(org))'
  if re.match(pattern, sequence):
    return True
  else: 
    return False


def is_valid_email(sequence):
  pattern = r'([\w\.-]+)@([\w\.-]+)'
  if re.match(pattern, sequence):
    return True
  else: 
    return False



def extract_information():
    email_list = []
    phones_list = []
    path_file_to_read = "assets/potential-contacts.txt"    
    
    content = read_file(path_file_to_read)
    # content_list = read_file(path_file_to_read).split()
    content_list = content.split()
    
    for word in content_list:
        # print(word)
        if is_valid_email(word) : email_list.append(word)
    
    get_phones(content)
        # if is_valid_phone_number(word) :  
        #   pass
            # TODO: remove trash
            # phones_list.append(word)
            # print(word)

    # print(email_list)
    # print()
    
    
def get_phones(content):
    # pattern = r'\d{3}\.\d{3}.\d{4}'  # working !!!, but the other get more this gets the ones with .
    # pattern = r'[2-9]\d{2}-\d{3}-\d{4}'  # THIS WORKS FOR ddd-ddd-dddd. bur the other get more this gets the ones with ..
    pattern = r'[2-9]\d{2}[-.]\d{3}[-.]\d{4}'  # THIS WORKS FOR ddd-ddd-dddd. UNITE THE LAST 2 !
    
    
    
    results = re.findall(pattern, content) 
    print(results)


if __name__ == "__main__":  
  extract_information()  
