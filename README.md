# Python app for monitoring processes 
### description
pyproc-server.py - server side script which gets data from client files and writes them to one file\
pyproc-client.py - client side script which collects info about running processes and write them to file\
pyprocweb.py - flask web app which displays data about running processes\
get-files.yml - ansible playbook which pull client's file to server\
### usage
ssh to 192.168.3.90
```
ssh username@192.168.3.90
```
In my home directory you will find two shell scripts:\
- `make.sh` - this script is in crontab and runs every 5 minutes. Executes everything for webpage refresh\
- `newclient.sh` - copy new client to all machines\
