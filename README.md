The options comes from command line and the operand for those options come from stdin.
Eamples below are self explanatory. "apply" is threaded.

####pingIPList file
	2,www.google.com
	2,mail.google.com
	2,yahoo.com
	2,facebook.com
	2,twitter.com

`apply ping -c < pingIPList`

	PING googlemail.l.google.com (74.125.229.245) 56(84) bytes of data.
	64 bytes from mia05s07-in-f21.1e100.net (74.125.229.245): icmp_req=1 ttl=55 time=24.3 ms
	64 bytes from mia05s07-in-f21.1e100.net (74.125.229.245): icmp_req=2 ttl=55 time=21.4 ms

	--- googlemail.l.google.com ping statistics ---
	2 packets transmitted, 2 received, 0% packet loss, time 1001ms
	rtt min/avg/max/mdev = 21.415/22.888/24.361/1.473 ms
	PING www.google.com (74.125.26.147) 56(84) bytes of data.
	64 bytes from vh-in-f147.1e100.net (74.125.26.147): icmp_req=1 ttl=42 time=41.8 ms
	64 bytes from vh-in-f147.1e100.net (74.125.26.147): icmp_req=2 ttl=42 time=41.4 ms

	--- www.google.com ping statistics ---
	2 packets transmitted, 2 received, 0% packet loss, time 1001ms
	rtt min/avg/max/mdev = 41.444/41.635/41.826/0.191 ms
	PING facebook.com (173.252.110.27) 56(84) bytes of data.
	64 bytes from edge-star-shv-13-frc1.facebook.com (173.252.110.27): icmp_req=1 ttl=83 time=40.3 ms
	64 bytes from edge-star-shv-13-frc1.facebook.com (173.252.110.27): icmp_req=2 ttl=83 time=43.3 ms

	--- facebook.com ping statistics ---
	2 packets transmitted, 2 received, 0% packet loss, time 1000ms
	rtt min/avg/max/mdev = 40.312/41.854/43.397/1.556 ms
	PING yahoo.com (206.190.36.45) 56(84) bytes of data.
	64 bytes from ir1.fp.vip.gq1.yahoo.com (206.190.36.45): icmp_req=1 ttl=48 time=89.4 ms
	64 bytes from ir1.fp.vip.gq1.yahoo.com (206.190.36.45): icmp_req=2 ttl=48 time=204 ms

	--- yahoo.com ping statistics ---
	2 packets transmitted, 2 received, 0% packet loss, time 1001ms
	rtt min/avg/max/mdev = 89.490/146.833/204.176/57.343 ms
	PING twitter.com (199.16.156.38) 56(84) bytes of data.
	64 bytes from 199.16.156.38: icmp_req=1 ttl=244 time=28.9 ms
	64 bytes from 199.16.156.38: icmp_req=2 ttl=244 time=25.8 ms

	--- twitter.com ping statistics ---
	2 packets transmitted, 2 received, 0% packet loss, time 5059ms
	rtt min/avg/max/mdev = 25.812/27.375/28.938/1.563 ms


####snmpList file
	,public, 1, localhost

`apply snmpwalk -0S -c -v < snmpList`

	iso.3.6.1.2.1.1.1.0 = STRING: "Linux server 3.2.0-39-generic-pae 
	iso.3.6.1.2.1.1.2.0 = OID: iso.3.6.1.4.1.8072.3.2.10
	iso.3.6.1.2.1.1.3.0 = Timeticks: (111595586) 12 days, 21:59:15.86
	iso.3.6.1.2.1.1.4.0 = STRING: "Me <me@example.org>"
	iso.3.6.1.2.1.1.5.0 = STRING: "server"
	iso.3.6.1.2.1.1.6.0 = STRING: "Sitting on the Dock of the Bay"
	iso.3.6.1.2.1.1.7.0 = INTEGER: 72
	iso.3.6.1.2.1.1.8.0 = Timeticks: (1) 0:00:00.01
	iso.3.6.1.2.1.1.9.1.2.1 = OID: iso.3.6.1.6.3.10.3.1.1
	iso.3.6.1.2.1.1.9.1.2.2 = OID: iso.3.6.1.6.3.11.3.1.1
	iso.3.6.1.2.1.1.9.1.2.3 = OID: iso.3.6.1.6.3.15.2.1.1
	iso.3.6.1.2.1.1.9.1.2.4 = OID: iso.3.6.1.6.3.1
	iso.3.6.1.2.1.1.9.1.2.5 = OID: iso.3.6.1.2.1.49
	iso.3.6.1.2.1.1.9.1.2.6 = OID: iso.3.6.1.2.1.4
	iso.3.6.1.2.1.1.9.1.2.7 = OID: iso.3.6.1.2.1.50
	iso.3.6.1.2.1.1.9.1.2.8 = OID: iso.3.6.1.6.3.16.2.2.1
	iso.3.6.1.2.1.1.9.1.3.1 = STRING: "The SNMP Management Architecture MIB."
	iso.3.6.1.2.1.1.9.1.3.2 = STRING: "The MIB for Message Processing and Dispatching."
	iso.3.6.1.2.1.1.9.1.3.3 = STRING: "The management information definitions for the SNMP User-based Security Model."
	iso.3.6.1.2.1.1.9.1.3.4 = STRING: "The MIB module for SNMPv2 entities"
	iso.3.6.1.2.1.1.9.1.3.5 = STRING: "The MIB module for managing TCP implementations"
	iso.3.6.1.2.1.1.9.1.3.6 = STRING: "The MIB module for managing IP and ICMP implementations"
	iso.3.6.1.2.1.1.9.1.3.7 = STRING: "The MIB module for managing UDP implementations"
	iso.3.6.1.2.1.1.9.1.3.8 = STRING: "View-based Access Control Model for SNMP."
	iso.3.6.1.2.1.1.9.1.4.1 = Timeticks: (0) 0:00:00.00
	iso.3.6.1.2.1.1.9.1.4.2 = Timeticks: (0) 0:00:00.00
	iso.3.6.1.2.1.1.9.1.4.3 = Timeticks: (0) 0:00:00.00
	iso.3.6.1.2.1.1.9.1.4.4 = Timeticks: (0) 0:00:00.00
	iso.3.6.1.2.1.1.9.1.4.5 = Timeticks: (0) 0:00:00.00
	iso.3.6.1.2.1.1.9.1.4.6 = Timeticks: (0) 0:00:00.00
	iso.3.6.1.2.1.1.9.1.4.7 = Timeticks: (0) 0:00:00.00
	iso.3.6.1.2.1.1.9.1.4.8 = Timeticks: (1) 0:00:00.01
	iso.3.6.1.2.1.25.1.1.0 = Timeticks: (501155914) 58 days, 0:05:59.14
	iso.3.6.1.2.1.25.1.2.0 = Hex-STRING: 07 DD 08 09 0E 05 36 00 2D 04 00 
	iso.3.6.1.2.1.25.1.3.0 = INTEGER: 1536
	iso.3.6.1.2.1.25.1.4.0 = STRING: "BOOT_IMAGE=/boot/vmlinuz-3.2.0-39-generic-pae root=UUID=d0e22b1c-1073-4abc-8531-cd7accc90d99 ro quiet splash vt.handoff=7
	"
	iso.3.6.1.2.1.25.1.5.0 = Gauge32: 2
	iso.3.6.1.2.1.25.1.6.0 = Gauge32: 145
	iso.3.6.1.2.1.25.1.7.0 = INTEGER: 0
	End of MIB


####echoList file
	this is line one
	this is line two
	this is line three
	this is line four

`apply echo -n  < echoList`
	this is line one this is line two this is line three this is line four

`apply echo  < echoList`
	this is line one
	this is line two
	this is line three
	this is line four

####snmpList file
localhost

You can only have ip in this file and control the options using "apply" command


`apply snmpwalk "-Os -c public -v 2c" < snmpList`
	iso.3.6.1.2.1.1.1.0 = STRING: "Linux server 3.2.0-39-generic-pae #62-Ubuntu SMP Wed Feb 27 22:25:11 UTC 2013 i686"
	iso.3.6.1.2.1.1.2.0 = OID: iso.3.6.1.4.1.8072.3.2.10
	iso.3.6.1.2.1.1.3.0 = Timeticks: (118921387) 13 days, 18:20:13.87
	iso.3.6.1.2.1.1.4.0 = STRING: "Me <me@example.org>"
	iso.3.6.1.2.1.1.5.0 = STRING: "server"
	iso.3.6.1.2.1.1.6.0 = STRING: "Sitting on the Dock of the Bay"
	iso.3.6.1.2.1.1.7.0 = INTEGER: 72
	iso.3.6.1.2.1.1.8.0 = Timeticks: (1) 0:00:00.01
	iso.3.6.1.2.1.1.9.1.2.1 = OID: iso.3.6.1.6.3.10.3.1.1
	iso.3.6.1.2.1.1.9.1.2.2 = OID: iso.3.6.1.6.3.11.3.1.1
	iso.3.6.1.2.1.1.9.1.2.3 = OID: iso.3.6.1.6.3.15.2.1.1
	iso.3.6.1.2.1.1.9.1.2.4 = OID: iso.3.6.1.6.3.1
	iso.3.6.1.2.1.1.9.1.2.5 = OID: iso.3.6.1.2.1.49
	iso.3.6.1.2.1.1.9.1.2.6 = OID: iso.3.6.1.2.1.4
	iso.3.6.1.2.1.1.9.1.2.7 = OID: iso.3.6.1.2.1.50
	iso.3.6.1.2.1.1.9.1.2.8 = OID: iso.3.6.1.6.3.16.2.2.1
	iso.3.6.1.2.1.1.9.1.3.1 = STRING: "The SNMP Management Architecture MIB."
	iso.3.6.1.2.1.1.9.1.3.2 = STRING: "The MIB for Message Processing and Dispatching."
	iso.3.6.1.2.1.1.9.1.3.3 = STRING: "The management information definitions for the SNMP User-based Security Model."
	iso.3.6.1.2.1.1.9.1.3.4 = STRING: "The MIB module for SNMPv2 entities"
	iso.3.6.1.2.1.1.9.1.3.5 = STRING: "The MIB module for managing TCP implementations"
	iso.3.6.1.2.1.1.9.1.3.6 = STRING: "The MIB module for managing IP and ICMP implementations"
	iso.3.6.1.2.1.1.9.1.3.7 = STRING: "The MIB module for managing UDP implementations"
	iso.3.6.1.2.1.1.9.1.3.8 = STRING: "View-based Access Control Model for SNMP."
	iso.3.6.1.2.1.1.9.1.4.1 = Timeticks: (0) 0:00:00.00
	iso.3.6.1.2.1.1.9.1.4.2 = Timeticks: (0) 0:00:00.00
	iso.3.6.1.2.1.1.9.1.4.3 = Timeticks: (0) 0:00:00.00
	iso.3.6.1.2.1.1.9.1.4.4 = Timeticks: (0) 0:00:00.00
	iso.3.6.1.2.1.1.9.1.4.5 = Timeticks: (0) 0:00:00.00
	iso.3.6.1.2.1.1.9.1.4.6 = Timeticks: (0) 0:00:00.00
	iso.3.6.1.2.1.1.9.1.4.7 = Timeticks: (0) 0:00:00.00
	iso.3.6.1.2.1.1.9.1.4.8 = Timeticks: (1) 0:00:00.01
	iso.3.6.1.2.1.25.1.1.0 = Timeticks: (508481716) 58 days, 20:26:57.16
	iso.3.6.1.2.1.25.1.2.0 = Hex-STRING: 07 DD 08 0A 0A 1A 34 00 2D 04 00 
	iso.3.6.1.2.1.25.1.3.0 = INTEGER: 1536
	iso.3.6.1.2.1.25.1.4.0 = STRING: "BOOT_IMAGE=/boot/vmlinuz-3.2.0-39-generic-pae root=UUID=d0e22b1c-1073-4abc-8531-cd7accc90d99 ro quiet splash vt.handoff=7
	"
	iso.3.6.1.2.1.25.1.5.0 = Gauge32: 2
	iso.3.6.1.2.1.25.1.6.0 = Gauge32: 144
	iso.3.6.1.2.1.25.1.7.0 = INTEGER: 0
	iso.3.6.1.2.1.25.1.7.0 = No more variables left in this MIB View (It is past the end of the MIB tree)
