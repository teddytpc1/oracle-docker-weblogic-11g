#!/bin/bash
. /u01/oracle/weblogic/wlserver_10.3/server/bin/setWLSEnv.sh
export ms_name=$1
export ms_listen_address=`echo "${ms_name,,}"`
export ms_listen_address=`echo "${ms_listen_address/_/}"`
export ms_listen_address=`echo "${ms_listen_address/1/}"`
export ms_cluster_name=`echo "${ms_name/WLS/CLUSTER}"`
export ms_cluster_name=`echo "${ms_cluster_name/1/}"`


echo $ms_name
echo $ms_listen_address
echo $ms_cluster_name
java weblogic.WLST /u01/oracle/weblogic/wlserver_10.3/common/bin/check.py $ms_name $ms_listen_address $ms_cluster_name
