#!/usr/bin/env bash

NOTIF_1="[*]Running server dependecies installation..."
NOTIF_2="[*]Creating directory..."
NOTIF_3="[*]Cloning from repository..."
NOTIF_4="[*]Running core application dependecies installation..."
NOTIF_5="[*]Moving core project to recently created file @ /server/file..."
NOTIF_6="[*]Deleting unnecessary folder..."
NOTIF_7="[*]Creating nginx virtual server @ /server/config/..."
NOTIF_8="[*]Creating script for starting gunicorn @ /server/config/application..."
NOTIF_9="[*]Creating upstart script for gunicorn executable file @ /server/application..."
NOTIF_10="[*]Creating and configuring database..."
NOTIF_11="[*]Finishing installation..."
NOTIF_12="[*]Installation finish..."

echo "$(tput setaf 1) $(tput bold) $NOTIF_1"
apt-get update
apt-get -y install software-properties-common python3 python3-dev libmariadbclient-dev build-essential python3-setuptools install libssl-dev git
easy_install-3.4 install pip
apt-key adv -y --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xcbcb082a1bb943db
add-apt-repository -y 'deb [arch=amd64,i386,ppc64el] http://kodeterbuka.beritagar.id/mariadb/repo/10.1/ubuntu trusty main'
add-apt-repository -y ppa:nginx/stable
apt-get update && apt-get install -y mariadb-server nginx

echo "$(tput setaf 1) $(tput bold) $NOTIF_2"
cd / && mkdir /server/ && mkdir /server/file/ && mkdir /server/config && mkdir /server/log && cd /server/file

echo "$(tput setaf 1) $(tput bold) $NOTIF_3"
cd /server/file/
git clone https://github.com/SufferProgrammer/manga-project-AManga.git
cd manga-project-AManga/
git branch -d origin/desktop

echo "$(tput setaf 1) $(tput bold) $NOTIF_4"
cd /server/file/
pip3.4 install -r requirements.txt

echo "$(tput setaf 1) $(tput bold) $NOTIF_5"
cd /server/file/
mv manga-project-AManga/application/ /server/file
mv manga-project-AManga/amvenv/ /server/file/
mv manga-project-AManga/.git/ /server/file
mv manga-project-AManga/.gitignore /server/file
mv manga-project-AManga/requirements.txt /server/file
mv manga-project-AManga/script /server/config/

echo "$(tput setaf 1) $(tput bold) $NOTIF_6"
rm -r manga-project-AManga

echo "$(tput setaf 1) $(tput bold) $NOTIF_7"
cd /server/config/script/
cat nginx_conf >> /server/config/amangaservconf
cd /server/config
ln -s /server/config/amangaservconf /etc/nginx/sites-enabled/

echo "$(tput setaf 1) $(tput bold) $NOTIF_8"
cd /server/config/script/
cat gunicorn.conf.start >> /server/file/application/gunFlask.sh
cd /server/file/application && chmod +x gunFlask.sh

echo "$(tput setaf 1) $(tput bold) $NOTIF_9"
cd /server/config/script/
cat upstat_service.conf >> /etc/init/amangaserv.conf

echo "$(tput setaf 1) $(tput bold) $NOTIF_10"
python3 pyExecuter.py

echo "$(tput setaf 1) $(tput bold) $NOTIF_11"
service nginx restart && service amangaserv start

echo "$(tput setaf 2) $(tput bold) $(tput bel) $NOTIF_12"