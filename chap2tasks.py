#3-1 Names
names = ["Jason", "Bob", "James", "Brian", "Marie"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

#3-2 Greetings
message = " you are a friend"
print(names[0] + message)
print(names[1] + message)
print(names[2] + message)
print(names[3] + message)
print(names[4] + message)

#3-3 Your Own List
cars = ["BMW", "BatMobile", "Sports Car"]
message = (f"I want to own a {cars[0]}")
print(message)
message = (f"I want to own a {cars[1]}")
print(message)
message = (f"I want to own a {cars[2]}")
print(message)

#3-4 Guest List
invite_list = ["Augustus Ceasar", "Winston Churchill", "George Washington"]
print(invite_list[0] + " You are invited to dinner")
print(invite_list[1] + " You are invited to dinner")
print(invite_list[2] + " You are invited to dinner")

#3-5 Changing Guest List
print(invite_list[1] + " is unable to attend")

invite_list[1] = "King Alfred"
print(invite_list[0] + " You are invited to dinner")
print(invite_list[1] + " You are invited to dinner")
print(invite_list[2] + " You are invited to dinner")

#3-6
print("A larger table has been found and more guests will be invited!")

invite_list.insert(0, "Dwayne Johnson")
invite_list.insert(1, "Marilyn Monroe")
invite_list.append("Emma Watson")

print(invite_list[0] + " You are invited to dinner")
print(invite_list[1] + " You are invited to dinner")
print(invite_list[2] + " You are invited to dinner")
print(invite_list[3] + " You are invited to dinner")
print(invite_list[4] + " You are invited to dinner")
print(invite_list[5] + " You are invited to dinner")

#3-7 Shrinking Guest List

print(invite_list)

print(invite_list.pop(1) + " ,I'm sorry you can't come to dinner")
print(invite_list.pop(1) + " ,I'm sorry you can't come to dinner")
print(invite_list.pop(1) + " ,I'm sorry you can't come to dinner")
print(invite_list.pop(1) + " ,I'm sorry you can't come to dinner")

print(invite_list[0] + " you are still invited")
print(invite_list[1] + " you are still invited")

invite_list.remove("Dwayne Johnson")
invite_list.remove("Emma Watson")

print(invite_list)

#3-8 Seeing the World
places = ["China", "Japan", "Germany", "Cannada", "Russia", "France"]
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)

#3-9 Dinner Guests
print(len(invite_list))

#3-10 Every Function
languages = ["Mandarin", "Japanese", "English", "German", "Irish", "French"]
print(sorted(languages))
languages.reverse()
languages.sort()
languages.append("Russian")
languages.insert(3, "Arabic")
languages.remove("French")
print("I am learning " + languages.pop(5))
print(languages)

#3-11 Intentional error (fixed)
print("Cat")
