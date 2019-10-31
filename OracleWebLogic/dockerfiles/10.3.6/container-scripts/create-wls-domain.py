# Weblogic on Docker Default Domain
#
# Default domain 'base_domain' to be created inside the Docker image for WLS
#
# Since : October, 2014
# Author: bruno.borges@oracle.com
# ==============================================
admin_port = int(os.environ.get("ADMIN_PORT", "7001"))
admin_pass = 'welcome1'
admin_listen_address = 'wlsadmin'
admin_nm_name = 'wlsadmin'
admin_nm_listen_port = 5556


ecup_ms_name = 'WLS_ECUP1'
ecup_ms_listen_address = 'wlsecup'
ecup_ms_listen_port = 7101
ecup_nm_name = 'wlsecup'
ecup_nm_listen_port = 5556
ecup_cluster_name = 'ECUP_CLUSTER'

# Open default domain template
# ======================
readTemplate("/u01/oracle/weblogic/wlserver/common/templates/domains/wls.jar")

# Configure the Administration Server and SSL port.
# =========================================================
cd('Servers/AdminServer')
set('ListenAddress', admin_listen_address)
set('ListenPort', admin_port)

create('AdminServer','SSL')
cd('SSL/AdminServer')
set('Enabled', 'True')
set('ListenPort', admin_port + 1)

cd('/Servers/AdminServer/SSL/AdminServer')
cmo.setHostnameVerificationIgnored(true)
cmo.setHostnameVerifier(None)
cmo.setTwoWaySSLEnabled(false)
cmo.setClientCertificateEnforced(false)

# Define the user password for weblogic
# =====================================
cd('/')
cd('Security/base_domain/User/weblogic')
cmo.setPassword(admin_pass)

# Create a JMS Server
# ===================
cd('/')
create('myJMSServer', 'JMSServer')

# Create a JMS System resource
# ============================
cd('/')
create('myJmsSystemResource', 'JMSSystemResource')
cd('JMSSystemResource/myJmsSystemResource/JmsResource/NO_NAME_0')

# Create a JMS Queue and its subdeployment
# ========================================
myq=create('myQueue','Queue')
myq.setJNDIName('jms/myqueue')
myq.setSubDeploymentName('myQueueSubDeployment')

cd('/')
cd('JMSSystemResource/myJmsSystemResource')
create('myQueueSubDeployment', 'SubDeployment')

# Create and configure a JDBC Data Source, and sets the JDBC user
# ===============================================================
# IF YOU WANT TO HAVE A DEFAULT DATA SOURCE CREATED, UNCOMMENT THIS SECTION BEFORE BUILD

# cd('/')
# create('myDataSource', 'JDBCSystemResource')
# cd('JDBCSystemResource/myDataSource/JdbcResource/myDataSource')
# create('myJdbcDriverParams','JDBCDriverParams')
# cd('JDBCDriverParams/NO_NAME_0')
# set('DriverName','org.apache.derby.jdbc.ClientDriver')
# set('URL','jdbc:derby://localhost:1527/db;create=true')
# set('PasswordEncrypted', 'PBPUBLIC')
# set('UseXADataSourceInterface', 'false')
# create('myProps','Properties')
# cd('Properties/NO_NAME_0')
# create('user', 'Property')
# cd('Property/user')
# cmo.setValue('PBPUBLIC')

# cd('/JDBCSystemResource/myDataSource/JdbcResource/myDataSource')
# create('myJdbcDataSourceParams','JDBCDataSourceParams')
# cd('JDBCDataSourceParams/NO_NAME_0')
# set('JNDIName', java.lang.String("myDataSource_jndi"))

# cd('/JDBCSystemResource/myDataSource/JdbcResource/myDataSource')
# create('myJdbcConnectionPoolParams','JDBCConnectionPoolParams')
# cd('JDBCConnectionPoolParams/NO_NAME_0')
# set('TestTableName','SYSTABLES')

# Create Machine Admin
cd('/')
create(admin_nm_name,'Machine')

cd('/Machines/' + admin_nm_name  +'/')
create(admin_nm_name,'NodeManager')
cd('/Machines/' + admin_nm_name + '/NodeManager/' + admin_nm_name)
set('ListenAddress', admin_listen_address)
set('ListenPort', admin_nm_listen_port)
set('NMType','Plain')

# Create Machine ECUP
cd('/')
create(ecup_nm_name,'Machine')

cd('/Machines/' +  ecup_nm_name +'/')
create(ecup_nm_name,'NodeManager')
cd('/Machines/' + ecup_nm_name + '/NodeManager/' + ecup_nm_name)
set('ListenAddress', ecup_ms_listen_address)
set('ListenPort', ecup_nm_listen_port)
set('NMType','Plain')

# Create Cluster
cd('/')
create(ecup_cluster_name,'Cluster')

# Create MS
cd('/')
create(ecup_ms_name,'Server')

cd('/Servers/' + ecup_ms_name)
set('ListenPort',ecup_ms_listen_port)
set('ListenAddress', ecup_ms_listen_address)
set('Machine',ecup_nm_name)
assign('Server',ecup_ms_name,'Cluster',ecup_cluster_name)

# Asignar AdminServer a NodeManager
cd('/Servers/AdminServer')
set('Machine',admin_nm_name)

# Set NM Username and Password
#cd('/SecurityConfiguration/base_domain')
#set('NodeManagerUsername','weblogic')
#set('NodeManagerPasswordEncrypted','welcome1')

# Target resources to the servers
# ===============================
cd('/')
assign('JMSServer', 'myJMSServer', 'Target', 'AdminServer')
assign('JMSSystemResource.SubDeployment', 'myJmsSystemResource.myQueueSubDeployment', 'Target', 'myJMSServer')
# assign('JDBCSystemResource', 'myDataSource', 'Target', 'AdminServer')

# Write the domain and close the domain template
# ==============================================
setOption('OverwriteDomain', 'true')
setOption('ServerStartMode','prod')

cd('/')
writeDomain('/u01/oracle/weblogic/user_projects/domains/base_domain')
closeTemplate()

readDomain('/u01/oracle/weblogic/user_projects/domains/base_domain')
cd('/SecurityConfiguration/base_domain')
set('NodeManagerUsername','weblogic')
set('NodeManagerPasswordEncrypted','welcome1')
updateDomain()

# Exit WLST
# =========
exit()

