data1 = {'abc@gmail.com':'qwerty'}
data2={}

print('Welcome! \n ')

x = input('Would You like to Login or Sign Up').lower()
if x == 'login':
    y = input('Please enter your email address').lower()
    z = input('Please enter your password').lower()
    data2[x] = y

   
        else:
        print('Incorrect email address or password')



elif x == 'sign up':
    a = input('Please enter your email address')
    b = input('Please enter your password')
    c = input('Please enter your password again')
