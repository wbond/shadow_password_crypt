import string
import random
import crypt
import getpass


salt = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(8))
password = None
confirm_password = None
while not password or not confirm_password or password != confirm_password:
    password = getpass.getpass('Password: ')
    confirm_password = getpass.getpass('Confirm: ')

hash = crypt.crypt(password, '$6$' + salt)
print(hash)
