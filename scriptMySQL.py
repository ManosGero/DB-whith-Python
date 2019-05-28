import mysql.connector

def serching():
    inputWorld = input ("give a word in English and press Enter: ")
    con = mysql.connector.connect(user="ardit700_student",
                                  password= "ardit700_student",
                                  host = "108.167.140.122",
                                  database = "ardit700_pm1database"
                                  )
    cursor = con.cursor()
    query = cursor.execute(
        "SELECT * FROM Dictionary WHERE Expression = '%s'"%(inputWorld))
    results = cursor.fetchall()
    if results:
        for result in results:
            print(result[1])
    else:
        print("We couldn't find any results about that.")


def view():
    con = mysql.connector.connect(user="ardit700_student",
                                  password= "ardit700_student",
                                  host = "108.167.140.122",
                                  database = "ardit700_pm1database"
                                  )
    cursor = con.cursor()
    query = cursor.execute("SELECT * FROM Dictionary")
    results = cursor.fetchall()
    print(results)

view()     
