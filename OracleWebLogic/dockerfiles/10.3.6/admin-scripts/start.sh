#!/bin/bash 
sleep 30
/u01/oracle/mwhome/11.1.1.6/Middleware/wlserver_10.3/common/bin/wlst.sh <<EOF
connect('weblogic','welcome1','t3://wlsadmin:7001')
nmEnroll('/u01/oracle/weblogic/user_projects/domains/base_domain','/u01/oracle/weblogic/wlserver_10.3/common/nodemanager')
exit()
EOF
