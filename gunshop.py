
import sqlite3
import sys
import pyfiglet


# creating db

def create_table():
    conn = sqlite3.connect('gunshop.db')
    cur = conn.cursor()
    cur.execute(''' CREATE TABLE IF NOT EXISTS Guns (GunMaker TEXT PRIMARY KEY NOT NULL,
                                    ModelNum INTEGER,
                                    Description TEXT,
                                    ProductionDate INTEGER,
                                    AmmoType TEXT) ''')
    conn.commit()
##    conn.close()

    return conn,cur

class GunInfo:

    def __init__(self,maker,model_num,description,production_date,ammo_type):

        self.__maker = maker
        self.__model_num = model_num
        self.__description = description
        self.__production_date = production_date
        self.__ammo_type = ammo_type

    def get_maker(self):
        return self.__maker

    def set_maker(self,maker):
        self.__maker = maker

    def get_model_num(self):
        return self.__model_num

    def set_model_num(self,model_num):
        self.__model_num = model_num


    def get_description(self):
        return self.__description

    def set_description(self,description):
        self.__description = descirption

    def get_production_date(self):
        return self.__production_date

    def set_production_date(self,production_date):
        self.__production_date = production_date

    def get_ammo_type(self):
        return self.__ammo_type

    def set_ammo_type(self,ammo_type):
        self.__ammo_type = ammo_type



def gun_entry_for_market(cur,conn):
##    print("****GUN SHOP*****")
##    print("\nMENU")
##    print("1.Add to selection")
##    print("2.View Logs")
##    print("3.Quit")
##    selection = int(input("Enter a selection: "))
    try:
        maker = input('Enter the maker of the gun: ')
        model_num = int(input('Enter the gun model number (legally required):' ))
        description = input('Enter the name of the firearm: ')
        production_year = input('Enter the production year: ')
        ammo_type = input('Enter the ammo type of the gun: ')
    except ValueError as e:
        print("Enter the proper value")
    finally:
        print("Gun data added.")
    mygun = GunInfo(maker,model_num,description,production_year,ammo_type)

    print(f"\nGun added to market: {mygun.get_maker()}, {mygun.get_model_num()}, {mygun.get_description()}, {mygun.get_production_date()}, {mygun.get_ammo_type()}")

    cur.execute('''INSERT INTO Guns (GunMaker,ModelNum,Description,ProductionDate,AmmoType)
                     VALUES (?,?,?,?,?)''',
                            (maker,model_num,description,production_year,ammo_type))
    conn.commit()
##    conn.close()

def viewing_guns_in_stock(conn,cur):
    cur.execute("SELECT Gunmaker FROM guns")
    gunshop = cur.fetchall()
    print("Gun manufactuers in stock")
    for gun in gunshop:
        print('\n',gun[0])
    

    
def main():
    conn,cur = create_table()
    txt = pyfiglet.figlet_format("GUN SHOP",font = "larry3d")
    print(txt)
                                 
    print("****GUN SHOP*****")
    print("\nMENU")
    print("1.Add to selection")
    print("2.View Guns in stock")
    print("3.Quit")
    selection = int(input("Enter a selection: "))
    if selection  == 1:
        gun_entry_for_market(cur,conn)
    elif selection == 2:
        viewing_guns_in_stock(conn,cur)
    elif selection == 3:
        exit()
main()

