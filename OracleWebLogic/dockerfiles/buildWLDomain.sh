#docker run --net wlsnw --name wlsdomain -v /D01/arcor/domain:/u01/oracle/weblogic/user_projects/domains/base_domain -d -i oracle/weblogic:10.3.6
docker run --net wlsnw --name wlsdomain  -d -i soporteayi/weblogic:10.3.6
docker exec -u oracle -it wlsdomain bash /u01/oracle/container-scripts/create-wls-domain.sh
sudo docker cp  wlsdomain:/u01/oracle/weblogic/user_projects/domains/base_domain /D01/arcor/domain/
sudo chown -R arcor:arcor /D01/arcor/domain/
docker stop wlsdomain
#docker rm wlsdomain
docker run --net wlsnw --name wlsadmin -v /D01/arcor/domain/base_domain:/u01/oracle/weblogic/user_projects/domains/base_domain -p 7001:7001 -d -i soporteayi/weblogic:10.3.6 /u01/oracle/weblogic/user_projects/domains/base_domain/bin/startWebLogic.sh
##docker commit wlsadmin  oracle/weblogic:10.3.6-wlsadmin2
##docker build -t oracle/weblogic:10.3.6-ecup ../../samples/11g-domain/ecup/
sleep 60
docker run --net wlsnw --name  wlsecup -v /D01/arcor/domain/base_domain:/u01/oracle/weblogic/user_projects/domains/base_domain -p 7101:7101 -d -i soporteayi/weblogic:10.3.6 /u01/oracle/weblogic/user_projects/domains/base_domain/bin/startManagedWebLogic.sh WLS_ECUP1
