#!/bin/bash
source book-api/bin/activate
cd /home/ec2-user/Books-RDF
export API_DEBUG=False
./startServer.sh &> Books-DRF.log &
echo "Hello"
echo (ps -ef | grep waitres)