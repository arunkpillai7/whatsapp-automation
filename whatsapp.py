import pywhatkit
print(' You have to open the whatsapp web version in your default browser')
print(' ')
print(' ')

phone = input('Enter the phone number you want to send the message: ')

msg = input('Enter the message you wanna send: ')
timeh = input('Enter the time to send the message in 24 hour format : ')
times = input('Enter the remaining time in minutes : ')


pywhatkit.sendwhatmsg( phone, msg , int(timeh) , int(times) )
print('Message delivered succesfully')
