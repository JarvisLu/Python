__author__ = 'Jarvis'
# A single hash character is used to comment a single line

''' Three single-quote marks are used to open and close a multiple line comment.
    Three single-quote marks are used to open and close a multiple line comment.
    Three single-quote marks are used to open and close a multiple line comment.'''

ExtronAna = 'Extron Electronics'
print(ExtronAna)

ExtronAna = ExtronRal = ExtronDal = 'Extron Electronics'
print(ExtronRal)
print(ExtronDal)

ExtronAna, ExtronRal, ExtronDal = 'Extron1', 'Extron2', 'Extron3'
print(ExtronAna)
print(ExtronRal)
print(ExtronDal)

ExtronLoc = ['Dallas', 'Raleigh', 'Anaheim']
print('Extron is located in:' , ExtronLoc[2])

ExtInfo = {'name':'Extron Electronics', 'city':'Anaheim', 'street':'Ball Road', 'address':1025}
print(ExtInfo['name'], 'is located in', ExtInfo['city'], 'on', ExtInfo['address'], ExtInfo['street'],'.')

def ExtronAnaheim():
    Extron = 'Extron Electronics'
    print(Extron, 'is located in Anaheim')

ExtronAnaheim()


print('Extron Electronics')

ExtronLoc = ['Anaheim', 'Raleigh', 'Dallas']
print(ExtronLoc[2])

print('{} headquarters are in {}'.format('Extron', 'Anaheim'))

print('{0} has an office in {1}'.format('Extron', 'Raleigh'))

ExtronLoc = int(input('How many times have you been to Extron in Anaheim?:'))

if ExtronLoc < 1:
    print('Please come visit Extron.')
elif ExtronLoc > 1:
    print('Welcome back to Extron!')
else :
    print('Welcome to Extron!')