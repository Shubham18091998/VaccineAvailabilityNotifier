# VaccineAvailabilityNotifier

How to run this script to get notification for Covid Vaccine availability:-

Step-1:Clone the github repository on your local system using the following command in GitBash.

git clone https://github.com/Shubham18091998/VaccineAvailabilityNotifier.git

Step-2:Install below dependencies using command prompt/terminal.

pip install requests (For Windows and Linix)

pip install requests pygame (For Windows and Linux)

pip install plyer (For Windows)

sudo apt-get install python-gobject (For Linux)

sudo apt-get install libnotify-bin (For Linux)

Step-3:Enter the age and pincode.

Step-4:Run the script vaccine.py on your local system. This script will automatically ping the CoWIN website for every 5 mins(you can adjust the time in the script by editing thid line dt = datetime.now() + timedelta(minutes=5)) and will send desktop notification if slot available
