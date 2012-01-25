#!/bin/bash

APP_NAME=acquaniebla
INSTALL_DIR=/$APP_NAME
echo "****************AcquaInstaller****************"
echo "Will install in " $INSTALL_DIR

mkdir $INSTALL_DIR
mkdir $INSTALL_DIR/log
mkdir $INSTALL_DIR/db
mkdir $INSTALL_DIR/watchdog
mkdir $INSTALL_DIR/scripts

chmod 777 $INSTALL_DIR/log
chmod 777 $INSTALL_DIR/db

cp -rv app/* $INSTALL_DIR
cp -rv scripts/watchdog.* $INSTALL_DIR/watchdog
cp -v scripts/*.sh $INSTALL_DIR/scripts/
cp -v scripts/acquaniebla.cron /etc/cron.d/acquaniebla

ln -sf /acquaniebla/scripts/acquaniebla.sh /etc/init.d/acquaniebla.sh
ln -sf /etc/init.d/acquaniebla.sh /etc/rc5.d/S20acquaniebla

