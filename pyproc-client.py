import psutil
import os
import socket
import sys
from datetime import datetime

host = socket.gethostname()
running = []
tmp = datetime.now()
now = tmp.strftime("%m%d%Y-%H%M")

def gethelp():
	if sys.argv[1] in ("-h", "--help"):
		print('script which collect specified processses and save them to file')
		print('There should be script on server where files are collected')
		sys.exit()

#fce ktera odstrani stare soubory
def delfiles():
	if len(os.listdir('/root/files')) > 0:
		for files in os.listdir('/root/files'):
			os.remove('/root/files/{}'.format(files))

#fce, ktera zjistuje zda dany proces bezi
def getproc(name):
	for proc in psutil.process_iter():
		if proc.name() in name:
			running.append(name)

#fce ktera ktera krmi fci getproc procesy, ktere chceme najit
def genproc():
	procs = ['ansa_linux_x86_64', 'meta_post_x86_64', 'a4', 'a4_linux64.x', 'a4_linux64_fbo.x']
	for getp in procs:
		getproc(getp)


#fce ktera zapisuje bezici ;procesy do souboru
def selectproc():
	filename = '/root/files/{}-{}'.format(host, now)
	file = open(filename, 'w')

	if 'a4' in running:
		animator = 'animator - {}'.format(host)
		file.write(animator)
		file.write('\n')

	if 'ansa_linux_x86_64' in running:
		ansa = 'ansa - {}'.format(host)
		file.write(ansa)
		file.write('\n')

	if 'meta_post_x86_64' in running:
		meta = 'meta - {}'.format(host)
		file.write(meta)
		file.write('\n')

def main():
	if len(sys.argv) > 1:
		gethelp()

	delfiles()
	genproc()
	selectproc()

if __name__ == "__main__":
	main()
