from datetime import datetime, date, timedelta
import json

# function to decode 7-digit group code
# code format: xxxxxxx where x is the amount (0-9) of passangers in each category
# passanger types: aikuinen, lapsi, opiskelija, eläkeläinen, varusmies, siviilipalvelusmies, saattaja
# passnumbers list is in the same order

def group_decode(groupcode):
    passcount = str(groupcode)
    # VR passanger numbers in query string
    passnumbers = [84, 87, 85, 86, 89, 88, 92]
    counter = 0
    finalpasslist = []

    for x in passcount:
        if not passcount[counter] == "0":
            new_entry = {
                "passangertype": passnumbers[counter],
                "passamount": passcount[counter]
            }
            finalpasslist.append(new_entry)
        counter += 1
    return finalpasslist

# query string creation for price
# input arguments: departure station, end station, date, passangers (7-digit groupcode)
def price_query(fromSt, toSt, depDate, passangers):
    VRQ_start = "https://shop.vr.fi/onlineshop/JourneySearch.do?"           #fixed URL string
    VRQ_from = "basic.fromStationVR="+ fromSt + "&"                         # start station
    VRQ_to = "basic.toStationVR=" + toSt + "&"                              # end station
    VRQ1 = "basic.oneWay=true&"                                             # fixed str for future use, now just one way
    VRQ2 = "basic.returnTimeSelection=true&"                                # fixed str for future use
    VRQ3 = "basic.outwardTimeSelection=true&"                               # fixed str for future use
    VRQ4 = "basic.campaignCode=&"                                           # fixed str for future use
    VRQ5 = "basic.trainTypes=S&basic.trainTypes=IC&basic.trainTypes=IC2&basic.trainTypes=P&basic.trainTypes=H&basic.trainTypes=LOL&basic.trainTypes=LOC&basic.trainTypes=BUS&basic.trainTypes=LKB&basic.trainTypes=PL&basic.trainTypes=KLA&"
    VRQ6 = "basic.onlyDirect=false&"                                        # fixed str for future use
    VRQ7 = "basic.transferType=NORMAL&"                                     # fixed str for future use
    VRQ8 = "basic.changeOverStation=&"                                      # fixed str for future use
    VR_depDate = "basic.departureDate.date=" + depDate +"&"                 # departure date as dd.mm.yyyy
    VR_retDate = "basic.returnDate.date=" + depDate + "&"                   # now just one-way, so this is reserved for future

    # combine first part of the query string together
    VR_query_start = VRQ_start+VRQ_from+VRQ_to+VRQ1+VRQ2+VRQ3+VRQ4+VRQ5+VRQ6+VRQ7+VRQ8+VR_depDate+VR_retDate

    # passanger section
    # for-loop to build query string from given passanger group code

    passanger_list = group_decode(passangers)       # calling group_decode function -> returns dictionary
    categories = len(passanger_list)                # defines the iterations on for-loop -> amount of pass.categories
    VR_pass = ""                                    # reset query string

    for pass_num in range(0,categories):
        pass_type = str(passanger_list[pass_num]["passangertype"])
        pass_amount = str(passanger_list[pass_num]["passamount"])
        VR_pass += "basic.passengerNumbers%5B" + str(pass_num) + "%5D.passengerType=" + pass_type + "&basic.passengerNumbers%5B" + str(pass_num) + "%5D.passengerAmount=" + pass_amount + "&"

    # end section
    VR_end = "basic.departureDate.hours=05&basic.departureDate.mins=55&basic.returnDate.hours=05&basic.returnDate.mins=55&"

    VR_query_full = VR_query_start+VR_pass+VR_end

    return VR_query_full

# date check function

def checkDate(userdate, max_delta):
    datetest = userdate.replace(".", "")
    if not datetest.isnumeric():
        return False, "Väärä muoto. Käytä dd.mm.yyyy. Vain numeroita ja pisteitä."
    else:
        try:
            dateconvert = datetime.strptime(userdate, "%d.%m.%Y").date()
        except ValueError:
            return False, "Väärä muoto. Käytä dd.mm.yyyy"

        if dateconvert <= date.today():
            #print("Anna päivämäärä tulevaisuudesta.")
            return False, "Päivämäärän pitää olla tulevaisuudessa"

        elif dateconvert > date.today() + timedelta(days=max_delta):
            return False, "Liian kaukana tulevaisuudessa."


        return True, dateconvert
    #return dateconvert

def printResults():
    filehandle = open("results_file.json", "r")
    jsoncontent = filehandle.read()
    results_content = json.loads(jsoncontent)
    filehandle.close()

    print("Haun tulokset:")

    for x in results_content:
        print("PÄIVÄ: " + x)
        for y in results_content[x]:
            print("Lähtöaika " + results_content[x][y]["starttime"] + " Hinta " + results_content[x][y]["price"])






