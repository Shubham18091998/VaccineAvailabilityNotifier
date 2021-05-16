import requests

import time
from datetime import datetime, timedelta
import json
from pygame import mixer
from gi.repository import Notify

print("Starting search for Covid vaccine slots!")

age = int(input("Please input your age:"))
pincodes = [input("Please input your pincode:")]
print_flag = "Y"
num_days = 10

actual = datetime.today()
# print(actual)

list_format = [actual + timedelta(days=i) for i in range(num_days)]
# print(list_format)

actual_dates = [i.strftime("%d%m%y") for i in list_format]


# print(actual_dates)

def vaccine_availability():
    while True:
        counter = 0
        for pincode in pincodes:
            for given_date in actual_dates:
                URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(
                    pincode, given_date)
                header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                        'Chrome/56.0.2924.76 Safari/537.36'}
                result = requests.get(URL, headers=header)
                if result.ok:
                    response_json = result.json()

                    flag = False
                    if response_json["centers"]:
                        if print_flag == 'Y':
                            for center in response_json["centers"]:
                                for session in center["sessions"]:
                                    if session["min_age_limit"] <= age and session["available_capacity"] > 0:
                                        print('Pincode: ' + pincode)
                                        print("Available on: {}".format(given_date))
                                        print("\t", center["name"])
                                        print("\t", center["block_name"])
                                        print("\t Price: ", center["fee_type"])
                                        print("\t Availability : ", session["available_capacity"])

                                        if session["vaccine"] != '':
                                            print("\t Vaccine type: ", session["vaccine"])
                                        print("\n")

                                        counter = counter + 1
                                    else:
                                        pass
                    else:
                        pass

                else:
                    print("No Response!")

        if counter == 0:
            print("No Vaccination slot available!")
        else:
            mixer.init()
            mixer.music.load('sound/drip.ogg')
            mixer.music.play()
            Notify.init("Vaccine Notifier")
            Notify.Notification.new(summary="Vaccine", body="Vaccine slot is available").show()
            print("Search Completed!")
            return 0

        dt = datetime.now() + timedelta(minutes=5)

        while datetime.now() < dt:
            time.sleep(1)


vaccine_availability()
