import os, sys
if __name__ == "__main__":
	if len(sys.argv) == 2:
		if sys.argv[1] == "remove":
			os.system("rm -f .__apikey__.txt")
			exit(" [!] Succesfull Deleted")
		else:
			print(" [?] Wellcome : ")
			exit(" [!] Run : python Jsl.py remove")
	try:
		__import__("xjsl").__main_somi_code()
	except Exception as e:
		exit(str(e))
