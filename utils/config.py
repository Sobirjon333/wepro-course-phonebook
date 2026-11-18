
from utils.storage import DATA_FILE, load_contacts, save_contacts


def show_contacts(contacts):
    if not contacts:
        print("Телефонная книга пуста.")
        return
    print("\n--- Список контактов ---")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} — {contact['phone']}")
    print("-" * 25)

def add_contact(contacts):
    name = input("Введите имя: ").strip()
    phone = input("Введите номер телефона: ").strip()
    if name and phone:
        contacts.append({"name": name, "phone": phone})
        save_contacts(contacts)
        print(f"Контакт {name} успешно добавлен!")
    else:
        print("Имя и номер не могут быть пустыми.")

def search_contact(contacts):
    query = input("Введите имя для поиска: ").strip().lower()
    found = [c for c in contacts if query in c['name'].lower()]
    if found:
        print(f"\nНайдено контактов: {len(found)}")
        for contact in found:
            print(f"- {contact['name']}: {contact['phone']}")
    else:
        print("Контакт не найден.")

def main():
    contacts = load_contacts()
    while True:
        print("\n1. Показать контакты")
        print("2. Добавить контакт")
        print("3. Найти контакт")
        print("4. Выход")
        
        choice = input("Выберите пункт меню: ").strip()
        
        if choice == "1":
            show_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Неверный выбор, попробуйте снова.")
