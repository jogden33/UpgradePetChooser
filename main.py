# Jenny Ogden
# Purpose: Upgrade Pet Chooser
# Write a program that connects to the SQL database, Pets, and reads in the data.
# Print out information regarding your choice of pet and allow user to alter name and age of pet.

# Import my class, Pet, and several other modules.
import pymysql.cursors
from PetsClass import *
import sys

# Connect to the SQL database, Pets, and read in the appropriate data.
try:
    myConnection = pymysql.connect(host='localhost',
                                   user='root',
                                   password='Jenny8212',
                                   db='pets',
                                   charset='utf8mb4',
                                   cursorclass=pymysql.cursors.DictCursor)

except Exception as e:
    print(f"There was an error in the connection. Exiting.")
    print(e)
    print()
    exit()

# Execute a query to read in the data and write each Pet() object to a dictionary, PetsDict.
PetsDict = {}

try:
    with myConnection.cursor() as cursor:
        SqlSelect = """
              select
                pets.id as ID,
                pets.name as PetName,
                pets.age as PetAge, 
                owners.name as OwnerName, 
                types.animal_type as PetType
              from pets join owners on pets.owner_id = owners.id
                        join types on pets.animal_type_id = types.id;
              """

        # Execute the select statement
        cursor.execute(SqlSelect)

        # Loop through all the results, appending a new Pet object to our pets dictionary, PetsDict.
        # Print the data, nicely
        for row in cursor:
            TempPet = Pet(ID = row['ID'],
                          PetName = row['PetName'],
                          PetAge = row['PetAge'],
                          OwnerName = row['OwnerName'],
                          PetType = row['PetType'])
            PetsDict[row['ID']] = TempPet

except Exception as e:
    print(f"An error has occurred while reading in the data. Exiting now.")
    print(TypeError)
    print(e)
    print()

# Close connection
finally:
    myConnection.close()

# Print a nice list of the pets.
print("*".center(30, "*"))
print(" Upgrade Pet Chooser ".center(30, "*"))
print("*".center(30, "*"))
print()

# Create a method that nicely prints the Pet IDs and Pet Names.
def ListOfChoices():
    for ID in PetsDict:
        print(f"[{PetsDict[ID].GetID()}] {PetsDict[ID].GetPetName()}")

    print("[Q] Quit")

# Create a method that allows user to choose a pet and edit the name and age of pet
def ChoosePet():
    ListOfChoices()
    print()
    try:
        Pet = input("Please choose from the list above by typing the pet's number: ")

        # Quit nicely, if the player chooses to
        if Pet.upper() == "Q":
            print("Thank you for playing! Goodbye.")
            sys.exit()

        # If player chooses a number from PetsDict, then display a message describing the pet
        elif int(Pet) in PetsDict:
            TempPet = PetsDict[int(Pet)]
            print(f"You have chosen {TempPet.GetPetName()}, the {TempPet.GetPetType()}. {TempPet.GetPetName()} is "
                  f"{TempPet.GetPetAge()} years old. {TempPet.GetPetName()}'s owner is {TempPet.GetOwnerName()}. ")
            print()
            Continue = input("Would you like to [C]ontinue, [Q]uit, or [E]dit a pet?")

            # If the player chooses to continue, allow them to loop back to list and choose a new pet
            if Continue.upper() == 'C':
                print()
                ChoosePet()

            # Exit program nicely, if the player decides to quit
            elif Continue.upper() == 'Q':
                print("Thank you for playing! Goodbye.")
                sys.exit()

            # If player chooses to edit, first ask which pet they'd like to edit
            elif Continue.upper() == "E":
                print()
                Edit = input("Which pet would you like to edit?")

                # Ask the player for the new name
                if int(Edit) in PetsDict:
                    TempPet = PetsDict[int(Edit)]
                    print(f"You have chosen to edit {TempPet.GetPetName()}.")
                    print()

                    # Force the input, NewName, to be a string
                    NewName = str(input("New name: "))

                    # If no new name is chosen, then keep the original name of pet
                    if NewName == '':
                        print(f"You have chosen to not update the pet's name.")
                        print()
                        NewAge = int(input("New Age: "))

                        # If no new age is chosen, then keep the original age of pet
                        if NewAge == '':
                            print(f"You have chosen to not update the pet's age.")
                            print()

                            # Print the list of pets with new names
                            ListOfChoices()

                        # If new age is chosen, make sure to update the Pet() object
                        else:
                            TempPet.SetPetAge(NewAge)
                            print(f"You have updated the pet age for Pet ID = {TempPet.GetID()} to {TempPet.GetPetAge()}")
                            print()
                            ListOfChoices()

                    # Update the Pet() object with new name
                    else:
                        TempPet.SetPetName(NewName)
                        print(f"You have updated the pet name for Pet ID = {TempPet.GetID()} to '{TempPet.GetPetName()}'")
                        print()
                        NewAge = input("New Age: ")

                        if NewAge == '':
                            print(f"You have chosen to not update the pet's age.")
                            print()
                            ListOfChoices()

                        else:
                            NewAge = int(NewAge)
                            TempPet.SetPetAge(NewAge)
                            print(f"You have updated the pet age for Pet ID = {TempPet.GetID()} to {TempPet.GetPetAge()}")
                            print()
                            ListOfChoices()
                else:
                    print(f"Invalid Input! Thanks for playing.")
                    sys.exit()
            else:
                print(f"Invalid Input! Thanks for playing.")
                sys.exit()
        else:
            print(f"Invalid Input! Thanks for playing.")
            sys.exit()

    except ValueError as e:
        print(f"Invalid input. Thanks for playing!")

    except Exception as e:
        print(f"{Pet} is an invalid choice.")
        print(f"Error Message: {e}")

# Play the game!
ChoosePet()