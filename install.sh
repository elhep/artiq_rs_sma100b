#!/bin/bash

apt-get install -y wget
wget https://scdn.rohde-schwarz.com/ur/pws/dl_downloads/dl_application/application_notes/1dc02___rs_v/rsvisa_5.12.9_amd64.deb -O /tmp/rsvisa_5.12.9_amd64.deb
dpkg -i /tmp/rsvisa_5.12.9_amd64.deb || apt-get install -f -y
rm /tmp/rsvisa_5.12.9_amd64.deb && apt-get clean && rm -rf /var/lib/apt/lists/*

