"""
programmet tar inn max_temperatures_per_month.csv og deler den inn i ordbok der
keyen er månedene og valuen er temperaturen
"""
ordbok= {} #lager ordbok

def prosedyre(fil): #lager prosedyre
    for linje in fil: #for loop som spliter og setter inn i ordboken
        biter=linje.split(",")
        månedene=biter[0]
        høyeste_temp=biter[1]
        ordbok[månedene]=høyeste_temp #månedene er keys og høyeste temp er value
    return ordbok



min_fil=open("max_temperatures_per_month.csv") #åpner filen
print(prosedyre(min_fil)) #kjører prosedyren med filen som parammeter


#her klarte jeg ikke å dele inn sånn at jeg fikk 12 ordboker (en for hver av månedeene, men 30/31 valuer)
#istedet får jeg 365 ordbøker
fil2=open("max_daily_temperature_2018.csv")
for linje in fil2:
    biter2=linje.split(",")
    månedene=biter2[0]
    dag=biter2[1]
    temp=biter2[2]
    print(biter2)
