connect('weblogic','welcome1','t3://wlsadmin:7001')
ms_name = sys.argv[1]
ms_listen_address = sys.argv[2]
ms_cluster_name = sys.argv[3]
ms_listen_port = sys.argv[4]

print '===> Server \"' +ms_name+'\" s'


try:
 cd('/Servers/' + ms_name)
 print '===> Server \"' +ms_name+'\" already exists'
 print '===> No action was performed'
 exit()
except:
 pass
 print '===> Server \"' +ms_name+'\" does not exists'
 print '===> It will be created'
 
 edit()
 startEdit()
 try:
     cd('/Clusters/' + ms_cluster_name)
 # Create Cluster
 print '===> Cluster \"' +ms_cluster_name+'\" already exists'
 print '===> No action was performed'
 exit()
 except:
  pass
  cd('/')
  create(ms_cluster_name,'Cluster')

  # Create MS
  print '===> Creating MS' + ms_name'
  cd('/')
  create(ms_name,'Server')

  cd('/Servers/' + ms_name)
  set('ListenPort', ms_listen_port)
  set('ListenAddress', ms_listen_address)
  assign('Server',ms_name,'Cluster',ms_cluster_name)


  save()
  activate()
