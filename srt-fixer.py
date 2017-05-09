import time
import sys
import re
import argparse


parser = argparse.ArgumentParser()
# add mandatory (positional) arguments
parser.add_argument("fname",help="input srt file name")
parser.add_argument("offset",type=float,help="subtitle offset in seconds to apply (can be fractional)")

# parse arguments
args = parser.parse_args()
with open(args.fname,newline='') as ifp:	
	for line in ifp:
	
		# -- αντικαταστήστε με τον δικό σας κώδικα (αρχή) --
		rexp = re.compile('\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}')
		found = rexp.search(line)
		if found:
			sys.stdout.flush()
			line = re.sub('--> ','', line)
			line = re.sub('\r\n','', line)
			line = line.split(' ')

			line[0] = line[0].split(':')
			line[0][2] = line[0][2].split(',')

			line[1] = line[1].split(':')
			line[1][2] = line[1][2].split(',')

			line[0][0] = str(int(line[0][0]) + (int(args.offset)//3600))
			line[0][1] = str(int(line[0][1]) + (int(args.offset)%3600//60))
			# line[0][1][0] = str(int(line[0][1][0]) + (int(args.offset//3600)))

			# line[1][0] = str(int(line[0][0]) + (int(args.offset)//3600))
			# line[1][1] = str(int(line[0][1]) + (int(args.offset)%3600//60))
			# line[1][1][0] = str(int(line[1][1][0]) + (int(args.offset)//3600))

			#line[2][1] = str(int(line[2][1]) + (int(args.offset)))

			print(line)
			#line = '\n'
			#timeStampFormation = "{}:{}:{},{} --> {}:{}:{},{}"
			
			#print(timeStampFormation.format(4,4,4,4,4,4,4,4), end='')

		#sys.stdout.write(line)
		#sys.stdout.flush()
		# -- αντικαταστήστε με τον δικό σας κώδικα (τέλος) --

