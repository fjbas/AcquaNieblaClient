#!/bin/bash

APP_NAME=acquaniebla_installer
INSTALL_DIR=/$APP_NAME
echo "****************AcquaInstaller****************"
echo "Will install in " $INSTALL_DIR

mkdir $INSTALL_DIR
mkdir $INSTALL_DIR/log
mkdir $INSTALL_DIR/db
mkdir $INSTALL_DIR/watchdog

cp -rv app/* $INSTALL_DIR
cp -rv scripts/watchdog.* $INSTALL_DIR/watchdog


