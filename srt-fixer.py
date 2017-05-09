
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

		h = int(float(args.offset)//3600)
		mi = int(float(args.offset)%3600//60)
		sec = int(float(args.offset%60))

		a = str(args.offset).split('.')
		mil = int(a[1])

		rexp = re.compile('\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}')
		found = rexp.search(line)
		if found:
			sys.stdout.flush()
			temp = re.sub('--> ','', line)
			temp = re.sub('\r\n','', temp)
			temp = temp.split(' ')

			temp[0] = temp[0].split(':')
			temp[0][2] = temp[0][2].split(',')

			temp[1] = temp[1].split(':')
			temp[1][2] = temp[1][2].split(',')

			temp[0][0] = str(int(temp[0][0]) + h)
			temp[0][1] = str(int(temp[0][1]) + mi)
			temp[0][2][0] = str(int(temp[0][2][0]) + sec)
			temp[0][2][1] = str(int(temp[0][2][1]) + mil)

			temp[1][0] = str(int(temp[0][0]) + h)
			temp[1][1] = str(int(temp[0][1]) + mi)
			temp[1][2][0] = str(int(temp[1][2][0]) + sec)
			temp[1][2][1] = str(int(temp[1][2][1]) + mil)

			# print(line)
			line = '\n'
			timeStampFormation = "{}:{}:{},{} --> {}:{}:{},{}"
			#a = str(line[0][0])
			print(timeStampFormation.format(temp[0][0],temp[0][1],temp[0][2][0],temp[0][2][1],temp[1][0],temp[1][1],temp[1][2][0],temp[1][2][1]), end='')

		sys.stdout.write(line)
		sys.stdout.flush()

		# -- αντικαταστήστε με τον δικό σας κώδικα (τέλος) --

