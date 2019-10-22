/u01/oracle/weblogic/wlserver/common/bin/wlst.sh -skipWLSModuleScanning /u01/oracle/container-scripts/create-wls-domain.py && \
mkdir -p /u01/oracle/weblogic/user_projects/domains/base_domain/servers/AdminServer/security && \
echo "username=weblogic" > /u01/oracle/weblogic/user_projects/domains/base_domain/servers/AdminServer/security/boot.properties && \
echo "password=$ADMIN_PASSWORD" >> /u01/oracle/weblogic/user_projects/domains/base_domain/servers/AdminServer/security/boot.properties && \
mkdir -p /u01/oracle/weblogic/user_projects/domains/base_domain/servers/WLS_ECUP1/security && \
echo "username=weblogic" > /u01/oracle/weblogic/user_projects/domains/base_domain/servers/WLS_ECUP1/security/boot.properties && \
echo "password=$ADMIN_PASSWORD" >> /u01/oracle/weblogic/user_projects/domains/base_domain/servers/WLS_ECUP1/security/boot.properties && \
echo ". /u01/oracle/weblogic/user_projects/domains/base_domain/bin/setDomainEnv.sh" >> /u01/oracle/.bashrc && \
echo "export PATH=$PATH:/u01/oracle/weblogic/wlserver/server/bin:/u01/oracle/weblogic/wlserver/common/bin:/u01/oracle/weblogic/user_projects/domains/base_domain/bin" >> /u01/oracle/.bashrc && \
chown -R oracle:oracle /u01/oracle/scripts/
chown -R oracle:oracle /u01/oracle/weblogic/user_projects
rm /u01/oracle/container-scripts/create-wls-domain.py
