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

# file: nilgiri/callbacks/instances/views.py

from django import shortcuts
from django.template.context import RequestContext
from django.http import HttpResponse

import dashboard.nilgiri.commands.euca.describeinstances
import dashboard.nilgiri.commands.euca.terminateinstances
import dashboard.nilgiri.commands.euca.runinstances


def describe_instances(request):
    feed = request.POST.get('feed', '')
    nilCmd = dashboard.nilgiri.commands.euca.describeinstances.DescribeInstances()
    reservations = nilCmd.main_cli()
    context = { 'reservations': reservations }
    if not feed:
        template = 'instances/describe_instances.html'
        return shortcuts.render_to_response(template, context, context_instance=RequestContext(request))
    else:
        if feed == "volume_feed":
            template = 'instances/instance_ids.html'
            return shortcuts.render_to_response(template, context, context_instance=RequestContext(request))


def terminate_instances(request):
    query = request.POST.get('id', '')
    nilCmd = dashboard.nilgiri.commands.euca.terminateinstances.TerminateInstances()
    instances = nilCmd.main_cli(query)
    return HttpResponse(instances)

def launch_instance(request):
    query_key = request.POST.get('selected_key', '')
    query_image = request.POST.get('selected_image', '')
    query_group = request.POST.get('selected_group', '')
    context = { 'image': query_image, 'key': query_key, 'group': query_group }
    template = "instances/launch_instance.html"
    return shortcuts.render_to_response(template, context, context_instance=RequestContext(request))


def run_instances(request):
    # run instance
    query_key = request.POST.get('selected_key', '')
    query_image = request.POST.get('selected_image', '')
    query_groups = request.POST.get('selected_group', '')
    query_instance_type = request.POST.get('instance_type', '')
    query_addressing_type = request.POST.get('addressing_type', '')
    
    groups = []
    groups.append(query_groups)
    nilCmd = dashboard.nilgiri.commands.euca.runinstances.RunInstances()
    reservation = nilCmd.main_cli(query_image, query_key, groups, query_instance_type, query_addressing_type)
    context = { 'reservation': reservation }
    template = "instances/new_instance.html"
    return shortcuts.render_to_response(template, context, context_instance=RequestContext(request))