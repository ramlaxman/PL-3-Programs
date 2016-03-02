#!/usr/bin/python 
###############################################################
# * Python code for Setting an IP Address and implementing 
# * a FTP Client application to upload file on the server 
# * using Beaglebone Black running Debian 7 Linux distribution
###############################################################
# * Developed by MicroEmbedded Technologies
###############################################################

import socket, struct, fcntl
import ftplib

IP_ADDR  	= "192.168.0.125" 
SERVER_IP	= "192.168.0.20"
SERVER_USER	= "ACER"
SERVER_USER_PWD = ""
FILE_TO_SEND	= "b.c"
SEND_CMD	= "STOR "

SIOCSIFADDR = 0x8916
SIOCGIFADDR = 0x8915
 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
def setIpAddr(iface, ip):
     bin_ip = socket.inet_aton(ip)
     ifreq = struct.pack('16sH2s4s8s', iface, socket.AF_INET, '\x00'*2, bin_ip, '\x00'*8)
     fcntl.ioctl(sock, SIOCSIFADDR, ifreq)
     return
     
def getIpAddr(iface = 'eth0'):
     ifreq = struct.pack('16sH14s', iface, socket.AF_INET, '\x00'*14)
     try:
         res = fcntl.ioctl(sock, SIOCGIFADDR, ifreq)
     except:
         return None   
     ip = struct.unpack('16sH2x4s8x', res)[2]
     return socket.inet_ntoa(ip)

print "Current IP Address: %s" % getIpAddr('eth0')
print "Setting IP to: %s" % IP_ADDR   
setIpAddr('eth0', IP_ADDR)
print "New IP Address: %s" % getIpAddr('eth0')


try:
	print "\nUploading a File on Server [%s]" %SERVER_IP
	print "Sending a File (%s)......." % (FILE_TO_SEND),
	session = ftplib.FTP(SERVER_IP, SERVER_USER, SERVER_USER_PWD)
	file = open(FILE_TO_SEND,'rb')                  # file to send
	session.storbinary(SEND_CMD + FILE_TO_SEND, file)     # send the file
	file.close()                                    # close file and FTP
	session.quit()
	print "Done"
except:
	print "Error Communicating to Server !!!"