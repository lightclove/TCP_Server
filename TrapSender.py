# -*- coding: utf-8 -*-
#!\usr\bin\python
#This is my SNMP trap Sender code

from pysnmp.hlapi.asyncore import *

snmpEngine = SnmpEngine()
sendNotification(
    snmpEngine,
    CommunityData('public'),
    UdpTransportTarget(('192.168.13.117', 162)),
    ContextData(),
    'trap',
    NotificationType(ObjectIdentity('SNMPv2-MIB', 'coldStart')),
  )

snmpEngine.transportDispatcher.runDispatcher()