from pyrogram import Client
import re

api_id =  29571255 
api_hash = "7fbceeecda9658cc3335cc5ef449a2b5"
app = Client("my_account", api_id=api_id, api_hash=api_hash)


def extract_company_and_director(text):
    mchj_list = ["ooo","mchj","ооо","мчж","MChJ", "MCHJ","ООО","МЧЖ","OOO"]
    company_permission = ""
    
    for sub_text in mchj_list:
        if sub_text in text:
            text = text.replace(sub_text,"")
            company_permission = sub_text
    company_text = re.sub("[^A-Za-z\s\-]", "", text)
    
    company_name = ' '.join(company_text.split())
    if re.search("-$", company_name) !=None:
        company_name = company_name.replace("-","")
        
    print(company_name,"\n\n")
    director = text.replace(company_name, "")
    company_name+=f" {company_permission}"
    
    # print(director,"\n\n")
    return "director", company_name
    


async def main():
    async with app:
        # "me" refers to your own chat (Saved Messages)
        async for message in app.get_chat_history("kjdasnflkasjbdnl"):
            text = message.text
            director, company_name = extract_company_and_director(str(text))


app.run(main())