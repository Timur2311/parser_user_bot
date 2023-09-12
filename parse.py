from pyrogram import Client
import re
import pandas as pd
import openpyxl


api_id =  29571255 
api_hash = "7fbceeecda9658cc3335cc5ef449a2b5"
app = Client("my_account", api_id=api_id, api_hash=api_hash)


def extract_company_and_director(text):
    mchj_list = ["ooo","mchj","ооо","мчж","MChJ", "MCHJ","ООО","МЧЖ","OOO"]
    bad_words = ["Добрый день","Здравствуйте","коллеги","“","\"",",","«","»","!"]
    company_permission = ""
    
    # extracting unnecessary words
    for bad_word in bad_words:
        text = text.replace(bad_word,"")
    
    # extracting mchj_or_OOO
    for sub_text in mchj_list:
        if sub_text in text:
            text = text.replace(sub_text,"")
            company_permission = sub_text
    # extracting_company_name      
    company_text = re.sub("[^A-Za-z\s\-’]", "", text)
    
    company_name = ' '.join(company_text.split())
    # delete some characters
    if re.search("-$", company_name) !=None:
        company_name = company_name.replace("-","")
        
    director = text.replace(company_name.strip(), "")    
    company_name+=f" {company_permission}"   
    
    return director, company_name
    


async def main():
    async with app:
        data_list = []
        async for message in app.get_chat_history("kjdasnflkasjbdnl"):
            text = message.text
            if text is None:
                continue
            director, company_name = extract_company_and_director(str(text))
            data_list.append([company_name, director])
        df = pd.DataFrame(data_list,
                 columns=['company', 'director(s)'])
        df.to_excel('directors.xlsx', sheet_name='list')

app.run(main())