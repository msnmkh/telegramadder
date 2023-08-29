from telethon import functions, types
from telethon import TelegramClient
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest
from phoneNumbers import createPhoneNumbers
from CONSTANT import *
from readWrite import *
import asyncio
import random

phone_number = ''      # Your Phone Number With Country Code.
################################################
# +989917922078 | 
client = TelegramClient('', API_ID, API_HASH)

# ---------------------------------------
# add user to contact
async def connect():
    await client.connect()
    async with client:
        if not await client.is_user_authorized():
            client.send_code_request(phone_number)
            me = client.sign_in(phone_number, input('Enter code: '))
        
        # get phone number from csv

        userInput = "8"
        cnt = 0
        # loop phone number
        result = createPhoneNumbers(userInput,40)
        print(result)
        print("--------------------------")
        empUser = 0
        for number in result:
            cnt +=1
            if(cnt%15==0):
                # check this user have telegram account
                await asyncio.sleep(random.randint(400,600))
                print("##30##")

            contact = InputPhoneContact(client_id=0, phone=number, first_name=number, last_name=number)
            await asyncio.sleep(random.randint(25,30))
            result = await client(ImportContactsRequest([contact]))
            await asyncio.sleep(random.randint(15,16))

            # check this user have telegram account
            # print(result)
            # print(len(result.users))
            
            if(len(result.users)>0):
                username = None
                try:
                    username = await client(AddChatUserRequest(user_id=result.users[0], fwd_limit=0, chat_id=GROUPID))
                    # save phone number have telegram in to excel
                    teleFile = COUNTRIES[userInput]['Name']+"TeleMobile"
                    writeToCSV(teleFile,[number])
                    print(number)
                except:
                    print("inexcept: " + number)

                # remove contact
                if username is not None: #if username is not empty
                    await client(functions.contacts.DeleteContactsRequest(id=[result.users[0]]))
                    await asyncio.sleep(random.randint(7,10))
            else:
                empUser += 1
                teleFile = COUNTRIES[userInput]['Name']+"NotTeleMobile"
                writeToCSV(teleFile,[number])


asyncio.run(connect())



