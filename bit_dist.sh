#!/usr/bin/sh


export LANG=C
HOST=192.168.5.181
PORT=5653
OUT=log.log

expect -c "
set timeout 5
spawn telnet $HOST $PORT
log_file -noappend $OUT
expect;			send \"show_adcsmpbit1?;\n\"
expect;			send \"show_adcsmpbit2?;\n\"
expect;			send \"show_adcsmpbit3?;\n\"
expect;
expect;                 send \"\"
expect;'telnet>'        send \"q\n\"
"
echo #####$OUT is saved, now runnig python script#####
python bit_dist.py
