import random
from rules import rules
import asyncio
from global_variable import api_token,group_chat_id
from telegram_class_bot import Telegram_Module
from telegram.error import TelegramError
from telegram.error import BadRequest
import sys
'''
1.import the rules module into the main program.
2.create a infinite while loop to read the sensor values.
3.have an option to break the while loop.
4.from the rules dictionary ,download the LL and UL of every parameter.
5.compare each of these parameters against the rules.
6.return a 1 or 0 flag depending on rule is violated or not.
'''
print(f'API{api_token},Grp chat Id {group_chat_id}')
telegram=Telegram_Module(api_token,group_chat_id)
co2=0.00
temp=0.00
humdty=0.00
sensor_values_dict={}
def is_co2_voilated(co2):
    co2_ll=round(float(rules['co2']['LL']),2)
    co2_ul=round(float(rules['co2']['UL']),2)
    if co2<co2_ll or co2>co2_ul:
        print(f"co2 alarm : co2 is: {co2},loewr limit is {co2_ll}, upper limit is {co2_ul}")
        return True
    else:
        print(f"value is read is :{co2}")
        return False
def is_temp_voilated(temp):
    temp_ll=round(float(rules['temp']['LL']),2)
    temp_ul=round(float(rules['temp']['UL']),2)
    if temp>= temp_ll and temp<=temp_ul:
        return True
    else:
        return False
def is_hum_voilated(hum):
    hum_ll=round(float(rules['humdty']['LL']),2)
    hum_ul=round(float(rules['humdty']['UL']),2)
    if hum>=hum_ll and hum<=hum_ul:
        return True
    else:
        return False
def main():
    while True:
        co2=round(random.uniform(0,4000),2)
        temp=round(random.uniform(10,40),2)
        humdty=round(random.uniform(50,80),2)
        print(f"co2:{co2}ppm\ntemp:{temp}deg celsius\nHumidity:{humdty}%")
        break_yes=input("please select y or n (y/n)")
        if break_yes=='y':
            break
        else:
            pass
        voilated_flg=is_co2_voilated(co2)
        print(is_co2_voilated(co2))
        if voilated_flg==True:
            messg=f'Hello Every One In This Group \nCo2 Levels Violated. Co2 Value Is : {co2}\nhere is the video reference to control temperature you can go through it : https://www.youtube.com/watch?v=bvwnvYvMPyo&t=13s'
            print(f"co2 levels voilated. co2 values is {co2}")
            print(f'Violation detected: ${messg}')
            asyncio.run(telegram.send_test_message(messg))
        else:
            pass
        voilated_flg=is_temp_voilated(temp)
        print(is_temp_voilated(temp))
        if voilated_flg==True:
            messg=f'Hello Every One In This Group \nAlert: Temp Levels Violated. Temp Value Is : {temp}\n here is the video reference to control temperature you can go through it : https://www.youtube.com/watch?v=zFgqgSY3lJ0'
            print(f'violation detected: ${messg}')
            asyncio.run(telegram.send_test_message(messg))
        else:
            pass
        voilated_flg=is_hum_voilated(humdty)
        print(is_hum_voilated(humdty))
        if voilated_flg==True:
            messg=f'Hello Every One In This Group \nAlert: Humidity Levels Violated. Humidity Value Is : {humdty}\n here is the video reference to control humidity in air you can go through it : https://www.youtube.com/watch?v=cjlMRj56XXU'
            print(f'violation detected: ${messg}')
            asyncio.run(telegram.send_test_message(messg))
        else:
            pass
if __name__=='__main__':
    main()