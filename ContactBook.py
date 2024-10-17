class Contact:

    def __init__(self,name,phonenum,email,address):
        self.name=name
        self.phonenum=phonenum
        self.email=email
        self.address=address


    def __str__(self):
        return f"Name:{self.name},phonenum:{self.phonenum},email:{self.email},address:{self.address}"


class ContactBook:

    def __init__(self):
        self.contacts = []

    def displaymenulist(self):
        print("Contact menu List")
        print("1. Add new Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit\n")

    def addnewcontact(self):
        name=input("Enter Name")
        phonenum=input("Enter Phone Number")
        email=input("Enter Email Id")
        address=input("Enter Address")
        contact=Contact(name,phonenum,email,address)
        self.contacts.append(contact)
        print("New Contact added successfully !!!!")


    def viewcontactlist(self):

        if len(self.contacts) == 0:
            print("No Contacts available.\n")
        else:
            index=1
            for contact in self.contacts:
                print(f"{index}. Name: {contact.name}, Phone: {contact.phonenum}, Email: {contact.email}, Address: {contact.address}")
                index += 1
                print()



    def searchcontact(self):
        search=input("Enter phone number or name to search :")
        found=False
        for contact in self.contacts :
            if search.lower() == contact.phonenum or search.lower() == contact.name :
                print(contact)
                found = True

        if not found :
            print("No Contact Found !!.\n")
        else :
            print()


    def updatecontact(self):
        update=input("Enter name or phone number to update :")
        for contact in self.contacts :
            if update.lower() == contact.phonenum or update.lower() == contact.name :
                print("contact Found !")
                print(contact)
                contact.name=input("Enter new name :")
                contact.phonenum=input("Enter new Phone Number :")
                contact.email=input("Enter new email :")
                contact.address=input("Enter new Address :")
                print("Updated Successfully  !!!")
                return
        print("No Contact Found \n")


    def deletecontact(self):
        delete=input("Enter Phone Number or name to delete :")
        for contact in self.contacts :
            if delete.lower() == contact.phonenum or delete.lower() == contact.name :
                self.contacts.remove(contact)
                print("Deleted Succesfully !!!!")
                return

        print("No records Found !\n")







def main():
    contactbook=ContactBook()

    while True :
        contactbook.displaymenulist()
        choice=input("Enter Your Choice :")

        if choice == '1':
           contactbook.addnewcontact()
        elif choice == '2':
            contactbook.viewcontactlist()
        elif choice == '3':
            contactbook.searchcontact()
        elif choice == '4':
            contactbook.updatecontact()
        elif choice == '5':
            contactbook.deletecontact()
        elif choice == '6':
            print("Exiting Contact Lists")
            break
        else :
            print("Invalid choice please enter valid choice")








if __name__ == "__main__":
    main()
