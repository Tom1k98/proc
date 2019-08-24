import os
from datetime import datetime

ansap = 0
metap = 0
animatorp = 0
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

def printprocs():
	print('bezici sluzby na fem stanicich:')
	print('ansa - {}'.format(ansap))
	print('meta - {}'.format(metap))
	print('animator - {}'.format(animatorp))

def main():
	getprocs()
	countprocs()
	printprocs()
	#delfiles()

if __name__ == "__main__":
	main()
