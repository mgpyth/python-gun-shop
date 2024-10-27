import sqlite3
import sys
import art

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
    try:
        maker = input('Enter the maker of the gun: ')
        model_num = int(input('Enter the gun model number (legally required):' ))
        description = input('Enter the name of the firearm: ')
        production_year = input('Enter the production year: ')
        ammo_type = input('Enter the ammo type of the gun: ')
    except ValueError as e:
        print("Enter the proper value")
    except sqlite3.IntegrityError:
        print("Record was not found.")
    finally:
        print("Gun data added.")
    mygun = GunInfo(maker,model_num,description,production_year,ammo_type)

    print(f"\nGun added to market: Manufactuer:{mygun.get_maker()}, Serial:{mygun.get_model_num()}, Model:{mygun.get_description()}, ProductionDate:{mygun.get_production_date()}, AmmoType:{mygun.get_ammo_type()}")

    cur.execute('''INSERT INTO Guns (GunMaker,ModelNum,Description,ProductionDate,AmmoType)
                     VALUES (?,?,?,?,?)''',
                            (maker,model_num,description,production_year,ammo_type))
    conn.commit()
##    conn.close()

def viewing_guns_in_stock(conn,cur):
##    conn= sqlite3.connect('gunshop.db')
    cur.execute("SELECT Gunmaker,Description,AmmoType FROM guns")
    gunshop = cur.fetchall()
    print("Gun manufactuers in stock")
    for gun in gunshop:
        print('\n','Manufactuer:',gun[0])
        print('\n','Model:',gun[1])
        print('\n','Ammotype:',gun[2])
##    conn.close()

def delete_gun(conn,cur):
    try:
        removal = input('Enter gun name to delete: ')
    except ValueError as e:
        print("No integer type,enter gun name instead")
    cur.execute('DELETE FROM guns WHERE GunMaker = ?',(removal,))
    conn.commit()
##    conn.close()

def search_filter(conn,cur):
    try:
##        conn = sqlit3.connect('gunshop.db')
        brand_search = input("Enter the criteria to search by[BRAND]: ")
    except ValueError as e:
        print("Incorrect value type.")
    finally:
        print("Item with matching attributes found.")
    cur.execute("SELECT GunMaker FROM guns WHERE GunMaker = ?",(brand_search,))
    result = cur.fetchone()
##
##    if result:
####        print(f'Brand found:{result[0]}')
####        return result[0]
##    else:
##        print('nothing')
        
    
    
                
    
def main():
    from art import text2art
    Art =text2art("GUNSHOP")
    print(Art)
    conn,cur = create_table()
    print("****GUN SHOP*****")
    print("\nMENU")
    print("1.Add to selection")
    print("2.View Guns in stock")
    print("3.Delete Gun entries")
    print("4.Search filter")
    print("5.Quit")
    
    selection = int(input("Enter a selection: "))
    if selection  == 1:
        gun_entry_for_market(cur,conn)
    elif selection == 2:
        viewing_guns_in_stock(conn,cur)
    elif selection == 3:
        delete_gun(conn,cur)
    elif selection == 4:
         search_filter(conn,cur)
    elif selection == 5:
        exit()
main()
