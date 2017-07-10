import fbchat
import sys
import getpass
from fbchat.models import *
user_name = raw_input("Enter your fb username: ")
password = str("NULL")

password = getpass.getpass("Enter your password: ") 

client = fbchat.Client(user_name, password)

friend_name = raw_input("Enter the person you want to torture: ") 

friends = client.searchForUsers(friend_name) #return a list of names 
friend = friends[0]

message = raw_input("Enter the message for your friend :) ") 

times = raw_input("Enter how many times u wanna bug that friend of yours :) ") 

for i in range(int(times)):
	message_id = client.sendMessage(message, thread_id=friend.uid, thread_type=ThreadType.USER)


print(" \n Mischief Managed... #TECHroll!")



