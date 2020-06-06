python manage.py makemigrations
python manage.py migrate
git add .
git commit -m "Automatic Commit"
git push -u origin master
ssh -i "/atools/aws resources/ppkKey.pem" ubuntu@13.233.104.142 'cd /opt/eventBackend/EventRegistrationBackend/;git stash;git pull;pm2 restart 2;'
