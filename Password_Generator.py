import random
import string 
print("Welcome to password Generator")
def gen_pass(L=8):
    if L<4:
        print("password length must be at least 4")
        return None
    else:
        Lower = string.ascii_uppercase
        Upper = string.ascii_lowercase
        digits = string.digits
        symbol = string.punctuation
        password= [
            random.choice(Upper),
            random.choice(Lower),
            random.choice(digits),
            random.choice(symbol) ]
        all_chr=Lower+Upper+digits+symbol
        password+=random.choices(all_chr, k=L-4)
        random.shuffle(password)
        return ''.join(password)

len_=int(input("Enter the length of password\n"))

print(f"The password are ;{gen_pass(L=len_)}")