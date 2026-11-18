import json
import os

DATA_FILE = "data/contacts.json"


def load_contacts():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            contacts = json.load(f)
            if not isinstance(contacts, list):
                return []
            return [
                contact
                for contact in contacts
                if isinstance(contact, dict)
                and isinstance(contact.get("name"), str)
                and isinstance(contact.get("phone"), str)
            ]
        except (json.JSONDecodeError, OSError):
            return []


def save_contacts(contacts):
    directory = os.path.dirname(DATA_FILE)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=4)