import string
import random
if __name__=="__main__":
    s1 = string.ascii_lowercase
   # print(s1)
    s2 = string.ascii_uppercase
   # print(s2)
    s3 = string.digits
    #print(s3)
    s4 = string.punctuation
    #print(s4)
while True:
    try:
        plen = int(input("Enter password length: "))
        s= []
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))
        # print(s)
        random.shuffle(s)
        #print(s)
        print("Your Password is: ")
        print("".join(s[0:plen]))

    except:
        print("Invalid Input. Please enter a valid integer for the password length.")
        
    
   
