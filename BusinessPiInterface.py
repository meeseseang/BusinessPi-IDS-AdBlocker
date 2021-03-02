# Import Python modules
# Subprocess is the module that enables Python to interact with the CLI of a computer
# PySimpleGUI is the module that compiles different modules and allows me to write a GUI (Graphical User Interface)
# Logging is a module that allows exceptions and errors to be written to a file
import subprocess
import PySimpleGUI as sg
import logging

# Set the window theme to dark blue
sg.theme("Dark Grey 1")

# This initializes the variable that will output the speed test results. Initialize any other variables here.
SpeedTestStdout = ""

# Create the main text header at the top of the window
TopHeader = [[sg.Text("BusinessPi Interface", font=("Helvetica", 35), justification="center")]]

# Create the PiHole controls
PiHoleLayout = [[sg.Text("PiHole Controls", font=("Helvetica", 25))],
                [sg.Button("Restart PiHole"), sg.Button("Status"), sg.Button("Update Blocklist", key='updateGravity')],
                [sg.InputText('URL to whitelist (excluding http://)', size= (30,5), key='whitelistText'), sg.Button("Submit", key='submitWhitelist')],
                [sg.InputText('URL to blacklist (excluding http://)', size= (30,5), key='blacklistText'), sg.Button("Submit", key='submitBlacklist')]]

# Create the Raspberry Pi system controls
RaspiSystemControls = [[sg.Text("Raspberry Pi System Controls", font=("Helvetica", 25))],
                       [sg.Button("Restart", key='_raspiRestart_'), sg.Button("Shutdown", key='_raspiShutdown_')]]

# Create speed test control
SpeedTestControl = [[sg.Text("Speed Test", font=("Helvetica", 25))],
                    [sg.Button("Run Speed Test", key='-runSpeedTest-')]]

# Create the Snort IDS controls
SnortControls = [[sg.Text("Snort IDS Controls", font=("Helvetica", 25))],
                 [sg.Button("Start Snort", key='-startSnort-'), sg.Button("Stop Snort", key='-stopSnort-'), sg.Button("Show Alerts", key='-showSnortAlert-')]]

# Create the Console Output Layout
ConsoleOutputLayout = [[sg.Text("Console Output: ", key='-updateSpeed-', font=("Helvetica", 14)), sg.Button("Clear Console", key='-clearConsole-')],
                       [sg.Output(size=(123, 8), key='outputConsole')]]

# Stitch together the final layout
layout = [[sg.Column(TopHeader, justification='center')],
          [sg.HorizontalSeparator()],
          [sg.Column(RaspiSystemControls), sg.Column(PiHoleLayout)],
          [sg.Column(SpeedTestControl, pad=((5,210),3)), sg.Column(SnortControls)],
          [sg.Column(ConsoleOutputLayout)]]

# Create the window for the controls to be in
window = sg.Window("BusinessPi Control Interface", layout, keep_on_top=True, size=(800, 480))

# Start the event loop that checks for button presses and interactions
while True:

    # Read the interface window
    event, values = window.read()
    window.refresh()

    # Check for the Restart PiHole command
    if event == "Restart PiHole":
        try:
            subprocess.run(["sudo", "/home/raspi/BusinessPiScripts/piholeRestart.sh"])
            print("PiHole has been restarted")
        except Exception as Argument:
            f = open("BusinessPiExceptions.txt", "a")
            f.write(str(Argument))
            f.write("\n")
            f.close()

    # Check for the PiHole Status command
    if event == "Status":
        try:
            window.find_element('outputConsole').Update('')
            subprocess.Popen(["sudo", "/home/raspi/BusinessPiScripts/piholeStatus.sh"], stdout=subprocess.PIPE)
            PiHoleStatusOutput = subprocess.Popen(["sudo", "/home/raspi/BusinessPiScripts/piholeStatus.sh"], stdout=subprocess.PIPE).stdout.read()
            CleanedStatusOutput = PiHoleStatusOutput.decode().split('\n')
            print(*CleanedStatusOutput, sep='\n')
            window.refresh()
        except Exception as Argument:
            f = open("BusinessPiExceptions.txt", "a")
            f.write(str(Argument))
            f.write("\n")
            f.close()

    # Check for PiHole gravity update
    if event == "updateGravity":
        try:
            subprocess.run(["sudo", "/home/raspi/BusinessPiScripts/piholeUpdateBlocklist.sh"])
            print("The blocklist has been updated")
        except Exception as Argument:
            f = open("BusinessPiExceptions.txt", "a")
            f.write(str(Argument))
            f.write("\n")
            f.close()

    # Check for PiHole whitelist submission
    if event == "submitWhitelist":
        whitelistURL = values['whitelistText']
        try:
            subprocess.run(["pihole", "-w", str(whitelistURL)])
            print(str(whitelistURL) + " has been added to the whitelist")
        except Exception as Argument:
            f = open("BusinessPiExceptions.txt", "a")
            f.write(str(Argument))
            f.write("\n")
            f.close()

    # Check for PiHole blacklist submission
    if event == "submitBlacklist":
        blacklistURL = values['blacklistText']
        try:
            subprocess.run(["pihole", "-w", str(blacklistURL)])
            print(str(blacklistURL) + " has been added to the whitelist")
        except Exception as Argument:
            f = open("BusinessPiExceptions.txt", "a")
            f.write(str(Argument))
            f.write("\n")
            f.close()

    # Check for shutdown raspi command
    if event == "_raspiShutdown_":
        try:
            subprocess.run(["sudo", "/home/raspi/BusinessPiScripts/shutdown.sh"])
        except Exception as Argument:
            f = open("BusinessPiExceptions.txt", "a")
            f.write(str(Argument))
            f.write("\n")
            f.close()

    # Check for restart raspi command
    if event == "_raspiRestart_":
        try:
            subprocess.run(["sudo", "/home/raspi/BusinessPiScripts/restart.sh"])
        except Exception as Argument:
            f = open("BusinessPiExceptions.txt", "a")
            f.write(str(Argument))
            f.write("\n")
            f.close()

    # Check for Start Snort command
    if event == "-startSnort-":
        try:
            subprocess.run(["sudo", "/home/raspi/BusinessPiScripts/startSnort.sh"])
            print("Snort has been started")
        except Exception as Argument:
            f = open("BusinessPiExceptions.txt", "a")
            f.write(str(Argument))
            f.write("\n")
            f.close()

    # Check for Stop Snort command
    if event == "-stopSnort-":
        try:
            subprocess.run(["sudo", "/home/raspi/BusinessPiScripts/stopSnort.sh"])
            print("Snort has been stopped")
        except Exception as Argument:
            f = open("BusinessPiExceptions.txt", "a")
            f.write(str(Argument))
            f.write("\n")
            f.close()

    # Check for Check Snort Alerts command
    if event == "-showSnortAlert-":
        try:
            subprocess.run(["sudo", "/home/raspi/BusinessPiScripts/snortAlerts.sh"])
            print("Printing Snort Alerts")
        except Exception as Argument:
            f = open("BusinessPiExceptions.txt", "a")
            f.write(str(Argument))
            f.write("\n")
            f.close()

    # Check for speedtest command. Then run it.
    if event == "-runSpeedTest-":
        window.find_element('outputConsole').Update('')
        print("Speed test is running")
        subprocess.Popen(["speedtest"], stdout=subprocess.PIPE)
        SpeedTestStdout = subprocess.Popen(["speedtest"], stdout=subprocess.PIPE).stdout.read()
        cleanedOutput = SpeedTestStdout.decode().split('\n')
        # Try except block. If the code throws an error, don't freeze, but instead print the whole output
        try:
            print(cleanedOutput[6])
            print(cleanedOutput[8])
        except:
            print("Could not parse output. Printing Full Output instead")
            print(cleanedOutput)

        print("Speed test has finished")
        cleanedOutput.clear()
        window.refresh()

    # Code to clear the console when the button is pressed
    if event == "-clearConsole-":
        window.find_element('outputConsole').Update('')
        window.refresh()

    # If the window is closed, then exit the event loop
    if event == sg.WINDOW_CLOSED:
        break

# Once the program has exited the event loop then close then window and stop the program
window.close()
