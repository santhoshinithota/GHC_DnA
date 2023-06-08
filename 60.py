import subprocess as sp
import pymysql
import pymysql.cursors

def Diseases_Data():
    query = "SELECT * FROM DISEASE NATURAL JOIN TYPE_NAME;"
    print(query)
    cur.execute(query)
    con.commit()
    print("Data has been retrieved")
    return

def Health_Stats_Data():
    query = "SELECT * FROM HEALTH_STATISTICS NATURAL JOIN IDS_OF_COUNTRIES_AFFECTED;"
    print(query)
    cur.execute(query)
    con.commit()
    print("Data has been retrieved")
    return

def Offices_Data():
    query = "SELECT * FROM BRANCHES NATURAL JOIN LOCATION_OF_BRANCH;"
    print(query)
    cur.execute(query)
    con.commit()
    print("Data has been retrieved")
    return

def Max_Duration():
    query = "SELECT PROGRAM_NAME, DURATION FROM PROGRAM_TIME WHERE DURATION IN(SELECT MAX(DURATION) FROM PROGRAM_TIME);"
    print(query)
    cur.execute(query)
    con.commit()
    print("Data has been retrieved")
    return

def Sum_Deaths():
    query1 = "CREATE VIEW temp AS SELECT NO_OF_PEOPLE_AFFECTED - NO_OF_PEOPLE_RECOVERED AS Death FROM HEALTH_STATISTICS;"
    query2 = "SELECT SUM(Death) FROM temp;"
    query3 = "DROP VIEW temp;"
    # print(query)
    cur.execute(query1)
    cur.execute(query2)
    cur.execute(query3)
    con.commit()
    print("Data has been retrieved")
    return

def Sum_Local_Organisations():
    query = "SELECT SUM(NO_OF_LOCAL_ORGANIZATIONS) FROM BRANCHES;"
    print(query)
    cur.execute(query)
    con.commit()
    print("Data has been retrieved")
    return

def Disease_finder_by_name():
    to_find = input("Type in part of the Disease name: ")
    query = "SELECT DISEASE Name FROM BRANCHES WHERE DISEASE_NAME LIKE '%%s%';" % (to_find)
    print(query)
    cur.execute(query)
    con.commit()
    print("Data has been retrieved")
    return

def Representative_finder():
    to_find = input("Type a string that comes at the end of the representative's name: ")
    query = "SELECT NAME FROM MEMBERS WHERE NAME LIKE '%%s';" % (to_find)
    print(query)
    cur.execute(query)
    con.commit()
    print("Data has been retrieved")
    return

def Country_finder():
    to_find = input("Type a string that comes at the beginning of the country's name: ")
    query = "SELECT COUNTRY_NAME FROM MEMBERS WHERE COUNTRY_NAME LIKE '%s%';" % (to_find)
    print(query)
    cur.execute(query)
    con.commit()
    print("Data has been retrieved")
    return

def Researches_with_status():
    to_find = int(input("Enter the threashold for status of completion: "))
    query = "SELECT SERIAL_NO FROM BIOMEDICAL_RESEARCHES WHERE STATUS_OF_COMPLETION >= %d;" % (to_find)
    print(query)
    cur.execute(query)
    con.commit()
    print("Data has been retrieved")
    return

def Branches_with_organisations():
    to_find = int(input("Enter the threashold of number of local organizations: "))
    query = "SELECT BRANCH_ID FROM BRANCHES WHERE NO_OF_TOTAL_ORGANIZATIONS >= %d;" % (to_find)
    print(query)
    cur.execute(query)
    con.commit()
    print("Data has been retrieved")
    return

def DiseaseID_mortality():
    to_find = int(input("Enter the threashold for mortality: "))
    query = "SELECT DISEASE_ID FROM BRANCHES WHERE MORTALITY_RATE >= %d;" % (to_find)
    print(query)
    cur.execute(query)
    con.commit()
    print("Data has been retrieved")
    return

def Rnaught_recoveries():
    query = "SELECT RNAUGHT FROM DISEASE, HEALTH_STATISTICS WHERE NO_OF_PEOPLE_RECOVERED IN(SELECT MAX(NO_OF_PEOPLE_RECOVERED) FROM HEALTH_STATISTICS);"
    print(query)
    cur.execute(query)
    con.commit()
    print("Data has been retrieved")
    return

def Mortality_minDoc():
    query = "SELECT COUNTRY_ID, MORTALITY_RATE FROM MEDICAL_INFRASTRUCTURE, HEALTH_STATISTICS WHERE NO_OF_DOCTORS IN(SELECT MAX(NO_OF_DOCTORS) FROM MEDICAL_INFRASTRUCTURE);"
    print(query)
    cur.execute(query)
    con.commit()
    print("Data has been retrieved")
    return

def Representative_maxLocal():
    query = "SELECT FIRST_NAME, LAST_NAME FROM BIOMEDICAL_RESEARCHES, BRANCHES WHERE NO_OF_LOCAL_ORGANIZATIONS IN(SELECT MAX(NO_OF_LOCAL_ORGANIZATIONS) FROM BRANCHES);"
    print(query)
    cur.execute(query)
    con.commit()
    print("Data has been retrieved")
    return

def AddingPolicies():
    try:
        row = {}
        print("Enter new Policy's details: ")
        row["PROGRAM_NO"] = int(input("Program Number: "))
        row["PROGRAM_NAME"] = input("Program Name: ")
        row["PROGRAM_TYPE"] = input("Program Type: ")
        row["DURATION"] = input("Duration: ")
        row["LOCATIONS"] = input("Locations: ")
        row["DISEASE_ID"] = input("Disease ID: ")

        query1 = "INSERT INTO LOCATIONS(Name) VALUES('%s')" % (row["LOCATIONS"])
        query2 = "INSERT INTO HEALTH_POLICIES(PROGRAM_NO, PROGRAM_NAME, LOCATION_ID, DISEASE_ID)VALUES('%d','%s','%d','%d')"%(row["PROGRAM_NO"], row["PROGRAM_NAME"], "NULL", row["DISEASE_ID"])
        query3 = "INSERT INTO PROGRAM_TIME(PROGRAM_NAME, DURATION, PROGRAM_TYPE)VALUES('%s','%d','%s')"%(row["PROGRAM_NAME"], row["DURATION"], row["PROGRAM_TYPE"])
        query4 = "UPDATE Health Policies SET Location ID IN (SELECT Location ID FROM Locations WHERE Name='%s')"%(row["Locations"])
        
        # print(query)
        cur.execute(query1)
        cur.execute(query2)
        cur.execute(query3) 
        cur.execute(query4)       
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def AddMembers():
    try:
        row = {}
        print("Enter new Member's details: ")
        row["COUNTRY_ID"] = int(input("Country ID: "))
        row["COUNTRY_NAME"] = input("Country Name: ")
        row["NAME"] = input("Head's Name: ")
        row["YEAR_OF_TERM"] = int(input("Year Of Term: "))
        row["DESIGNATION"] = input("Designation: ")
        row["COUNTRY_ID"] = int(input("Disease ID: "))

        query1 = "INSERT INTO Members(COUNTRY_ID, COUNTRY_NAME, NAME,YEAR_OF_TERM, DESIGNATION, COUNTRY_ID )VALUES('%d','%s','%s','%d','%s','%d')"%(row["COUNTRY_ID"], row["COUNTRY_NAME"], row["NAME"], row["YEAR_OF_TERM"], row["DESIGNATION"], row["COUNTRY_ID"])
        
        # print(query)
        cur.execute(query1)      
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def AddDisease():
    try:
        row = {}
        print("Enter new Disease's details: ")
        row["DISEASE_ID"] = int(input("Disease ID: "))
        row["DISEASE_NAME"] = input("Disease Name: ")
        row["RNAUGHT"] = input("RNaught: ")
        row["DISEASE_TYPE"] = input("Disease Type: ")

        query1 = "INSERT INTO DISEASE(DISEASE_ID, DISEASE_NAME, RNAUGHT )VALUES('%d','%s','%d')"%(row["DISEASE_ID"], row["DISEASE_NAME"], row["RNAUGHT"])
        query2 = "INSERT INTO TYPE_NAME(DISEASE_NAME, DISEASE_TYPE)VALUES('%s','%s')"%(row["DISEASE_NAME"], row["DISEASE_TYPE"])
        print(query1)
        print(query2)
        cur.execute(query1) 
        cur.execute(query2)      
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def AddingInfrastructure():
    try:
        row = {}
        print("Enter new Infrastructure's details: ")
        row["COUNTRY_ID"] = int(input("Country ID: "))
        row["NO_OF_HOSPITALS"] = input("No. Of Hospitals: ")
        row["NO_OF_DOCTORS"] = input("No. Of Doctors: ")
        row["NO_OF_EQUIPMENTS"] = input("No. Of Equipments: ")
        row["SERIAL_NO"] = input("Serial No.: ")

        query1 = "INSERT INTO NUMBER_OF_EQUIPMENT(NUMBER_OF_EQUIPMENTS) VALUES('%d')" % (row["NUMBER_OF_EQUIPMENTS"])
        query2 = "INSERT INTO MEDICAL_INFRASTRUCTURE(COUNTRY_ID, NO_OF_HOSPITALS, NUMBER_OF_DOCTORS, NUMBER_ID, SERIAL_NO)VALUES('%d','%d','%d','%d','%d')"%(row["COUNTRY_ID"], row["NO_OF_HOSPITALS"], row["NUMBER_OF_DOCTORS"], "NULL", row["SERIAL_NO"])
        query4 = "UPDATE MEDICAL_INFRASTRUCTURE SET NUMBER_ID IN (SELECT NUMBER_ID FROM NUMBER_OF_EQUIPMENT WHERE NUMBER_OF_EQUIPMENTS='%d')"%(row["NUMBER_OF_EQUIPMENTS"])
        
        # print(query)
        cur.execute(query1)
        cur.execute(query2)
        cur.execute(query4)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def RepresentativeChange():
    try:
        print("Enter new Representative: ")
        Representative = input("Write the name of New Representative: ")
        ID = int(input("Enter the country ID: "))
        query = "UPDATE MEMBERS SET NAME='%s' WHERE Country_ID='%d'"%(Representative, ID)
        cur.execute(query)
        con.commit()
        print("Updated")
    except Exception as e:
        con.rollback()
        print("Failed to update into database")
        print(">>>>>>>>>>>>>", e)

def LocationChange():
    try:
        print("Enter new Location: ")
        Location = input("Write the name of New Location: ")
        ID = int(input("Enter the Branch ID: "))
        query = "UPDATE BRANCHES SET LOCATION_ID='%s' WHERE BRANCH_ID='%d'"%(Location, ID)
        cur.execute(query)
        con.commit()
        print("Updated")
    except Exception as e:
        con.rollback()
        print("Failed to update into database")
        print(">>>>>>>>>>>>>", e)

def CompletionChange():
    try:
        print("Updating the status of completion: ")
        Status = int(input("Write the name of New Location: "))
        ID = int(input("Enter the Serial Number: "))
        query = "UPDATE BIOMEDICAL_RESEARCHES SET STATUS_OF_COMPLETION='%d' WHERE SERIAL_NO='%d'"%(Status, ID)
        cur.execute(query)
        con.commit()
        print("Updated")
    except Exception as e:
        con.rollback()
        print("Failed to update into database")
        print(">>>>>>>>>>>>>", e)

def VaccineChange():
    try:
        print("Updating the Vaccination Status: ")
        Status = int(input("Write the new Vaccine's Status: "))
        Type = input("Enter the Disease Type: ")
        query = "UPDATE HEALTH_STATISTICS SET VACCINATION_STATUS='%d' WHERE DISEASE_TYPE='%s'"%(Status, Type)
        cur.execute(query)
        con.commit()
        print("Updated")
    except Exception as e:
        con.rollback()
        print("Failed to update into database")
        print(">>>>>>>>>>>>>", e)

def PolicyDeletion():
    try:
        print("Deleting an expired policy: ")
        query = "DELETE FROM HEALTH_POLICIES, PROGRAM_TIME WHERE PROGRAM_NAME IN (SELECT PROGRAM_NAME FROM PROGRAM_TIME WHERE DURATION IN (SELECT YEAR(CURDATE()-2020)));"
        cur.execute(query)
        con.commit()
        print("All expired policies deleted")
    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)

def CountryRemoval():
    try:
        print("Removing a country: ")
        ID = int(input("Write the Country's ID: "))
        query = "DELETE FROM MEMBERS, BIOMEDICAL_RESEARCHES, COUNTRY_LOCATION, Implement WHERE COUNTRY_ID='%d'"%(ID)
        cur.execute(query)
        con.commit()
        print("Deletion successfull")
    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)

def ResearchRemoval():
    try:
        print("Removing a biomedical research: ")
        query = "DELETE FROM MEDICAL_INFRASTRUCTURE, BIOMEDICAL_RESEARCHES WHERE SERIAL_NO IN(SELECT SERIAL_NO FROM BIOMEDICAL_RESEARCHES WHERE STATUS_OF_COMPLETION=100)"
        cur.execute(query)
        con.commit()
        print("Deletion successfull")
    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)
def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        Diseases_Data()
    elif(ch == 2):
        Health_Stats_Data()
    elif(ch == 3):
        Offices_Data()
    elif(ch == 4):
        Max_Duration()
    elif(ch == 5):
        Sum_Deaths()
    elif(ch == 6):
        Sum_Local_Organisations()
    elif(ch == 7):
        Disease_finder_by_name()
    elif(ch == 8):
        Representative_finder()
    elif(ch == 9):
        Country_finder()
    elif(ch == 10):
        Researches_with_status()
    elif(ch == 11):
        Branches_with_organisations()
    elif(ch == 12):
        DiseaseID_mortality()
    elif(ch == 13):
        Rnaught_recoveries()
    elif(ch == 14):
        Mortality_minDoc()
    elif(ch == 15):
        Representative_maxLocal()
    elif(ch == 16):
        AddingPolicies()
    elif(ch == 17):
        AddMembers()
    elif(ch == 18):
        AddDisease()
    elif(ch == 19):
        AddingInfrastructure()
    elif(ch == 20):
        RepresentativeChange()
    elif(ch == 21):
        LocationChange()
    elif(ch == 22):
        CompletionChange()
    elif(ch == 23):
        VaccineChange()
    elif(ch == 25):
        PolicyDeletion()
    elif(ch == 26):
        CountryRemoval()
    elif(ch == 28):
        ResearchRemoval()
    elif(ch == 24):
        return
    elif(ch == 27):
        return
    else:
        print("Error: Invalid Option")


# Global
while(1):
    tmp = sp.call('clear', shell=True)

    # Can be skipped if you want to hardcode username and password
    username = input("Username: ")
    password = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server
        con = pymysql.connect(host='localhost',
                              port=30306,
                              user="root",
                              password="password",
                              db='COMPANY',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)

                # 1. Queries
                # 1.1 Selection
                print("1. Retrieving data of all the diseases")
                print("2. Retrieving entire data about world health's stats")
                print("3. Retrieving data of all the offices with their data")
                # 1.2 Aggregate
                print("4. Finding maximum duration among all the health policies with the name of the policy")
                print("5. Finding sum of all the deaths caused by all the diseases")
                print("6. Finding sum of all local organisations of all brannches")
                # 1.3 Search
                print("7. List of all diseases having 'ler' between their name")
                print("8. Number of all representatives with name ending with 'an'")
                print("9. List of all the countries whose name starts with 'Ans'")
                # 1.4 Projection
                print("10. List of all Bio-Medical researches with status of completion >= 90%")
                print("11. List of all the branches in a particular country with more than 30 local organizations")
                print("12. List of all Disease IDs with more than 0.6 mortality rate")
                
                # 2. Analysis
                print("13. R0 value of the disease with maximum number of recoveries")
                print("14. Mortality rate of the country with minimum number of doctors/nurses")
                print("15. Representative of the country with maximum numbers of local organizations")

                # 3. Modification
                # 3.1 Insertion
                print("16. Adding any new policy being deployed by some country")
                print("17. Adding any new members who wants to join GHC")
                print("18. Inserting any new disease being found")
                print("19. Adding new branches and infrastructures formed.")
                # 3.2 Update
                print("20. Change in representative of any country")
                print("21. Change in location of any branch")
                print("22. Change in status of completion of any Bio-Medical research")
                print("23. Updating the percentage of vaccination status of a disease")
                print("24. Updating member of the executive boards and secretariats")
                # 3.3 Deletion
                print("25. Deleting any policy after its expiry")
                print("26. Removing any country who wants to leave GHC group")
                print("27. Removing member of an executive board")
                print("28. Removing the research that has been completed")

                print("29. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 29:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
