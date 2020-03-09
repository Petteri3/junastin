# junastin
## Command line Python script to query VR (Finnish railway company) website for schedules with prices

This command line script is designed for quick retrieval of schedules for certain passanger groups. Therefore is is using a "passanger code" as one command line argument.
Script must have 5 command line arguments:
1. Start station
2. End station
3. Date in dd.mm.yyyy format
4. How many days to search forward (keep this low to not query VR servers too much :)
5. Group code

Group code format:
1st number: amount of adults
2nd number: amount of children
3rd number: amount of students
4th number: amount of students
5th number: amount of conscripts
6th number: amount of non-military service person
7th number: amount of assistant (to a disabled traveler)

Example group code: 1210001 (one adult, two children, one student, one assistant)

Using:
```
python3 junastin startstation endstation date daysforward groupcode 
```

Example:
```
python3 junastin Rovaniemi Helsinki 23.4.2020 3 1210001
```

Using without arguments:
```
python3 junastin
```
Without arguments script prints results of a previous search if present

