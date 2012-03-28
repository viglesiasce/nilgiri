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

# file: nilgiri/callbacks/keypairs/views.py

from django import shortcuts
from django.template.context import RequestContext
from django.http import HttpResponse

import dashboard.nilgiri.commands.euca.describegroups
import dashboard.nilgiri.commands.euca.addgroup
import dashboard.nilgiri.commands.euca.deletegroup
import dashboard.nilgiri.commands.euca.editgroup
import dashboard.nilgiri.commands.euca.authorize
import dashboard.nilgiri.commands.euca.revoke

def groups(request):
    context = { }
    template = 'groups/groups.html'
    return shortcuts.render_to_response(template, context, context_instance=RequestContext(request))

# all groups
def describe_groups(request):
    nilCmd = dashboard.nilgiri.commands.euca.describegroups.DescribeGroups()
    groups = nilCmd.main_cli()
    context = { 'groups': groups }
    template = 'groups/describe_groups.html'
    return shortcuts.render_to_response(template, context, context_instance=RequestContext(request))

# edit group
def edit_group(request):
    query = request.POST.get('group_name', '')
    nilCmd = dashboard.nilgiri.commands.euca.editgroup.EditGroup()
    groups = nilCmd.main_cli(query)
    context = { 'groups': groups }
    template = 'groups/edit_group.html'
    return shortcuts.render_to_response(template, context, context_instance=RequestContext(request))

def describe_group(request):
    query = request.POST.get('group_name', '')
    nilCmd = dashboard.nilgiri.commands.euca.editgroup.EditGroup()
    groups = nilCmd.main_cli(query)
    context = { 'groups': groups }
    template = 'groups/describe_group.html'
    return shortcuts.render_to_response(template, context, context_instance=RequestContext(request))

def create_group(request):
    query_name = request.POST.get('group_name', '')
    query_description = request.POST.get('group_description', '')
    nilCmd = dashboard.nilgiri.commands.euca.addgroup.AddGroup()
    group = nilCmd.main_cli(query_name, query_description)
    context = { 'group': group }
    template = 'groups/create_group.html'
    return shortcuts.render_to_response(template, context, context_instance=RequestContext(request))


def delete_group(request):
    query = request.POST.get('group_name', '')
    nilCmd = dashboard.nilgiri.commands.euca.deletegroup.DeleteGroup()
    status = nilCmd.main_cli(query)
    return HttpResponse(status)


def authorize_group(request):
    query_group_name = request.POST.get('group_name', '')
    query_ip_protocol = request.POST.get('ip_protocol', '')
    query_from_port = request.POST.get('from_port', '')
    query_to_port = request.POST.get('to_port', '')
    query_cidr_ip = request.POST.get('cidr_ip', '')
    nilCmd = dashboard.nilgiri.commands.euca.authorize.Authorize()
    status = nilCmd.main_cli(query_group_name, query_ip_protocol, query_from_port, query_to_port, query_cidr_ip)
    return HttpResponse(status)


def revoke_rules(request):
    query_group_name = request.POST.get('group_name', '')
    query_ip_protocol = request.POST.get('ip_protocol', '')
    query_from_port = request.POST.get('from_port', '')
    query_to_port = request.POST.get('to_port', '')
    query_cidr_ip = request.POST.get('cidr_ip', '')
    nilCmd = dashboard.nilgiri.commands.euca.revoke.Revoke()
    status = nilCmd.main_cli(query_group_name, query_ip_protocol, query_from_port, query_to_port, query_cidr_ip)
    return HttpResponse(status)