import random
alphabets_Cap =['A','B','C','D','E','F','G','H',
                'I','J','K','L','M','N','O','P',
                'Q','R','S','T','U','V','W',
                'X','Y','Z']
alphabets_Small = ['a','b','c','d','e','f','g',
                   'h','i','j','k','l','m','n',
                   'o','p','q','r','s','t','u',
                   'v','w','x','y','z']
numbers = str(1234567890)
special_char = ['!','#','$','%','&','+','?']
cap_count = random.randint(2,5)
small_count = random.randint(2,5)
numbers_count = random.randint(2,5)
special_count = random.randint(2,5)

def generate_password():
    password_list = []
    my_password = ''
    for i in range(cap_count):
        password_list.append(random.choice(alphabets_Cap))
    for j in range(small_count):
        password_list.append(random.choice(alphabets_Small))
    for k in range(numbers_count):
        password_list.append(random.choice(numbers))
    for l in range(special_count):
        password_list.append(random.choice(special_char))
    random.shuffle(password_list)
    for item in password_list:
        my_password += item
    return my_password
