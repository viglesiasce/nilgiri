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

# file: nilgiri/callbacks/volumes/views.py

from django import shortcuts
from django.template.context import RequestContext
from django.http import HttpResponse

import dashboard.nilgiri.commands.euca.describevolumes
import dashboard.nilgiri.commands.euca.createvolume
import dashboard.nilgiri.commands.euca.deletevolume
import dashboard.nilgiri.commands.euca.attachvolume
import dashboard.nilgiri.commands.euca.detachvolume

def describe_volumes(request):
    nilCmd = dashboard.nilgiri.commands.euca.describevolumes.DescribeVolumes()
    volumes = nilCmd.main_cli()
    context = { 'volumes': volumes }
    template = 'volumes/describe_volumes.html'
    return shortcuts.render_to_response(template, context, context_instance=RequestContext(request))


def create_volume_view(request):
    context = { }
    template = 'volumes/create_volume.html'
    return shortcuts.render_to_response(template, context, context_instance=RequestContext(request))


def create_volume(request):
    query_vol_size = request.POST.get('vol_size', '')
    query_vol_zone = request.POST.get('vol_zone', '')
    nilCmd = dashboard.nilgiri.commands.euca.createvolume.CreateVolume()
    volume = nilCmd.main_cli(query_vol_size, query_vol_zone)
    context = { 'volume': volume }
    template = 'volumes/new_volume.html'
    return shortcuts.render_to_response(template, context, context_instance=RequestContext(request))


def delete_volume(request):
    query_vol_id = request.POST.get('vol_id', '')
    nilCmd = dashboard.nilgiri.commands.euca.deletevolume.DeleteVolume()
    status = nilCmd.main_cli(query_vol_id)
    return HttpResponse(status)


def attach_volume(request):
    query_vol_id = request.POST.get('vol_id', '')
    query_instance_id = request.POST.get('instance_id', '')
    query_device_name = request.POST.get('device_name', '')
    nilCmd = dashboard.nilgiri.commands.euca.attachvolume.AttachVolume()
    status = nilCmd.main_cli(query_vol_id, query_instance_id, query_device_name)
    return HttpResponse(status)


def detach_volume(request):
    query_volume_id = request.POST.get('vol_id', '')
    nilCmd = dashboard.nilgiri.commands.euca.detachvolume.DetachVolume()
    status = nilCmd.main_cli(query_volume_id)
    return HttpResponse(status)