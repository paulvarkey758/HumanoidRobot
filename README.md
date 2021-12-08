# HumanoidRobot
A 9DOF humanoid robot which can move according to our voice commands and the robot can communicate and reply to us.raspberry pi is the core part of the robot and the full script is written in python. we can give commands to the robot using our smartphone. the smartphone and raspberry pi are communicatiing by using the bluetooth. Here SQLite3 is used as database to store the data.<br>
<img src="images/humanoid_robot.png" width="600" height="700">

<h2>Installation of Servo Driver</h2>
Here we are using 9 servos for the robot. So we need a servo driver to control and power the servos. In this scenario we are using adafruit-pca9685 16 channel servo driver. To work with the driver we have to install The riquired library using following command.<br><br>
<i>sudo pip install adafruit-pca9685</i><br><br>
<h2>Installation of Database</h2>
Here we are using SQLite3 as database. and we have a GUI for the SQLite3 data base which is called DB Browser. To install the database and DB Browser use the following commands respectively.<br><br>
<i>sudo apt-get install sqlite3</i><br>
<i>sudo apt-get install sqlitebrowser</i><br><br>
<h2>Installation of Festival</h2><br>
Festival is a library to used to conver the text into speech. Here the robot talk to us by converting the text taken from the database into speech. To install the Festival use the following command<br><br>
<i>sudo apt-get install festival</i><br><br>
<h2>Installation of bluetooth libraries</h2>
To Establish the connection between the robot and the smartphone is done by using bluetooth to use the bluetooth in raspberrypi, we have to install some libraries,<br><br>
<i>sudo apt-get install python-bluetooth<i/><br><br>
<i>sudo apt-get install bluetooth bluez libbluetooth-dev blueman<i/><br><br>
To add the SP profile to the Pi edit this file<br><br>

<i>sudo nano /etc/systemd/system/dbus-org.bluez.service</i><br><br>

Add the compatibility flag ‘-C’, at the end of ‘ExecStart=’ line. 
Add a new line after that to add the SP profile.<br><br>

<i>ExecStart=/usr/lib/bluetooth/bluetoothd -C</i><br><br>
<i>ExecStartPost=/usr/bin/sdptool add SP</i><br><br>
Now save the file and reboot the Pi. Back to the terminal and enter the following command.<br><br>

<i>sudo hciconfig</i><br><br>
<i>sudo rfcomm watch hci0</i><br><br>




