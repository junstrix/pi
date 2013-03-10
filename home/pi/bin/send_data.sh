#! /bin/bash

cd /home/pi/bin/cosm/
sed 's/\([0-9]*\.[0-9][0-9]\) \([0-9]*\.[0-9][0-9]\) \([0-9]*\.[0-9][0-9]\)\(.*\)/{"datastreams":[ {"id":"5min","current_value":"\1"},{"id":"10min","current_value":"\2"},{"id":"15min","current_value":"\3"} ]}/' /proc/loadavg > cosm-load.json
curl --request PUT --data-binary @cosm-load.json --header "X-ApiKey: oXsirKpAjZwkkZNzuZ_tAdDnDTeSAKxyVzgyYTFnWC9DRT0g" http://api.cosm.com/v2/feeds/117008?timezone=+8

VAL=`cat /sys/class/thermal/thermal_zone0/temp`
STR=`awk 'BEGIN{printf "{\"datastreams\":[ {\"id\":\"temp\",\"current_value\":\"%.1f\"} ] } ",'$VAL'/1000}'`
echo $STR > cosm_temp.json
curl --request PUT --data-binary @cosm_temp.json --header "X-ApiKey: oXsirKpAjZwkkZNzuZ_tAdDnDTeSAKxyVzgyYTFnWC9DRT0g" http://api.cosm.com/v2/feeds/117008?timezone=+8
