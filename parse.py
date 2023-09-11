from pyrogram import Client
import re

api_id =  29571255 
api_hash = "7fbceeecda9658cc3335cc5ef449a2b5"
app = Client("my_account", api_id=api_id, api_hash=api_hash)


def extract_company_and_director(text):
    director = ""
    text = re.sub("[^A-Za-z\s]", "", text)
    company_name = ' '.join(text.split())
    print(company_name,"\n\n")
    
    
    return director, company_name
    


async def main():
    async with app:
        # "me" refers to your own chat (Saved Messages)
        async for message in app.get_chat_history("kjdasnflkasjbdnl"):
            text = message.text
            director, company_name = extract_company_and_director(str(text))


app.run(main())