# Write a password generator in Python. Be creative with how you generate passwords - 
# strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
# The passwords should be random, generating a new password every time the user asks for a new password. 
# Include your run-time code in a main method.
# 
# Extra:
# 
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

import random
import string

# Below solution have two type of implementation. First is using function calls GetWeakerPassword and GetStrongerOne.
# Second solution consist of class implementation where, user can set the preferences for password by calling various INCLUDE 
#methods 


def GetWeakerPassword():
    WeakPassList = ['password123', 'password1980', '12345678', '123456', 'baseball',
                    'football', 'cricket', 'trustno1', 'batman', 'abc123', '000000']
    return WeakPassList[random.choice(range(0, len(WeakPassList)))]


def GetStrongOne(PassLen):
    LowerAlpha = string.ascii_lowercase
    UpperAlpha = string.ascii_uppercase
    Digits = string.digits
    SpecialChar = string.punctuation
    FullList = (list(LowerAlpha) + list(UpperAlpha) + list(Digits) + list(SpecialChar))
    pass1 = ''.join(random.sample(FullList, PassLen))
    print(pass1)


class SetPreferences():
    FullList = list(string.ascii_lowercase)

    def __init__(self):
        self.loweraplha = True
        self.upperaplha = True
        self.digits = True
        self.specialchar = True
        self.passlen = 8   # Default password length

    def setlength(self, passlen):
        self.passlen = passlen
        print("Password length set to %d" % self.passlen)

    def getlength(self):
        return self.passlen

    def IncludeUpper(self,choice):
        self.upperaplha = choice

    def IncludeDigit(self,choice):
        self.digits = choice

    def IncludeSpecial(self,choice):
        self.specialchar = choice

    def Finalize(self):
        # FullList = list(string.ascii_lowercase)
        if self.specialchar == True:
            self.FullList += list(string.punctuation)
        if self.digits == True:
            self.FullList += list(string.digits)
        if self.upperaplha == True:
            self.FullList += list(string.ascii_uppercase)


class NewPassword(SetPreferences):

    def __init__(self,SetPreferences):
        self.passlen=SetPreferences.passlen
        self.FullList = SetPreferences.FullList

    def getpassword(self):
        pass1 = ''.join(random.sample(self.FullList,self.passlen))
        return pass1

#Solution using function calls
print(GetWeakerPassword())
PassLen = int(input("Enter desired password length:"))
GetStrongOne(PassLen)


#Solution using class implementation

NewPref = SetPreferences()
NewPref.IncludeDigit(True)
NewPref.IncludeUpper(False)
NewPref.IncludeSpecial(False)
NewPref.setlength(12)
NewPref.Finalize()   

PassWord = NewPassword(NewPref) ;
print(PassWord.getpassword())

# using default settings of preferences.
s = SetPreferences()
new1 = NewPassword(s)
print(new1.getpassword())
