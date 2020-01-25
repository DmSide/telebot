To proxy I try to use
https://hub.docker.com/r/dijedodol/simple-socks5-server/
snap install docker

THe run:
docker run -it --rm -p 1080:1080 -e 'SSS_USERNAME=dijedodol' -e 'SSS_PASSWORD=demo' dijedodol/simple-socks5-server

the proxy has structure {login:pass@host:port}
