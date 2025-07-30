#4 rolling a dice and get random number between 1-6
import random
rand=random.randint(1,6)
print("the rolling dice value :",rand)

#5 generate random password
import string
character = list(string.ascii_letters + string.digits)
password = ''.join(random.choice(character) for _ in range(6))
print("Password is :", password)

#6 shuffle number randomly
import random
num=[1,2,3,4,5,6]
random.shuffle(num)
print(num)

