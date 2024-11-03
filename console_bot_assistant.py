from typing import Callable, Dict

contacts = {}

def input_error(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Incomplete command, provide necessary arguments"
    return inner

# Команди бота
@input_error
def add_contact(args: list[str]) -> str:
    if len(args) < 2:
        return "Give me name and phone please"  
    name, phone = args[0], args[1]
    contacts[name] = phone
    return "Contact added."

@input_error
def get_phone(args: list[str]) -> str:
    if len(args) < 1:
        return "Enter user name"  
    name = args[0]
    return contacts.get(name, "Contact not found.")

@input_error
def show_all(args: list[str]) -> str:
    if not contacts:
        return "No contacts in the list."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

@input_error
def unknown_command(args: list[str]) -> str:
    return "Unknown command. Please try again."

# Обробник команд
def handle_command(command: str, args: list[str]) -> str:
    commands = {
        "add": add_contact,
        "phone": get_phone,
        "all": show_all
    }
    return commands.get(command, unknown_command)(args)

# Основний цикл
def main():
    print("Welcome to the contact manager bot!")
    while True:
        user_input = input("Enter a command: ").strip().split()
        
        if not user_input:
            print("Please enter a command.")
            continue
        
        command = user_input[0].lower()
        args = user_input[1:]
        
        result = handle_command(command, args)
        print(result)

if __name__ == "__main__":
    main()