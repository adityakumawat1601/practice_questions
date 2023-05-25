class Person:
    def __init__(self,lastname,name,phone,email):
        self.lastname = lastname
        self.name = name
        self.phone = phone
        self.email = email
    def __str__(self):
        return f"{self.lastname},{self.name}-phone number--{self.phone}-email address--{self.email}"
    
class Addressbook:
    def __init__(self):
        self.contacts = []
    def add_contact(self,person):
        self.contacts.append(person)
    def show_contacts(self):
        for item in self.contacts:
            print(item)
    def lookup_contacts(self,lastname,name=None):
        if name == None:
            for person in self.contacts:
             #search by only last name
                    if person.lastname == lastname:
                        print(person.name)
        else:
            for person in self.contacts:
                if person.lastname==lastname and person.name==name:
                    print(person.name)
aditya = Person("kumawat","aditya","4203423203","adityakumawat@gmail.com")
parth =  Person("kumawat","parth","234234243","parth444@gmail.com")
x= Addressbook()
x.add_contact(aditya)
x.add_contact(parth)
x.show_contacts()
x.lookup_contacts("kumawat","aditya")
