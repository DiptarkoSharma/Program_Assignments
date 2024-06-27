import random
from rules import rules
import asyncio
from global_variable import api_token,group_chat_id
from telegram_bot_class import Telegram_Module
from telegram.error import TelegramError
from telegram.error import BadRequest
import sys

try:

    '''
        1. Import the rules module into the main program.
        2. Create a infinite while loop to read the sensor values.
        3. Have an option to break the while loop.
        4. From the rules dictionary, download the LL and UL of every parameter.
        5. Compare each of these parameters against the rules
        6. return a 1 or 0 flag depending on rule is violated or not.
        In globals.py, replace the below with actual value.
        api_token = '<<Your API Token>>'
        
        group_chat_id = '<<Your group chat ID>>'

    '''
    print(f'API{api_token},Grp Chat ID {group_chat_id}')
    telegram = Telegram_Module(api_token,group_chat_id)
    co2 = 0.00
    temp = 0.00
    humdty = 0.00
    sensor_values_dict = {}

    #created the function for the Co2 alarm detection
    def is_co2_voilated(co2):
        #CO2 rules definition
        co2_ll = round(float(rules['co2']['LL']),2)
        co2_ul = round(float(rules['co2']['UL']),2)
        #Is CO2 read by the sensor violating the Rule defined UL or LL?
        if co2 < co2_ll or co2 > co2_ul:
            print(f'CO2 Alarm : CO2 is :{co2}, Lower Limit is {co2_ll}, Uper Limit is {co2_ul}')
            return True
        else:
            print(f'CO2 value read is :{co2}')
            return False
    # created the function for the temp
    def is_temp_voilated(temp):
        #Temp  rules definition
        temp_ll = round(float(rules['temp']['LL']),2)
        temp_ul = round(float(rules['temp']['UL']),2)
        if temp >= temp_ll and  temp <= temp_ul:
            return True
        else:
            return False
    # created the function for the humidity
    def is_hum_voilated(hum):
        hum_ll = round(float(rules['humdty']['LL']),2)
        hum_ul = round(float(rules['humdty']['UL']),2)
        if hum >= hum_ll and  hum <= hum_ul :
            return True
        else:
            return False

    def main():

        while True:
            #Simulate a Factory environment where sensors are reading
            #Values of C02,Temp and Humidity
            co2 = round(random.uniform(3600,4000),2)
            temp = round(random.uniform(10,40),2)
            humdty = round(random.uniform(50,80),2)

            print(f'CO2:{co2}PPM,Temp:{temp}Deg Celsius,Humidity:{humdty}%')
            #Option to come out of the while loop.
            break_yes = input('Please select Y or N(Y/N)>')
            if break_yes == 'Y':
                break
            else:
                pass

            # Analysing the voilation of the co2
            violated_flg = is_co2_voilated(co2)
            print(is_co2_voilated(co2)) 
            if violated_flg == True:
                messg = f'CO2 levels violated. CO2 value is {co2}'
                print(f'CO2 levels violated. CO2 value is {co2}')
                print(f'Violation detected: ${messg}')
                asyncio.run(telegram.send_test_message(messg))
            else:
                pass
            
            violated_flg = is_temp_voilated(temp)
            print(is_temp_voilated(temp)) 
            if violated_flg == True:
                messg = f'Alert: Temp levels Violated. Temp value is {temp}'
                print(f'Violation detected: ${messg}')
                asyncio.run(telegram.send_test_message(messg))
            else:
                pass

            violated_flg = is_hum_voilated(humdty)
            print(is_hum_voilated(humdty)) 
            if violated_flg == True:
                messg = f'Alert: Humidity levels Violated. Humidity value is {humdty}'
                print(f'Violation detected: ${messg}')
                asyncio.run(telegram.send_test_message(messg))
            else:
                pass

    if __name__ == '__main__':
        main()
except ModuleNotFoundError as e:
    print(f'Sorry the module was not found. Exception is {e}')
    sys.exit(0)
except TelegramError as e:
    print(f' Exception is {e}')
    if isinstance(e, BadRequest):
        print("Handle BadRequest")

        

