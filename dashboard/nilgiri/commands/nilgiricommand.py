# Software License Agreement (BSD License)
#
# Copyright (c) 2009-2011, Eucalyptus Systems, Inc.
# All rights reserved.
#
# Redistribution and use of this software in source and binary forms, with or
# without modification, are permitted provided that the following conditions
# are met:
#
#   Redistributions of source code must retain the above
#   copyright notice, this list of conditions and the
#   following disclaimer.
#
#   Redistributions in binary form must reproduce the above
#   copyright notice, this list of conditions and the
#   following disclaimer in the documentation and/or other
#   materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Author: Imran Hossain Shaon mdshaonimran@gmail.com

# file: nilgiri/dashboard/nilgiri/commands/nilgiricommand.py

import nilgiri
import getopt
import sys
import os
import textwrap
import urlparse
import boto
from boto.ec2.regioninfo import RegionInfo
from boto.s3.connection import OrdinaryCallingFormat
from boto.ec2.blockdevicemapping import BlockDeviceMapping, BlockDeviceType
from boto.roboto.param import Param

class NilgiriCommand(object):
    
    def __init__(self, is_euca=False, debug=False):
        self.region = RegionInfo()
        self.filters = {}
        self.ec2_user_access_key = 'WKy3rMzOWPouVOxK1p3Ar1C2uRBwa2FBXnCw'
        self.ec2_user_secret_key = 'PWdVhAPsGqQxZkdOSucsMWgQiZm1cQBNcITSQ'


    def make_ec2_connection(self):
        self.is_secure = True
        self.debug = 1
        self.region.name = 'eucalyptus'
        self.region.endpoint = '111.221.6.222'
        self.service_path = '/services/Eucalyptus'
        self.port = 8773

        return boto.connect_ec2(aws_access_key_id=self.ec2_user_access_key,
                                aws_secret_access_key=self.ec2_user_secret_key,
                                is_secure=self.is_secure,
                                region=self.region,
                                port=self.port,
                                path=self.service_path,
                                debug=self.debug)

    def make_connection(self, conn_type='ec2'):
        if conn_type == 's3':
            conn = self.make_s3_connection()
        elif conn_type == 'ec2':
            conn = self.make_ec2_connection()
        else:
            conn = None
        return conn

    def make_connection_cli(self, conn_type='ec2'):
        conn = self.make_connection(conn_type)
        return conn
    
    def make_request_cli(self, connection, request_name, **params):
        method = getattr(connection, request_name)
        return method(**params)
    
    
    
    # done
    def nversion(self):
        return nilgiri.__version__