import psutil
import os
import socket
from datetime import datetime

host = socket.gethostname()
running = []
tmp = datetime.now()
now = tmp.strftime("%m%d%Y-%H%M")

def checkfiles():
	if len(os.listdir('/root/files')) > 0:
		for files in os.listdir('/root/files'):
			os.remove('/root/files/{}'.format(files))


def getproc(name):
	for proc in psutil.process_iter():
		if proc.name() in name:
			running.append(name)

def genproc():
	procs = ['ansa_linux_x86_64', 'meta_post_x86_64', 'a4', 'a4_linux64.x']
	for getp in procs:
		getproc(getp)



def selectproc():
	filename = '/root/files/{}-{}'.format(host, now)
	file = open(filename, 'w')

	if ['a4', 'a4_linux64.x'] in running:
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
	checkfiles()
	genproc()
	selectproc()

if __name__ == "__main__":
	main()
