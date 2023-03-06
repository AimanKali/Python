contacts = [
    {"name":"John",
     "phone":["123456","678910"]
     },
    {"name":"Jane",
     "phone":["564321","564321"]
     },
    {"name":"Bob",
     "phone":["+1234","+1235","+1236"]
     },
    ]

def list(contactlist):
    result = f'{"Name":<15}{"Phone":>15}\n'
    for contact in contactlist:
        result += f'{contact["name"]:<15}{contact["phone"][0]:>15}\n'
    print(result)

def list_all(contact):
    result = f'{"Name":<15}{"Phone":>15}\n'
    result += f'{contact["name"]:<15}{",".join(contact["phone"]):>15}\n'
    print(result)

def list_numbers(list):
    index = 0
    for i in list:
        index += 1
        print(f'{index}.{i}')

def find(contact_name):
    for contact in contacts:
        if contact_name == contact['name']:
            return contact

def add(name, number):
    if find(name) ==None:
        contacts.append({"name":name, "phone":[number]})
    else:
        print("Already exist!!!")

def add_number(name,number):
    contact=find(name)
    if contact !=None:
        contact['phone'].append(number)
    else:
        print("Does not exist!!!")


def edit(contact_name):
    contact=find(contact_name)
    if contact == None:
        print("No such name in your contact list!")
    else:
        new_name=input("Please enter a new name: ")
        list_numbers(contact["phone"])
        selected_number = int(input("Please select a number to edit: "))
        new_number=input("Please enter a new phone number: ")
        contact['name']=new_name
        contact['phone'][selected_number-1]=new_number

def delete(name):
    contact = find(name)
    if contact != None:
        contacts.remove(contact)

def delete_number(name):
    contact = find(name)
    list_numbers(contact["phone"])
    selected_number = int(input("Please select a number to delete: "))
    del contact["phone"][selected_number-1]
    list_all(contact)

while True:
    user_choice=input(f'Choose one of the options:\n'
      f'[1] Contact List \n'
      f'[2] Find contact\n'
      f'[3] Add contact\n'
      f'[4] Edit contact\n'
      f'[5] Delete contact\n'
      f'[6] Add number to contact\n'
      f'[7] Delete number for contact\n'
      f'[0] Exit\n'
      f'Your choice: ')

    if user_choice == '1':
        list(contacts)

    elif user_choice == '2':
        find_name = input('Print contact for search: ')
        result = find(find_name)
        if result:
            list_all(result)
        else:
            print('Contact is not found!')

    elif user_choice == '3':
        contact_name = input("Input a new contact's name: ")
        contact_phone = input("Input a new contact's phone: ")
        add(contact_name,contact_phone)

    elif user_choice == '4':
        edit_name = input("Input the name to edit: ")
        edit(edit_name)


    elif user_choice == '5':
        delete_name = input("Insert name to delete from your contact list: ")
        if find(delete_name) == None:
            print(("Insert name from contact list"))
        else:
            checking_delete = input(f'Are you sure you want to delete {delete_name}?(Write Y if sure, N if not: )')
            if checking_delete == "Y":
                delete(delete_name)
            else:
                print("OK, not deleting")

    elif user_choice == '6':
        contact_name = input("Input contact's name: ")
        contact_phone = input("Input a new contact's phone: ")
        add_number(contact_name, contact_phone)

    elif user_choice == '7':
        delete_name = input("Insert name to delete from your contact list: ")
        if find(delete_name) == None:
            print(("Insert name from contact list"))
        else:
            delete_number(delete_name)

    elif user_choice == '0':
        exit()

    else:
        print("Please, choose one of the option from the list.")





