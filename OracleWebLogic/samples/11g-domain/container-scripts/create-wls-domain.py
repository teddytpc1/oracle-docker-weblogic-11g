# Weblogic on Docker Default Domain
#
# Default domain 'base_domain' to be created inside the Docker image for WLS
#
# Since : October, 2014
# Author: bruno.borges@oracle.com
# ==============================================
admin_port = int(os.environ.get("ADMIN_PORT", "7001"))
admin_pass = os.environ.get("ADMIN_PASSWORD", "welcome1")

# Open default domain template
# ======================
readTemplate("/u01/oracle/weblogic/wlserver/common/templates/domains/wls.jar")

# Configure the Administration Server and SSL port.
# =========================================================
cd('Servers/AdminServer')
set('ListenAddress','0.0.0.0')
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

# Create Machine
cd('/')
create('ArcorDevops','Machine')

cd('/Machines/ArcorDevops/')
create('ArcorDevops','NodeManager')
cd('/Machines/ArcorDevops/NodeManager/ArcorDevops')
set('ListenAddress','172.17.0.2')
set('ListenPort',5557)
set('NMType','Plain')

# Create Cluster
cd('/')
create('ECUP_CLUSTER','Cluster')

# Create MS
cd('/')
create('WLS_ECUP1','Server')

cd('/Servers/WLS_ECUP1')
set('ListenPort',7101)
set('ListenAddress','172.17.0.2')
set('Machine','ArcorDevops')
assign('Server','WLS_ECUP1','Cluster','ECUP_CLUSTER')

# Asignar AdminServer a NodeManager
cd('/Servers/AdminServer')
set('Machine','ArcorDevops')


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

# Exit WLST
# =========
exit()

