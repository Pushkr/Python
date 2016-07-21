from PasswordGenerator import SetPreferences,NewPassword
import unittest
import string

class TestThis(unittest.TestCase):

    def setUp(self):
        pass

    def test_case1(self):
        ''' test for multiple sized password'''
        self.s1 = SetPreferences()
        for i in range (1,51):
            self.s1.setlength(i)
            self.n1 = NewPassword(self.s1).getpassword()
            self.assertEqual(len(self.n1),i)


    def test_case2(self):
        ''' Test with excluding digits'''
        s0 = SetPreferences()
        s0.includedigit(False)
        n0 = NewPassword(s0).getpassword()
        list1 = [x for x in list(n0) if x.isdigit() == True]
        self.assertEqual(len(list1),0)


    def test_case3(self):
        ''' test with excluding Upper case characters'''
        s2 = SetPreferences()
        s2.includeupper(False)
        n2= NewPassword(s2)
        p2=n2.getpassword()
        list1 = [x for x in list(p2) if x.isupper() == True]
        self.assertEqual(len(list1), 0)

    def test_case4(self):
        ''' test with excluding special characters'''
        s4 = SetPreferences()
        s4.includespecial(False)
        p4 = NewPassword(s4).getpassword()
        list1 = [x for x in list(p4) if x in list(string.punctuation)]
        self.assertEqual(len(list1),0)

    def test_case5(self):
        ''' default length test'''
        p5=NewPassword(SetPreferences()).getpassword()
        self.assertEqual(len(p5),8)



# print(GetWeakerPassword())
# PassLen = int(input("Enter desired password length:"))
# GetStrongOne(PassLen)
# NewPref = SetPreferences()
# NewPref.IncludeDigit(True)
# NewPref.IncludeUpper(False)
# NewPref.IncludeSpecial(False)
# NewPref.setlength(12)
#
#
# PassWord = NewPassword(NewPref) ;
# print(PassWord.getpassword())
#
# s = SetPreferences()
# new1 = NewPassword(s)
# print(new1.getpassword())
