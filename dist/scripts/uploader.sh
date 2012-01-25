#°/bin/bash

cat /acquaniebla/log/uploader.last >> /acquaniebla/log/uploader.log
/usr/bin/python /acquaniebla/acquauploader.py > /acquaniebla/log/uploader.last

