from pprint import pprint
from function import get_contact

contacts = []

for i in range(3):
    contacts.append(get_contact())

pprint(contacts)



