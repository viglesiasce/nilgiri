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

# file: dashboard/urls.py

from django.conf.urls.defaults import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# for admin - class based view (to-do)
from admin.views import AdminView

urlpatterns = patterns('',
    url(r'^$', 'dashboard.views.home', name='home'),
    url(r'^home.html$', 'dashboard.views.home', name='home'),
    url(r'^admin/', AdminView.as_view()),
    
    # instances
    url(r'^instances/describe_instances$', 'callbacks.instances.views.describe_instances', name='describe_instances'),
    url(r'^instances/terminate_instances$', 'callbacks.instances.views.terminate_instances', name='terminate_instances'),
    url(r'^instances/run_instances$', 'callbacks.instances.views.run_instances', name='run_instances'),
    url(r'^instances/launch_instance$', 'callbacks.instances.views.launch_instance', name='launch_instance'),
    
    # images
    url(r'^images/describe_images$', 'callbacks.images.views.describe_images', name='describe_images'),
    
    # keypairs
    url(r'^keypairs/keypairs$', 'callbacks.keypairs.views.keypairs', name='keypairs'),
    url(r'^keypairs/describe_keypairs$', 'callbacks.keypairs.views.describe_keypairs', name='describe_keypairs'),
    url(r'^keypairs/delete_keypair$', 'callbacks.keypairs.views.delete_keypair', name='delete_keypair'),
    url(r'^keypairs/create_keypair$', 'callbacks.keypairs.views.create_keypair', name='create_keypair'),
    
    # groups
    url(r'^groups/groups$', 'callbacks.groups.views.groups', name='groups'),
    url(r'^groups/describe_groups$', 'callbacks.groups.views.describe_groups', name='describe_groups'),
    url(r'^groups/create_group$', 'callbacks.groups.views.create_group', name='create_group'),
    url(r'^groups/delete_group$', 'callbacks.groups.views.delete_group', name='delete_group'),
    url(r'^groups/edit_group$', 'callbacks.groups.views.edit_group', name='edit_group'),
    url(r'^groups/authorize_group$', 'callbacks.groups.views.authorize_group', name='authorize_group'),
    url(r'^groups/describe_group$', 'callbacks.groups.views.describe_group', name='describe_group'),
    url(r'^groups/revoke_rules$', 'callbacks.groups.views.revoke_rules', name='revoke_rules'),
    
    # volumes
    url(r'^volumes/describe_volumes$', 'callbacks.volumes.views.describe_volumes', name='describe_volumes'),
    url(r'^volumes/create_volume_view$', 'callbacks.volumes.views.create_volume_view', name='create_volume_view'),
    
    
    url(r'^dajax/$', 'callbacks.views.dajax', name='dajax'),
    
    url(r'^dajax/dajax.html$', 'callbacks.views.dajax', name='dajax'),
    url(r'^dajax/results.html$', 'callbacks.views.xhr_test', name='xhr_test'),
    url(r'^xhr_test$', 'callbacks.views.xhr_test', name='xhr_test'),
    
    # fixed
#    url(r'^show_instances$', 'callbacks.views.show_instances', name='show_instances'),
#    url(r'^describe_volumes$', 'callbacks.views.describe_volumes', name='describe_volumes'),
#    url(r'^terminate_instance$', 'callbacks.views.terminate_instance', name='terminate_instance'),
#    url(r'^show_images$', 'callbacks.views.show_images', name='show_images'),
#    url(r'^available_keypairs$', 'callbacks.views.available_keypairs', name='available_keypairs'),
#    url(r'^show_groups$', 'callbacks.views.show_groups', name='show_groups'),
#    url(r'^launch_verify$', 'callbacks.views.launch_verify', name='launch_verify'),
#    url(r'^start_instances$', 'callbacks.views.start_instances', name='start_instances'),
#    url(r'^add_keypair$', 'callbacks.views.add_keypair', name='add_keypair'),
#    url(r'^delete_key$', 'callbacks.views.delete_key', name='delete_key'),
#    url(r'^select_keypairs$', 'callbacks.views.select_keypairs', name='select_keypairs'),
    
    # Examples: 
    # url(r'^$', 'nilgiri.views.home', name='home'),
    # url(r'^nilgiri/', include('nilgiri.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
