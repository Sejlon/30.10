predvolby = {'420':'Česká republika', '32':'Belgie', '359':'Bulharsko', '385':'Chorvatsko', '357':'Kypr', '421':'Slovensko', '39':'Itálie', '358':'Finsko', '33':'Francie', '48':'Polsko', '353':'Irsko','36':'Maďarsko', '356':'Malta', '49':'Německo', '31':'Nizozemsko', '386':'Slovinsko', '34':'Španělsko', '46':'Švédsko', '30':'Řecko', '40':'Rumunsko','351':'Portugalsko', '45':'Dánsko', '372':'Estonsko', '371':'Lotyšsko', '370':'Litva', '43':'Rakousko', '352':'Lucembursko'}
pocetstatu=[]

soubor = open("telefonni_cisla.txt", mode="r",  encoding="utf-8")
x=soubor.read()
y=x.split("\n")
del y[-1]
soubor.close()

for i in y:
    type(i) == str
    if i[0] !="0" and i[0] !="+":
        pocetstatu.append(predvolby.get("420"))
    elif i[0] =="0":
        for staty in predvolby:
            if staty in i[2:5]:
                pocetstatu.append(predvolby.get(staty))
                print(pocetstatu)
            elif staty in i[2:4]:
                pocetstatu.append(predvolby.get(staty))
                print(pocetstatu)
    elif i[0] =="+":
        for staty in predvolby:
            if staty in i[1:4]:
                pocetstatu.append(predvolby.get(staty))
                print(pocetstatu)
            elif staty in i[1:3]:
                pocetstatu.append(predvolby.get(staty))
print("Pobočky máme v následujících zemích")
for i in predvolby.values():
    vysledne_cislo=pocetstatu.count(i)
    print(i,":",vysledne_cislo)