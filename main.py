import pandas as pd
import requests
from bs4 import BeautifulSoup
from pyscript import document



def translate_english1(event):
    
    input_text = document.querySelector("#zn1")
    zn1 = input_text.value
    zn1=zn1.split("\n")
    
    input_text = document.querySelector("#zn2")
    zn2 = input_text.value
    zn2=zn2.split("\n") 
    
    dlin1=len(zn1)
    dlin2=len(zn2)
    itog=((dlin1-1)*(dlin2-1)*0.00006)/60

    
    output_div = document.querySelector("#output5")
    output_div.innerText =itog



def translate_english(event):
    input_text = document.querySelector("#zn1")
    zn1 = input_text.value
    zn1=zn1.split("\n")
    

    add111=0
    k=0
    sum1111 = []
    adresosn = []
    for i in zn1:
        add111+=1
        ad45=zn1
        sum = []
        qw=['ул.,','Санкт-Петербург,','г.','улица,','ул,','лит.','Лит.','пр-кт','город','ул.','улица','дом','литера','корпус']
        for ii1 in qw :
            i=i.replace(ii1, "")
            

        adresosn.append(i)
        k+=1
        alp=['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','ч','ц','ч','ш','щ','ъ','ы','ь','э','ю','я','1','2','3','4','5','6','7','8','9','0','А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']   
        for word in alp:
            su=i.count(word)
            sum.append(su)
    
        sum1="".join(str(x) for x in sum)
        sum1111.append(sum1)

    sum1111.pop()
    zn1.pop()
    adresosn.pop()



    input_text = document.querySelector("#zn2")
    zn2 = input_text.value
    zn2=zn2.split("\n")
    


    add1112=0
    k=0
    sum2222 = []
    adresosn2 = []
    for i in zn2:
        add1112+=1
        ad455=zn2
        sum = []
        qw=['ул.,','Санкт-Петербург,','г.','улица,','ул,','лит.','Лит.','пр-кт','город','ул.','улица','дом','литера','корпус']
        for ii1 in qw :
            i=i.replace(ii1, "")
    
        adresosn2.append(i)
        k+=1
        alp=['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','ч','ц','ч','ш','щ','ъ','ы','ь','э','ю','я','1','2','3','4','5','6','7','8','9','0','А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']   
        for word in alp:
            su=i.count(word)
            sum.append(su)

        sum1="".join(str(x) for x in sum)
        sum2222.append(sum1)
        
    sum2222.pop()
    zn2.pop()
    adresosn2.pop()



    adresosn2end = []
    adresosnend = []
    max_keyend = []
    add=0
    for i in sum1111:
        max_summ=[]
        add+=1
        add1=0
        ad1=zn1
    
        ad49=adresosn
    

        i2=list(i)
        ad50=adresosn2
        ad2=zn2
    
        for i3 in sum2222:
            add1+=1
            i8=list(i3)
            su_buk = []
            for i10 in list(range(0,76)):
                b0=int(i2[i10])-int(i8[i10])
                
                if b0<0 :
                    b0=b0*(-1)
                else:
                    b0=b0

                su_buk.append(b0)
        
            all_sum=(su_buk[0]+su_buk[1]+su_buk[2]+su_buk[3]+su_buk[4]+su_buk[5]+su_buk[6]+su_buk[7]+su_buk[8]+su_buk[9]+su_buk[10]+su_buk[11]+su_buk[12]+su_buk[13]+su_buk[14]+su_buk[15]+su_buk[16]+su_buk[17]+su_buk[18]+su_buk[19]+su_buk[20]+su_buk[21]+su_buk[22]+su_buk[23]+su_buk[24]+su_buk[25]+su_buk[26]+su_buk[27]+su_buk[28]+su_buk[29]+su_buk[30]+su_buk[31]+su_buk[32]+su_buk[33]+su_buk[34]+su_buk[35]+su_buk[36]+su_buk[37]+su_buk[38]+su_buk[39]+su_buk[40]+su_buk[41]+su_buk[42]+su_buk[43]+su_buk[44]+su_buk[45]+su_buk[46]+su_buk[47]+su_buk[48]+su_buk[49]+su_buk[50]+su_buk[51]+su_buk[52]+su_buk[53]+su_buk[54]+su_buk[55]+su_buk[56]+su_buk[57]+su_buk[58]+su_buk[59]+su_buk[60]+su_buk[61]+su_buk[62]+su_buk[63]+su_buk[64]+su_buk[65]+su_buk[66]+su_buk[67]+su_buk[68]+su_buk[69]+su_buk[70]+su_buk[71]+su_buk[72]+su_buk[73]+su_buk[75])/76
            max_summ.append(all_sum)

        

        max_key=min(max_summ)
        max_keyend.append(round(max_key,3))
        ll=-1
        max_summ1=[]
        for i88 in max_summ:
            ll+=1
            if i88 !=max_key:
                max_summ1.append(ll)

            
        index=max_summ.index(max_key)
        adresosnend.append(adresosn[add-1])
        adresosn2end.append(ad2[index])
    komment='Обработка '+ str(add111-1) +' адресов' + ' завершилась'
    output_div = document.querySelector("#output4")
    output_div.innerText =komment

    
    output_div = document.querySelector("#output1")
    output_div.innerText =adresosnend

    output_div = document.querySelector("#output2")
    output_div.innerText =max_keyend

    output_div = document.querySelector("#output3")
    output_div.innerText =adresosn2end


    


