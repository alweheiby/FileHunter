import os
import re
import sys
import glob
from os import walk
import mmap
from threading import  Thread
from datetime import datetime

extension_List = [".txt", ".ppt", ".doc",".xls", ".csv"]
#xtension_List = [".txt", ".doc"]
#filesList = [] # this is the domain of the search function.
searchList = []

t1 = datetime.now()
# def searchFile(fileName, keyword):
# 	openfile = open(fileName, encoding ='utf-8')
# 	line = openfile.readlines()
# 	for line in openfile:
#
# 				if keyword in part:
# 					print(fileName)
# 				line = openFile.readline()

def get_drives():
	response = os.popen("wmic logicaldisk get caption")
	list1 = []
	total_file = []

	for line in response.readlines():
		line = line.strip("\n")
		line = line.strip("\r")
		line = line.strip(" ")
		if (line == "Caption" or line == ""):
			continue
		if (line == 'C:'):
			print('LINE', line)
			for (dirname) in os.listdir(line + '\\'):
				if (dirname != 'Windows'):
					list1.append('C:\\' + dirname)
		else:
			list1.append(line)
	return list1

drivesList = get_drives()
print(drivesList)


#for drive in drivesList:

#	listOfFiles = os.listdir() # each Drive will have the main folders in it is directory.
	#for x in listOfFiles:
	#	print(drive)
	#	print(x)

def searchFile(filename, dirname):
	for extension in extension_List:
		if filename.lower().endswith(extension):
			cwd = os.getcwd()
			fullPath = os.path.join(dirname,filename)
			if os.path.isfile(fullPath):
				print(fullPath)
				return fullPath
	return -1

def threadedWalk(directory):
	print('THREADED WALK')
	if (os.path.isdir(directory)):
		for (dirname,dirs,files) in os.walk(directory):
				for filename in files:
					result = searchFile(filename, dirname)
					if (result != -1):
						searchList.append(result)


os.chdir('/')
def spider(drivesList):
	print('THREADING')
	for drive in drivesList:
		if drive.startswith('C:\\$'):
			continue
		if (os.path.isdir(drive)):
			print('DRIVE', drive)
			thread = Thread(target=threadedWalk, args=(drive,))
			thread.start()


#### ver_01 : storing cwd and filename separately ####
cwdList = []
fileNameList = []


spider(drivesList)


keyword ="trademark"

file1 = r"C:\Users\grena_000\Documents\test.txt"

def searchFile1(sourceFile, keyword):
	a = sourceFile.replace(r'\t', r'\\t').replace(r'\a', r'\\a')
	f = open(a, 'r')
	contents = f.read()
	if (contents.find(keyword) >= 0):
		print(sourceFile)
	else:
		print('not found!')


#searchFile1(file1, keyword)
t2 = datetime.now()

totalTime = t2-t1
print(totalTime)


					#print((str1+'/'+dirpath+'/'+dirname+'/'+name))




