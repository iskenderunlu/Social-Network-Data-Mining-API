# -*- coding: utf-8 -*-
import datetime
import commands
import time
import shlex
import subprocess
import os
import sys


def main():

	if len(sys.argv)!=4:
		print "eksik bilgi girdiniz" + "\n"+"python import_script.py start_date(YYYY/MM/DD/HH) deadline_date(YYYY/MM/DD/HH) destination_folder(string) komutuyla çalıştırınız."
		return

	start_date=sys.argv[1]
	deadline_date=sys.argv[2]
	destination_folder=sys.argv[3]

	if start_date is None:
		print "Enter start date !"
	elif deadline_date is None :
		print "Enter deadline date !"
	elif destination_folder is None :
		print "Enter destination folder !"



	command1="hadoop fs -getmerge /user/flume/gniptweet/"

	#start_date= str(sys.argv[1])
	#start_date	=	raw_input("Please, enter your start date in form YYYY/MM/DD/HH :")
	start_array	= start_date.split('/')

	#deadline_date = str(sys.argv[2])
	#deadline_date	=	raw_input("Please, enter your deadline date in form YYYY/MM/DD/HH :")
	deadline_array	= deadline_date.split('/')
	#print (deadline_array)
	print int(deadline_array[0])
	date = datetime.datetime(int(start_array[0]),int(start_array[1]),int(start_array[2]),int(start_array[3]))
	print date
	deadline = datetime.datetime(int(deadline_array[0]),int(deadline_array[1]),int(deadline_array[2]),int(deadline_array[3]))
	print deadline

	temp=''
	temp2=''


	while date <= deadline: 
		temp=date.strftime('%Y/%m/%d/%H')
		if destination_folder:
			temp2="/tmp/"+ "/"+destination_folder+"/"+date.strftime('%Y%m%d%H')	
			command = command1 +temp+' '+temp2		
		else:
			os.system("mkdir /tmp"+"/"+destination_folder+"/"+date.strftime('%Y%m%d%H'))
			command = command1 +temp+' '+"/tmp"+destination_folder+"/"+date.strftime('%Y%m%d%H')
		date += datetime.timedelta(hours=1)
		print command
		os.system(command)

if __name__ == "__main__":
    main()

    pass
