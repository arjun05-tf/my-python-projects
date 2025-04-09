import string
special = list(string.punctuation)

def main():
    password = input("enter a password to check: ")
    
    if char_len(password):
        if upp_case(password):
            if low_case(password):
                if digit(password):
                    if spcl_char(password):
                        if no_space(password):
                            print(f"Your password is {password} and it's strong! Good job champ")
                        else:
                            print("no spaces allowed")
                    else:
                        print("atleast 1 special character required")
                else:
                    print("atleast 1 digit required")
            else:
                print("atleast 1 lower case character required")
        else:
            print("atleast 1 upper case character required")
    else:
        print("minimum length should be 8 characters")
        


    

def char_len(p):
    return len(p) >= 8

def upp_case(p):
    for i in p:
        if i.isupper():
            return True
    return False
    
def low_case(p):
    for i in p:
        if i.islower():
            return True 
    return False

def digit(p):
    for i in p:
        if i.isdigit():
            return True
    return False

def spcl_char(p):
    for i in p:
        if i in special:
            return True
    return False
    
def no_space(p):
    for i in p:
        if i == " ":
            return False
    return True


main()