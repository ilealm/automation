import re

def read_file(path_file_to_read):
    try:
        with open(path_file_to_read,'r') as my_file:
                contents = my_file.read()
        return contents
    except:
        print('Error on reading the file.')

def is_valid_email(sequence):
  pattern = r'([\w\.-]+)@([\w\.-]+)'
  if re.match(pattern, sequence):
    return True
  else: 
    return False

    
def get_phones(content):
    """
    Regex: JB Tellez. I Updated "-" to [-.]
    """
    pattern = r'[2-9]\d{2}[-.]\d{3}[-.]\d{4}'  # THIS WORKS FOR ddd-ddd-dddd. UNITE THE LAST 2 !
    return  re.findall(pattern, content) 


def save_email_list(e_mail_list):
    path_to_save = 'emails.txt'

    with open(path_to_save, "w+") as f:
        for element in e_mail_list:
            f.write(element + '\n')

def save_phone_list(phones_list):
    path_to_save = 'phone_numbers.txt'

    with open(path_to_save, "w+") as f:
        for element in phones_list:
            f.write(element + '\n') 


def process_information():
    email_list = []
    phones_list = []
    path_file_to_read = "assets/potential-contacts.txt"    
    
    content = read_file(path_file_to_read)
    
    for word in content.split(): #content_list: 
        if is_valid_email(word) : email_list.append(word)
    
    phones_list = get_phones(content)
 
    email_list.sort()
    phones_list.sort()

    save_email_list(email_list)
    save_phone_list(phones_list)


if __name__ == "__main__":  
  process_information()  
