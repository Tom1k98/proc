import os
from datetime import datetime
import csv
import sys

ansap = 0
metap = 0
animatorp = 0
tmp = datetime.now()
now = tmp.strftime("%m%d%Y-%H%M")
nowh = tmp.strftime("%m.%d.%Y-%H")


#smaze info o starych informacich
def delfiles():
	if len(os.listdir('/www/')) > 0:
		for files in os.listdir('/www/'):
			if not files.endswith('data.csv'):
				os.remove('/www/{}'.format(files))

#fce ktera vytahne procesy ze vsech souboru a zapise je do jednoho
def getprocs():
	filename = '/opt/procs/procs-{}'.format(now)
	fw = open(filename, 'w')
	for f in os.listdir('/opt/files'):
		ff = '/opt/files/{}'.format(f)
		fr = open(ff, 'r')
		for lines in fr:
			fw.write(lines)

#fce ktera spocita pocet procesu vuci jednotlivym aplikacim
def countprocs():
	filename = '/opt/procs/procs-{}'.format(now)
	file = open(filename, 'r')
	global ansap
	global metap
	global animatorp
	for tmp in file:
		fin = tmp.split('-')
		if 'ansa' in fin[0]:
			ansap += 1
		if 'meta' in fin[0]:
			metap += 1
		if 'animator' in fin[0]:
			animatorp += 1

#vypise pocet procesu k jednotlivym aplikacim
def writeprocs():
	with open('/www/procstat', 'w') as file:
		file.write('ansa - {}\n'.format(ansap))
		file.write('meta - {}\n'.format(metap))
		file.write('animator - {}\n'.format(animatorp))

def writetocsv():
	with open('/www/data.csv', 'a') as csv_file:
		writecsv = csv.writer(csv_file)
		writecsv.writerow([nowh, ansap, metap, animatorp])
	csv_file.close()

def checkcsv():
	with open('/www/data.csv', 'r') as csv_check:
		next(csv_check)
		check = csv.reader(csv_check, delimiter=',')
		for line in check:
			if nowh not in line[0]:
				writetocsv()


def main():
	getprocs()
	countprocs()
	delfiles()
	writeprocs()
	checkcsv()


if __name__ == "__main__":
	main()
