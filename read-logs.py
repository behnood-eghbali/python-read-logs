# reading npm log files from terminal using python (linux)

import os, glob, sys
log_path = os.path.expanduser('~/.npm/_logs/*.log')
log_files = glob.glob(log_path)
for file in log_files:
	f = open(file)
	sys.stdout.write(f.read())
	f.close()
