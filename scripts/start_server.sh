#!/bin/bash
cd /home/ec2-user
source book-api/bin/activate
cd Books-RDF
export API_DEBUG=False
./startServer.sh &> Books-DRF.log &
ps -ef | grep waitress