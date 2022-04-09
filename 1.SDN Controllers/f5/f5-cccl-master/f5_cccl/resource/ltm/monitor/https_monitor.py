"""Hosts an interface for the BIG-IP Monitor Resource.

This module references and holds items relevant to the orchestration of the F5
BIG-IP for purposes of abstracting the F5-SDK library.
"""
#
# Copyright 2017 F5 Networks Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import logging

from f5_cccl.resource.ltm.monitor import Monitor


LOGGER = logging.getLogger(__name__)


class HTTPSMonitor(Monitor):
    """Creates a CCCL BIG-IP HTTPS Monitor Object of sub-type of Resource

    This object hosts the ability to orchestrate basic CRUD actions against a
    BIG-IP HTTPS Monitor via the F5-SDK.

    The major difference is the afforded schema for HTTPS specifically.
    """
    properties = dict(interval=5,
                      timeout=16,
                      send="GET /\\r\\n",
                      recv="")

    def __init__(self, name, partition, **kwargs):
        super(HTTPSMonitor, self).__init__(name, partition, **kwargs)
        for key in ['send', 'recv']:
            self._data[key] = kwargs.get(key, self.properties.get(key))

    def _uri_path(self, bigip):
        """Get the URI resource path key for the F5-SDK for HTTPS monitor

        This is the URI reference for an HTTPS Monitor.
        """
        return bigip.tm.ltm.monitor.https_s.https


class ApiHTTPSMonitor(HTTPSMonitor):
    """Create the canonical HTTPS monitor from API input."""
    pass


class IcrHTTPSMonitor(HTTPSMonitor):
    """Create the canonical HTTPS monitor from iControl REST response."""
    pass
