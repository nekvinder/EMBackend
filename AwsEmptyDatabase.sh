ssh -i "/atools/aws resources/ppkKey.pem" ubuntu@13.233.104.142 'cd /opt/eventBackend/EventRegistrationBackend/;rm db3.sqlite3;python3 manage.py migrate;pm2 restart 2;'
