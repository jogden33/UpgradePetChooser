# Jenny Ogden
# Purpose: Write a program that connects to the SQL database, Pets, reads in the data and
# prints out information regarding your choice of pet.

import pymysql.cursors
import pprint as pp

# Steps 1 and 2: Start and connect to the SQL Database, Pets:
try:
    myConnection = pymysql.connect(host='localhost',
                                   user='root',
                                   password='Jenny8212',
                                   db='pets',
                                   charset='utf8mb4',
                                   cursorclass=pymysql.cursors.DictCursor)

except Exception as e:
    print(f"There was an error in the connection.")
    print()

# Step 3: Read in the data from the Pets database and write it into a list called PetsList.
PetsList = []

try:
    with myConnection.cursor() as cursor:
        SqlSelect = """
              select
                pets.name as PetName,
                pets.age as PetAge, 
                owners.name as OwnerName, 
                types.animal_type as PetType
              from pets join owners on pets.owner_id = owners.id
                        join types on pets.animal_type_id = types.id;
              """

        # Execute select
        cursor.execute(SqlSelect)

        # Loop through all the results
        # Print the data, nicely
        for row in cursor:
            #print(row)
            PetsList.append(row)

# If there is an exception, show what that is
except:
    print(f"An error has occurred while reading in the data")
    print()

# Close connection
finally:
    myConnection.close()

# Create a separate list for each pet that includes the following keys: PetName, PetAge, OwnerName, and PetType.
HarveyList = list(PetsList[0].values())
BooList = list(PetsList[1].values())
MickeyList = list(PetsList[2].values())
CallieList = list(PetsList[3].values())
MaxList = list(PetsList[4].values())
CharlieList = list(PetsList[5].values())
KingList = list(PetsList[6].values())
TweetyList = list(PetsList[7].values())
BingoList = list(PetsList[8].values())

# Import the class Pets from the Python file, PetsClass.
from PetsClass import Pets

# Step 4: Create one instance of a Pets class for each of the 9 pets listed in the Pets database.
# Append the pet objects into a list, called ListOfObjects.
ListOfObjects = []

ListOfObjects.append(Pets(HarveyList[0], HarveyList[1], HarveyList[2], HarveyList[3]))
ListOfObjects.append(Pets(BooList[0], BooList[1], BooList[2], BooList[3]))
ListOfObjects.append(Pets(MickeyList[0], MickeyList[1], MickeyList[2], MickeyList[3]))
ListOfObjects.append(Pets(CallieList[0], CallieList[1], CallieList[2], CallieList[3]))
ListOfObjects.append(Pets(MaxList[0], MaxList[1], MaxList[2], MaxList[3]))
ListOfObjects.append(Pets(CharlieList[0], CharlieList[1], CharlieList[2], CharlieList[3]))
ListOfObjects.append(Pets(KingList[0], KingList[1], KingList[2], KingList[3]))
ListOfObjects.append(Pets(TweetyList[0], TweetyList[1], TweetyList[2], TweetyList[3]))
ListOfObjects.append(Pets(BingoList[0], BingoList[1], BingoList[2], BingoList[3]))

# Step 5: Display a list of pet names, from the pet object instances:
print()
print("List of Pet Names:")
for obj in ListOfObjects:
    print(obj.PetName)

# Steps 6 and 7: Ask the user to choose a pet and print the specified pet's information.
try:
    while True:
        print()
        guess = str(input(
        f"""Please choose a pet from the list below by typing its name:
        [1] Harvey\t\t [2] Boo\t\t [3] Mickey
        [4] Callie\t\t [5] Max\t\t [6] Charlie
        [7] King\t\t [8] Tweety\t\t [9] Bingo
        [Q] Quit\n\nChoice: """))
        # Allow the user to quit instead of guessing a pet by entering 'q' or 'quit'
        if guess.lower() in ("q", "quit"):
            print(f"You are now exiting the pet chooser game!!")
            break

        try:
        # For each object in the Pet list, print out the attributes of name, type, age, and owner name.
            for obj in ListOfObjects:
                if guess.lower() == obj.PetName.lower():
                    name = obj.PetName
                    age = obj.PetAge
                    owner = obj.OwnerName
                    type = obj.PetType
                    print(f"""You have chosen {obj.PetName}, the {obj.PetType}. {obj.PetName} is {obj.PetAge} years old.
{obj.PetName}'s owner is {obj.OwnerName}.""")
                    print()
                    input(f"Press [ENTER] to continue.")
        except:
            print(f"ERROR: Invalid input! Please choose a pet from the list above.")
            print()
            continue
except:
    print(f"ERROR: Invalid Input!")