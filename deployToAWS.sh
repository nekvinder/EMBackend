cd ../
zip -r b.zip EventRegistrationBackend/
curl --insecure -v -k --key "/atools/aws_resources/ppkKey.pem" sftp://ubuntu@13.233.104.142/opt/Backends/b.zip -T "b.zip"
ssh -i "/atools/aws_resources/ppkKey.pem" ubuntu@13.233.104.142 'cd /opt/Backends/;unzip -q -o b.zip;cd EventRegistrationBackend;pm2 start runWithSSL.json;'