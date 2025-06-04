def show_help():
    print("Type 'ayude' to get a list of all the things you can do")
    print("Type 'vea' to get a list of all the animals")
    print("Type 'mascota' followed by the animal's name to pet a particular animal")
    print("Type 'ciao' to leave the zoo and exit the program")


def show_all_animals():
    print("The animals in the zoo are:")
    print("• Clover the Bunny 🐇")
    print("• Coco the Baby Goat 🐐")
    print("• Arno the Alligator 🐊")
    print("• Bella the Bear 🐻")


def pet_animal(animal):
    if animal == "clover":
        print("Clover is so happy! ❤️")
    elif animal == "coco":
        print("Coco the Baby Goat thanks you! 🥰")
    elif animal == "arno":
        print("Actually, we cannot allow you to pet Arno. ⛔️")
    elif animal == "bella":
        print("Bella the Bear is not in the mood for petting. 😒")
    else:
        print("Sorry, I don't know that animal")


print("Welcome to the Petting Zoo!")
print("Type 'help' to get a list of all the things you can do")
print()

keep_going = True
while keep_going:
    response = input("What would you like to do? ").strip().lower()
    if response == "ayude":
        show_help()
    elif response == "vea":
        show_all_animals()
    elif response.startswith("mascota "):
        animal = response[8:]
        pet_animal(animal)
    elif response == "ciao":
        print("Goodbye!")
        keep_going = False
    else:
        print("Sorry, I don't understand that command")
