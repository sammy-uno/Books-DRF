#!/bin/bash
kill -9  $(pgrep waitress)

cd /home/ec2-user
source book-api/bin/activate
cd Books-DRF
export API_DEBUG=False
./startServer.sh &> Books-DRF.log &
ps -ef | grep waitress