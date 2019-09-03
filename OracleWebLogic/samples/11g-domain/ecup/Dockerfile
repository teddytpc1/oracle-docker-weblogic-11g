# LICENSE CDDL 1.0 + GPL 2.0
#
# ORACLE DOCKERFILES PROJECT
# --------------------------
# This Dockerfile extends an Oracle WebLogic image by creating a sample domain.
# Util scripts are copied into the image enabling users to plug NodeManager 
# magically into the AdminServer running on another container as a Machine.
#
# HOW TO BUILD THIS IMAGE
# -----------------------
# Put all downloaded files in the same directory as this Dockerfile
# Run: 
#      $ sudo docker build -t myweblogic .
#

# Pull base image
# ---------------
FROM oracle/weblogic:10.3.6-wlsadmin2

# Maintainer
# ----------
MAINTAINER Bruno Borges <bruno.borges@oracle.com>

# Final setup
WORKDIR /u01/oracle

ENV PATH $PATH:/u01/oracle/weblogic/wlserver/server/bin:/u01/oracle/weblogic/wlserver/common/bin:/u01/oracle/weblogic/user_projects/domains/base_domain/bin:/u01/oracle
ENV SERVER_NAME WLS_ECUP1
ENV ADMIN_URL http://wlsadmin:7001

# Define default command to start bash. 
#ENTRYPOINT ["startManagedWebLogic.sh"]
#CMD ["WLS_ECUP1 http://wlsadmin:7001"]

#RUN ["/u01/oracle/scripts/start.sh"]
