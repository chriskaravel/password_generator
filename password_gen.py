import string
import random

def password_gen(size, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for x in range(size))

print(password_gen(int(input('How many characters do you want in your password?'))))
