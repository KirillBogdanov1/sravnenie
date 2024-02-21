import pandas as pd
import requests
from bs4 import BeautifulSoup
from pyscript import document








def translate_english(event):



    excel_data_df = pd.read_excel('./adress1.xlsx',index_col=None)
    dfs = []
    add111=0
    k=0
    for i in excel_data_df['название Адреса'].tolist():
        print(i)





    
    output_div = document.querySelector("#output")
    output_div.innerText =i 

