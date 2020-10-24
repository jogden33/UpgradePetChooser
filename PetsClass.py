"""
Jenny Ogden
Purpose: Pet Class
    Properties:
     1. ID - Pet's ID (integer)
     2. PetName - Pet's name (string)
     3. PetAge - Age of the pet (integer)
     4. OwnerName - Name of the pet's owner (string)
     5. PetType - Type of animal (string)

    Methods:
     1. GetID(), SetID()
     2. GetPetName(), SetPetName()
     3. GetPetAge(), SetPetAge()
     4. GetOwnerName(), SetOwnerName()
     5. GetPetType(), SetPetType()
"""

class Pet:
    # Create private properties
    __ID = 1
    __PetName = "Bella"
    __PetAge = 0
    __OwnerName = "Jenny"
    __PetType = "dog"

    def __init__(self,
                 ID = 1,
                 PetName = "Bella",
                 PetAge = 0,
                 OwnerName = "Jenny",
                 PetType = "dog"):

        self.SetID(ID)
        self.SetPetName(PetName)
        self.SetPetAge(PetAge)
        self.SetOwnerName(OwnerName)
        self.SetPetType(PetType)

    # Getter and Setter for ID
    def GetID(self):
        return (self.__ID)

    def SetID(self, ID):
        try:
            if int(ID):
                self.__ID = ID
        except Exception as e:
            raise TypeError(f"{ID} does not look like an integer!")

    # Getter and Setter for PetName
    def GetPetName(self):
        return (self.__PetName)

    def SetPetName(self, PetName):
        try:
            if str(PetName):
                self.__PetName = PetName
        except Exception as e:
            raise TypeError(f"{PetName} seems to be empty!")

    # Getter and Setter for PetAge
    def GetPetAge(self):
        return (self.__PetAge)

    def SetPetAge(self, PetAge):
        try:
            if int(PetAge):
                self.__PetAge = PetAge
        except Exception as e:
            raise TypeError(f"{PetAge} does not look like an integer!")

    # Getter and Setter for OwnerName
    def GetOwnerName(self):
        return (self.__OwnerName)

    def SetOwnerName(self, OwnerName):
        try:
            if str(OwnerName):
                self.__OwnerName = OwnerName
        except Exception as e:
            raise TypeError(f"{OwnerName} seems to be empty!")

    # Getter and Setter for PetType
    def GetPetType(self):
        return (self.__PetType)

    def SetPetType(self, PetType):
        try:
            if str(PetType):
                self.__PetType = PetType
        except Exception as e:
            raise TypeError(f"{PetType} seems to be empty!")