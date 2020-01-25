To proxy I try to use
https://hub.docker.com/r/dijedodol/simple-socks5-server/
snap install docker

THe run:
docker run -it --rm -p 1080:1080 -e 'SSS_USERNAME=dijedodol' -e 'SSS_PASSWORD=demo' dijedodol/simple-socks5-server

the proxy has structure {login:pass@host:port}

telethon docs
https://buildmedia.readthedocs.org/media/pdf/telethon/stable/telethon.pdf

apt update
apt install clang lib{jpeg-turbo,webp}-dev python{,-dev} zlib-dev
pip install -U --user setuptools
pip install -U --user telethon cryptg pillow