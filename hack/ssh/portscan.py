##nmap的使用####
import nmap
import optparse
import sys
def nmapScan(tgtHost,tgtPort):
	nmScan=nmap.PortScanner()
	nmScan.scan(tgtHost,tgtPort)
	state=nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
	print ("[*]"+tgtHost+"tcp/"+tgtPort+" "+state )
def main():
	parser =optparse.OptionParser('usage%prog '+ '-H <target host> -p <target port>')
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
	parser.add_option('-p', dest='tgtPort', type='string', help='specify target port')
	(options, args) = parser.parse_args()
	#tgtHost = sys.argv[1]
	#tgtPorts = str(sys.argv[2]).split(',')
	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPort).split(',')
	if (tgtHost == None) | (tgtPorts[0] == None):
		print (parser.usage)
		exit(0)
	for tgtPort in tgtPorts:
		nmapScan(tgtHost, tgtPort)
main()



