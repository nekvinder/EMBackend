cd ../
zip -r b.zip EventRegistrationBackend/
curl --insecure -v -k --key "/atools/aws_resources/ppkKey.pem" sftp://ubuntu@nekvinder.com/opt/Backends/b.zip -T "b.zip"
ssh -i "/atools/aws_resources/ppkKey.pem" ubuntu@nekvinder.com 'cd /opt/Backends/;unzip -q -o b.zip;cd EventRegistrationBackend;pm2 start runWithSSL.json;'