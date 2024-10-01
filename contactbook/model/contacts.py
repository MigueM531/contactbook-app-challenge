from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Contact:
    name: str
    phone: str
    email: str
    tags: list[str] = field(default_factory=list)
    creation_date: datetime = field(init=False, default=datetime.now())

    def add_tag(self, tag: str):
        if tag in self.tags:
            return
        else:
            self.tags.append(tag)

    def __str__(self) -> str:
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nTags: {",".join(self.tags)}\nCreated on: {self.creation_date}"


@dataclass
class ContactBook:
    contacts: dict[str, Contact] = field(init=False, default_factory=dict)

    def add_contact(self, name: str, phone: str, email: str, tags: list[str]):
        contact = Contact(name, phone, email, tags)
        self.contacts[phone] = contact

    def delete_contact(self, phone: str):
        self.contacts.pop(phone)

    def list_contacts(self) -> list[Contact]:
        contact_list = []
        for phone,contact in self.contacts.items():
            contact_list.append(contact)
        return contact_list

    def contacts_by_tag(self, tag: str) -> list[Contact]:
        contact_list = []
        for phone,contact in self.contacts.items():
            if tag in contact.tags:
                contact_list.append(contact)
        return contact_list

    def search_by_criteria(self, name: str = "", phone: str = "", email: str = "") -> list[Contact]:
        contact_list_name = []
        for phone_contact, contact in self.contacts.items():
            if len(name) == 0:
                contact_list_name.append(contact)
            elif name.lower() in contact.name.lower():
                contact_list_name.append(contact)
        print(contact_list_name)

        contact_list_phone = []
        for contact in contact_list_name:
            print(contact.phone)
            print(len(phone))
            if len(phone) == 0:
                contact_list_phone.append(contact)
            elif phone.lower() in contact.phone.lower():
                contact_list_phone.append(contact)
        print(contact_list_phone)

        contact_list_email = []
        for contact in contact_list_phone:
            if len(email) == 0:
                contact_list_email.append(contact)
            elif email.lower() in contact.email.lower():
                contact_list_email.append(contact)
        print(contact_list_email)
        return contact_list_email
