from datetime import time
import sqlite3
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



def gun_entry_for_market():
    print("****GUN SHOP*****")
    print("\nMENU")
    print("1.Add to selection")
    print("2.View Logs")
    print("3.Quit")

    maker = input('Enter the maker of the gun: ')
    model_num = int(input('Enter the gun model number (legally required):' ))
    description = input('Enter the name of the firearm: ')
    production_year = input('Enter the production year: ')
    ammo_type = input('Enter the ammo type of the gun: ')
    mygun = GunInfo(maker,model_num,description,production_year,ammo_type)

    print(f"\nGun added to market: {mygun.get_maker()}, {mygun.get_model_num()}, {mygun.get_description()}, {mygun.get_production_date()}, {mygun.get_ammo_type()}")

gun_entry_for_market()    
    
