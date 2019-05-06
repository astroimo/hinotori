#!/usr/bin/sh

TEMP=IF-Switch-Box.out
# ERROR NOW, MODIFY LATER
# ./dev3499n > $TEMP

## ---- OCTADv1 ----##
export LANG=C
HOST=192.168.5.181
PORT=5653
OUT=octadv1.out

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

## ---- OCTADv2 ----##
HOST2=192.168.5.181 ## TODO change it to ''192.168.5.182'' when it is good !
PORT2=5653
OUT2=octadv2.out

expect -c "
set timeout 5
spawn telnet $HOST2 $PORT2
log_file -noappend $OUT2
expect;                 send \"show_adcsmpbit1?;\n\"
expect;                 send \"show_adcsmpbit2?;\n\"
expect;                 send \"show_adcsmpbit3?;\n\"
expect;
expect;                 send \"^]\"
expect;'telnet>'        send \"q\n\"
"



echo #####$OUT is saved, now runnig python script#####
python bit_dist.py

# ERROR NOW, MODIFY LATER
#rm $TEMP
