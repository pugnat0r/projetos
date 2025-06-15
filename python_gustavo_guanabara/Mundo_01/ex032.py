from datetime import date

year = int(input("Diga um Ano para analisar, digite 0 para analisar o ano atual! "))

if year == 0:
    year = date.today().year

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Ano {} bissexto'.format(year))
else:
    print("Ano {} não é bissexto!! ".format(year))