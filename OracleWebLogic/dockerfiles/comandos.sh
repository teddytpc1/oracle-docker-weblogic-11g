git clone https://github.com/teddytpc1/oracle-docker-weblogic-11g.git
docker pull soporteayi/weblogic:10.3.6
mkdir -p /D01/arcor/domain/
sudo useradd -u 10500 -m arcor
sudo groupmod -g 10500 arcor
sudo  chown arcor:arcor /D01/arcor/domain/ 
sudo chmod  777 /D01/arcor/domain/
cd /home/corvaadm/wls/oracle-docker-weblogic-11g/OracleWebLogic/dockerfiles
./buildWLDomain.sh
