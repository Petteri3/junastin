# junastin
## Command line Python script to query VR (Finnish railway company) website for train schedules with prices (also for special passangers). It is possible to search for several days forward to find best price.

This command line script is designed for quick query of schedules&prices for certain passanger groups. Therefore it is using a "group code" as one command line argument.

Script must have 5 command line arguments:
1. Start station
2. End station
3. Date in dd.mm.yyyy format
4. How many days to search forward (keep this low to not query VR servers too much :)
5. 7-digit Group code

Group code format - amount can be 0-9 per each passanger type:
1st number: amount of adults
2nd number: amount of children
3rd number: amount of students
4th number: amount of pensioners
5th number: amount of conscripts
6th number: amount of non-military service person
7th number: amount of assistant (to a disabled traveler)

Example group code: 1210001 (one adult, two children, one student, one assistant)

Using:
```
python3 Junastin.py startstation endstation date daysforward groupcode 
```

Example:
```
python3 Junastin.py Rovaniemi Helsinki 23.4.2020 3 1210001
```

Using without arguments:
```
python3 Junastin.py
```
Without arguments script prints results of a previous search if (JSON file) present

NOTE: There is no check/test for the station names. If the station doesn't exist or is mistyped the script still runs but gives no results.

# Ohjeet suomeksi
## Junastin on python skripti jolla voi hakea VR:n sivuilta aikataulut hintoineen, myös erityisryhmille kuten saattajat. Mahdollisuus hakea useampi päivä eteenpäin kerralla ja löytää näin paras hinta.

Skriptille pitää antaa 5 argumenttia:
1. Aloitusasema
2. Pääteasema
3. Päivämäärä dd.mm.yyyy -muodossa
4. Kuinka monta päivää eteenpäin haetaan (pidä tämä luku pienenä ettet kuormita liikaa VR:n palvelimia ja haku ei kestä ikuisuuksia :)
5. 7-numeroinen ryhmän koodi

Ryhmän koodi muodostuu numeroista, kutakin matkustajatyyppiä voi olla 0-9 kappaletta:
1.numero: aikuisten määrä
2.numero: lasten määrä
3.numero: opiskelijoiden määrä
4.numero: eläkeläisten määrä
5.numero: varusmiesten määrä
6.numero: siviilipalvelusmiesten määrä
7.numero: avustajien määrä

Esimerkki ryhmäkoodista: 1210001 (aikuinen, kaksi lasta, opiskelija, avustaja)

Käyttö:
```
python3 Junastin.py aloitusasema pääteasema päiväys päivienmäärä ryhmäkoodi 
```

Esimerkki:
```
python3 Junastin.py Rovaniemi Helsinki 23.4.2020 3 1210001
```

Käyttö ilman argumentteja:
```
python3 Junastin.py
```
Ilman argumentteja skripti näyttää edellisen haun tulokset (jos haku tehty ja JSON-tiedosto tallessa)

HUOM. Skripti ei osaa testata asemien nimiä. Jos haettua asemaa ei ole tai siinä on virhe, skripti ajetaan, mutta tuloksia ei tule. Tarkista asemien nimet tarvittaessa VR:n omalla hakusivulla.

