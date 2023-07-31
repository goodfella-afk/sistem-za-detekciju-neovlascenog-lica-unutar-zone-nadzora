#!/bin/bash

# Define colors...
RED=`tput bold && tput setaf 1`
GREEN=`tput bold && tput setaf 2`
YELLOW=`tput bold && tput setaf 3`
BLUE=`tput bold && tput setaf 4`
NC=`tput sgr0`

function RED(){
	echo -e "\n${RED}${1}${NC}"
}
function GREEN(){
	echo -e "\n${GREEN}${1}${NC}"
}
function YELLOW(){
	echo -e "\n${YELLOW}${1}${NC}"
}
function BLUE(){
	echo -e "\n${BLUE}${1}${NC}"
}

# Testing if root...
if [ $UID -ne 0 ]
then
	RED "You must run this script as root!" && echo
	exit
fi



BLUE "Updating repositories..."
sudo apt update

BLUE "Installing dlib..."
sudo pip install dlib==19.22

BLUE "Installing OpenCV..."
sudo pip install opencv-python

BLUE "Installing face_recognition.py..."
sudo pip install face_recognition

BLUE "Installing smtplib..."
sudo pip install smtplib

BLUE "Installing Shutil..."
sudo pip install shutil

BLUE "Installing RunPy..."
sudo pip install runpy

BLUE "Installing mySqlConnector..."
sudo pip install mysql-connector-python

BLUE "Installing SubPRocess..."
sudo pip install subprocess

BLUE "Installing numpy.."
sudo pip install numpy