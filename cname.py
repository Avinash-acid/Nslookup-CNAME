import dns.resolver
from sys import argv
from termcolor import colored


script, filename = argv

with open(filename) as f:
	content = [x.strip('\n') for x in f.readlines()] # strips \n in outpu:
	for i in range(len(content)):
		try:
			print colored("For:  " +content[i],  "green")
			answers = dns.resolver.query(content[i], 'CNAME')
			for rdata in answers:
	    			print ' cname target address:', rdata.target
		except:
			"Error"
