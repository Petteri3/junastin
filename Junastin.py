import sys
import vr_functions as vr
import requests
import json
from datetime import timedelta
import os.path
from bs4 import BeautifulSoup

answer_pending = True
argslist = ["", "Lähtöasema", "Kohdeasema", "Päivämäärä", "Montako päivää eteenpäin", "Ryhmän kokoonpano"]

argcount = len(sys.argv)



# check the date format
if argcount == 6:
    # check that passangercode is 7 numbers
    if not len(sys.argv[5]) == 7:
        print("Väärä matkustajakoodi. Pitää olla 7 numeroa pitkä.")
        sys.exit()
    elif not sys.argv[5].isnumeric():
        print("Väärä matkustajakoodi. Pitää olla 7 numeroa, vain numeroita.")
        sys.exit()
    dateCheck = sys.argv[3]
    date_ok, dateformatted = vr.checkDate(dateCheck, 100)
    if not date_ok:
        print(dateformatted)
        sys.exit()
    else:
        print("Päivämäärä ok. Hakuehtojen määrä ok.")

# print general help text and if there is previous search JSON present, print it too
else:
    print("Lisää tietoja kaivataan. Anna parametrit: lähtöasema, kohdeasema, päivämäärä, montako päivää haetaan eteenpäin sekä ryhmäkoodi")
    print("Ryhmäkoodi on 7 numeroa, joista jokainen kertoo montako matkustajaa on kussakin kategoriassa.")
    print("Ryhmäkoodin järjestys: \n aikuinen \n lapsi \n opiskelija \n eläkeläinen \n varusmies \n siviilipalvelusmies \n saattaja")
    print("Esimerkkikoodi: 1210001 -> aikuinen, kaksi lasta, opiskelija ja avustaja")
    if os.path.isfile("results_file.json"):
        print("Edellisen haun tulokset:")
        vr.printResults()
    sys.exit()



# If everything is fine in the arguments, print them

print("Hakutietosi ovat:")
for x in range(1, argcount):
    print(f"{argslist[x]}: {sys.argv[x]} ")

# define argument based variables for the main loop
start_station = sys.argv[1]
end_station = sys.argv[2]
search_date = sys.argv[3]
search_days = int(sys.argv[4])
group = sys.argv[5]

# start main loop here

results_dict = {}   # reset results dictionary
for days in range(0,search_days):
    query_date = dateformatted+timedelta(days=days)
    vrdate = query_date.strftime("%d.%m.%Y")

    print("Haetaan päivä: "+ vrdate)

    query_URL = vr.price_query(start_station, end_station, vrdate, group)
    response = requests.get(query_URL)
    soup = BeautifulSoup(response.text, "html.parser")

    dateindex = str(vrdate)

    # create key for each date
    results_dict[dateindex] = {}
    for everytime in soup.find_all("tr", class_="tripOption"):
        starttime = everytime.find("td", class_="tripStartDomestic").text
        endtime = everytime.find("td", class_="tripEndDomestic").text
        durat = everytime.find("td", class_="tripDurationDomestic tripTrainTypesDurationFont").text
        price = everytime.find("div", class_="priceBoxPrice").text.strip()

        results_dict[dateindex][starttime] = {
                                          "starttime" : starttime,
                                          "endtime" : endtime,
                                          "durat" : durat,
                                          "price" : price
                                      }

print("Kirjoitetaan JSON")
jsoncontent = json.dumps(results_dict)
filehandle = open("results_file.json", "w")
filehandle.write(jsoncontent)
filehandle.close()

print("Valmis")

# show results from JSON
vr.printResults()


