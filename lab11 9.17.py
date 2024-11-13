
contacts_input = input().split()  
search_name = input()

contact_list = {}

for contact in contacts_input:
    name, phone = contact.split(',') 
    contact_list[name] = phone

print(contact_list[search_name])