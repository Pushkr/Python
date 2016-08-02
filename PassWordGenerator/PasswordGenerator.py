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


def getweakerpassword():
    weakpasslist = ['password123', 'password1980', '12345678', '123456', 'baseball',
                    'football', 'cricket', 'trustno1', 'batman', 'abc123', '000000']
    return weakpasslist[random.choice(range(0, len(weakpasslist)))]


def getstrongone(passlen):
    loweraplha = string.ascii_lowercase
    upperaplha = string.ascii_uppercase
    digits = string.digits
    specialchar = string.punctuation
    fulllist = (list(loweraplha) + list(upperaplha) + list(digits) + list(specialchar))
    pass1 = ''.join(random.sample(fulllist, passlen))
    print(pass1)


class SetPreferences:
    FullList = list(string.ascii_lowercase)

    def __init__(self):
        self.loweraplha = True
        self.upperaplha = True
        self.digits = True
        self.specialchar = True
        self.passlen = 8  # default

    def setlength(self, passlen):
        self.passlen = passlen
        # print("Password length set to %d" % self.passlen)

    def getlength(self):
        return self.passlen

    def includeupper(self, choice):
        self.upperaplha = choice

    def includedigit(self, choice):
        self.digits = choice

    def includespecial(self, choice):
        self.specialchar = choice

    # def getPreferences(self):
    #     print("Lowercase: %s \n Uppercase : %s \n Digits : %s \n Special : %s",%(self.loweraplha,self.upperaplha,
    #     self.digits,self.specialchar))

    def finalize(self):
        self.FullList = list(string.ascii_lowercase)
        # if self.loweraplha == True:
        #     self.FullList = list(string.ascii_lowercase)
        if self.specialchar is True:
            self.FullList += list(string.punctuation)
        if self.digits is True:
            self.FullList += list(string.digits)
        if self.upperaplha is True:
            self.FullList += list(string.ascii_uppercase)


# noinspection PyMissingConstructor,PyPep8Naming,PyShadowingNames
class NewPassword(SetPreferences):
    def __init__(self, SetPreferences):
        SetPreferences.finalize()
        self.passlen = SetPreferences.passlen
        self.FullList = SetPreferences.FullList

    def getpassword(self):
        pass1 = ''.join(random.sample(self.FullList, self.passlen))
        return pass1

