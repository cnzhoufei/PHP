#!/bin/bash
#logcut.sh

yesterday=`date -d yesterday +%Y%m%d`

srclog="/usr/local/apache2/logs/access_log"

dstlog="/usr/local/apache2/logsbak/access_${yesterday}.log"

mv $srclog $dstlog

pkill -1 httpd
