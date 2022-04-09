import os
import sys

import ciscosparkapi

# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))

# Get the absolute path for the project / repository root
project_root = os.path.abspath(os.path.join(here, "../.."))

# Extend the system path to include the project root and import the env files
sys.path.insert(0, project_root)
import env_lab  # noqa
import env_user  # noqa

spark = ciscosparkapi.CiscoSparkAPI(access_token=env_user.SPARK_ACCESS_TOKEN)

print(
    """
My Lab Environment:
    DNA Center Host: {dnac_host}
    DNA Center Username: {dnac_user}
    DNA Center Password: {dnac_pass}
""".format(
        dnac_host=env_lab.DNA_CENTER["host"],
        dnac_user=env_lab.DNA_CENTER["username"],
        dnac_pass=env_lab.DNA_CENTER["password"],
    )
)

print("Oh yeah... I'm also connected to Cisco Spark as:")
print(spark.people.me())

print("...and I'm posting things to the following Spark Room:")
print(spark.rooms.get(env_user.SPARK_ROOM_ID))
