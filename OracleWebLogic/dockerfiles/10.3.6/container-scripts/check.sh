export ms_name=$1
export ms_listen_address=`echo "${ms_name,,}"`
export ms_listen_address=`echo "${ms_listen_address/_/}"`
export ms_listen_address=`echo "${ms_listen_address/1/}"`
export ms_cluster_name=`echo "${ms_name/WLS/CLUSTER}"`
export ms_cluster_name=`echo "${ms_cluster_name/1/}"`
export ms_listen_port=$2

echo $ms_name
echo $ms_listen_address
echo $ms_cluster_name
java weblogic.WLST check.py $ms_name $ms_listen_address $ms_cluster_name $ms_listen_port

docker exec -it wlsadmin mkdir /u01/oracle/weblogic/user_projects/base_domain/servers/$ms_name
docker exec -it wlsadmin cp /u01/oracle/weblogic/user_projects/base_domain/servers/AdminServer/security/boot.properties /u01/oracle/weblogic/user_projects/base_domain/servers/$ms_name/security