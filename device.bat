@echo off

echo Disconnecting old connections...
adb disconnect

echo Setting up connected device
adb tcpip 5555

echo Waiting for device to initialize
timeout 3

FOR /F "tokens=2" %%G IN ('adb shell ip addr show wlan0 ^|find "inet "') DO set ipfull=%%G
FOR /F "tokens=1 delims=/" %%G in ("%ipfull%") DO set ip=%%G

echo Connecting to device with IP %ip%...
adb connect %ip%

rem Restart the ADB server
adb kill-server
adb start-server

rem Connect to the Android device over Wi-Fi using the retrieved IP
adb connect %ip%:5555

echo Connected to device %ip% on port 5555.
