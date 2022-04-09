#login credentials for InfluxDB

USER = 'root'
PASSWORD = 'root'
DBNAME = 'firewall_inspect'

host='localhost'
port=8086

series = []
total_records = 0

json_body = {}

#loop over the API response variable items and create records to be stored in InfluxDB

for i in items:
    json_body = { "measurement": "firewall_inspect_count",
                   "tags": {
                                "host": "wan_edge",
                           },
                  "time": time.strftime('%m/%d/%Y %H:%M:%S',  time.gmtime(i['entry_time']/1000.)),
                  "fields": {
                             "value": float(i['fw_total_insp_count'])
                 }
                 }
    series.append(json_body)
    total_records = total_records+1

client = InfluxDBClient(host, port, USER, PASSWORD, DBNAME)

print("Create a retention policy")
retention_policy = 'retention_policy_1'
client.create_retention_policy(retention_policy, '10d', 3, default=True)

print("Write points #: {0}".format(total_records))
client.write_points(series, retention_policy=retention_policy)

time.sleep(2)
