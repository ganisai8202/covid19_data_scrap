import requests
from bs4 import BeautifulSoup
import csv

link='https://www.worldometers.info/coronavirus/'
page=requests.get(link)
print(page)
html=page.content
soup=BeautifulSoup(html,'lxml')
trs=soup.findAll('tr')
data_list=[]
for tr in trs:
    data_dict={}
    tds=tr.findAll('td')
    if(len(tds)!=9):
        continue
    data_dict['country']=tds[0].text.strip()

    tot_case=tds[1].text.strip()
    data_dict['tot_case']=int(tot_case.replace(',','')) if tot_case else 0

    new_case=tds[2].text.strip()
    data_dict['new_case']=int(new_case.replace(',','')) if new_case else 0

    tot_death=tds[3].text.strip()
    data_dict['tot_death']=int(tot_death.replace(',','')) if tot_death else 0

    new_death=tds[4].text.strip()
    data_dict['new_death']=int(new_death.replace(',','')) if new_death else 0

    tot_recover=tds[5].text.strip()
    data_dict['tot_recover']=int(tot_recover.replace(',','')) if tot_recover else 0

    acti_case=tds[6].text.strip()
    data_dict['acti_case']=int(acti_case.replace(',','')) if acti_case else 0

    critical=tds[7].text.strip()
    data_dict['critical']=int(critical.replace(',','')) if critical else 0

    case_per_mil=tds[8].text.strip()
    data_dict['case_per_mil']=float(case_per_mil.replace(',','')) if case_per_mil else 0

    data_list.append(data_dict)

f=open('corona_stats.csv','w')
writer=csv.DictWriter(
                f,fieldnames=['country','tot_case','new_case','tot_death',
                            'new_death','tot_recover','acti_case','critical','case_per_mil'])
writer.writeheader()
writer.writerows(data_list)
f.close()
