ssh -i "/atools/aws resources/ppkKey.pem" ubuntu@13.233.104.142 'cd /opt/Backends/GMS/;rm db3.sqlite3;python3 manage.py migrate'
