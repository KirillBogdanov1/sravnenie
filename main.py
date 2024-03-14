import pandas as pd
import requests
from bs4 import BeautifulSoup
from pyscript import document
import re



    



def translate_english1(event):
    
    input_text = document.querySelector("#zn1")
    zn1 = input_text.value
    zn1=zn1.split("\n")
    
    input_text = document.querySelector("#zn2")
    zn2 = input_text.value
    zn2=zn2.split("\n") 
    
    dlin1=len(zn1)
    dlin2=len(zn2)
    itog=((dlin1-1)*(dlin2-1)*0.0000105)/60
    itog2=((dlin1-1)*(dlin2-1)*0.0000165)/60

    
    output_div = document.querySelector("#output5")
    output_div.innerText =itog 

    output_div = document.querySelector("#output55")
    output_div.innerText =itog2 






def translate_english0(event):
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
        sum555 = []
        
        qw=['ул.,','Санкт-Петербург,','б/н','г.','улица,','пос.','ул,','лит.','Лит.','пр-кт','город','ул.','улица','дом','литера','корпус','строение','проспект','Проспект','набережная','наб']
        if "_" in i:
            i=i[:i.index('_')]
        for ii1 in qw :
            i=i.replace(ii1, "")
        if i.startswith('19'):
            i=i[6:]
            

        adresosn.append(i)
        k+=1
        alp=['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','ч','ц','ч','ш','щ','ъ','ы','ь','э','ю','я','1','2','3','4','5','6','7','8','9','0','А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']   
        for word in alp:
            su=i.count(word)
            sum555.append(su)
    
        sum1="".join(str(x) for x in sum555)
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
        sum555 = []
        qw=['ул.,','Санкт-Петербург,','б/н','г.','улица,','пос.','ул,','лит.','Лит.','пр-кт','город','ул.','улица','дом','литера','корпус','строение','проспект','Проспект','набережная','наб']
        if "_" in i:
            i=i[:i.index('_')]
        for ii1 in qw :
            i=i.replace(ii1, "")
        if i.startswith('19'):
            i=i[6:]
            
    
        adresosn2.append(i)
        k+=1
        alp=['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','ч','ц','ч','ш','щ','ъ','ы','ь','э','ю','я','1','2','3','4','5','6','7','8','9','0','А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']    
        for word in alp:
            su=i.count(word)
            sum555.append(su)

        sum1="".join(str(x) for x in sum555)
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

        
        numbers = re.findall('\d+', adresosn[add-1])
        numbers=''.join(numbers)


        for i3 in sum2222:
            add1+=1
            i8=list(i3)
            su_buk = []
            
            numbers2 = re.findall('\d+', ad2[add1-1])
            numbers2=''.join(numbers2)
            
            if numbers==numbers2 : 
            
                for i10 in list(range(0,76)):
                    b0=int(i2[i10])-int(i8[i10])
                
                    if b0<0 :
                        b0=b0*(-1)
                    else:
                        b0=b0

                
                    su_buk.append(b0)
        
                all_sum=int(sum(su_buk))/76
                max_summ.append(all_sum)        
            else :
                all_sum=1
                max_summ.append(all_sum)  
                
        add166=0
        max_key=min(max_summ)
        for i9898 in max_summ:
 
            add166+=1
            if i9898==max_key:

                if ad2[add166-1][-1]=="А":

                    max_summ[add166-1]=max_key-0.01
                    max_key=min(max_summ) 
        
        max_keyend.append(round(max_key,3))
        ll=-1
        max_summ1=[]
        for i88 in max_summ:
            ll+=1
            if i88 !=max_key:
                max_summ1.append(ll)

            
        index=max_summ.index(max_key)
        adresosnend.append(zn1[add-1])
        adresosn2end.append(zn2[index])
    komment='Обработка '+ str(add111-1) +' адресов' + ' завершилась'
    output_div = document.querySelector("#output4")
    output_div.innerText =komment

    
    output_div = document.querySelector("#output1")
    output_div.innerText =adresosnend

    output_div = document.querySelector("#output2")
    output_div.innerText =max_keyend

    output_div = document.querySelector("#output3")
    output_div.innerText =adresosn2end


        
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
        sum555 = []
        
        qw=['ул.,','Санкт-Петербург,','б/н','г.','улица,','пос.','ул,','лит.','Лит.','пр-кт','город','ул.','улица','дом','литера','корпус','строение','проспект','Проспект','набережная','наб']
        if "_" in i:
            i=i[:i.index('_')]
        for ii1 in qw :
            i=i.replace(ii1, "")
        if i.startswith('19'):
            i=i[6:]
            

        adresosn.append(i)
        k+=1
        alp=['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','ч','ц','ч','ш','щ','ъ','ы','ь','э','ю','я','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100','А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']   
        for word in alp:
            su=i.count(word)
            sum555.append(su)
    
        sum1="".join(str(x) for x in sum555)
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
        sum555 = []
        qw=['ул.,','Санкт-Петербург,','б/н','г.','улица,','пос.','ул,','лит.','Лит.','пр-кт','город','ул.','улица','дом','литера','корпус','строение','проспект','Проспект','набережная','наб']
        if "_" in i:
            i=i[:i.index('_')]
        for ii1 in qw :
            i=i.replace(ii1, "")
        if i.startswith('19'):
            i=i[6:]
            
    
        adresosn2.append(i)
        k+=1
        alp=['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','ч','ц','ч','ш','щ','ъ','ы','ь','э','ю','я','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100','А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']    
        for word in alp:
            su=i.count(word)
            sum555.append(su)

        sum1="".join(str(x) for x in sum555)
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

        
        numbers = re.findall('\d+', adresosn[add-1])
        numbers=''.join(numbers)


        for i3 in sum2222:
            add1+=1
            i8=list(i3)
            su_buk = []
            
            numbers2 = re.findall('\d+', ad2[add1-1])
            numbers2=''.join(numbers2)
            
            if numbers==numbers2 : 
            
                for i10 in list(range(0,166)):
                    b0=int(i2[i10])-int(i8[i10])
                
                    if b0<0 :
                        b0=b0*(-1)
                    else:
                        b0=b0

                
                    su_buk.append(b0)
        
                all_sum=int(sum(su_buk))/166
                max_summ.append(all_sum)        
            else :
                all_sum=1
                max_summ.append(all_sum)  
                
        add166=0
        max_key=min(max_summ)
        for i9898 in max_summ:
 
            add166+=1
            if i9898==max_key:

                if ad2[add166-1][-1]=="А":

                    max_summ[add166-1]=max_key-0.01
                    max_key=min(max_summ) 
        
        max_keyend.append(round(max_key,3))
        ll=-1
        max_summ1=[]
        for i88 in max_summ:
            ll+=1
            if i88 !=max_key:
                max_summ1.append(ll)

            
        index=max_summ.index(max_key)
        adresosnend.append(zn1[add-1])
        adresosn2end.append(zn2[index])
    komment='Обработка '+ str(add111-1) +' адресов' + ' завершилась'
    output_div = document.querySelector("#output44")
    output_div.innerText =komment

    
    output_div = document.querySelector("#output1")
    output_div.innerText =adresosnend

    output_div = document.querySelector("#output2")
    output_div.innerText =max_keyend

    output_div = document.querySelector("#output3")
    output_div.innerText =adresosn2end


        

 








 







