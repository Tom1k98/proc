import os
from datetime import datetime

tmp = datetime.now()
now = tmp.strftime("%m%d%Y-%H%M")

def delfiles():
	if len(os.listdir('/opt/files')) > 0:
		for files in os.listdir('/opt/files'):
			os.remove('/opt/files/{}'.format(files))

def getprocs():
	filename = '/opt/procs/procs-{}'.format(now)
	fw = open(filename, 'w')
	for f in os.listdir('/opt/files'):
		ff = '/opt/files/{}'.format(f)
		fr = open(ff, 'r')
		for lines in fr:
			fw.write(lines)

def printproc():
	filename = '/opt/procs/procs-{}'.format(now)
	file = open(filename, 'r')
	for tmp in file:
		fin = tmp.split('-')
		print(fin)

def main():
	getprocs()
	printproc()
	delfiles()

if __name__ == "__main__":
	main()
