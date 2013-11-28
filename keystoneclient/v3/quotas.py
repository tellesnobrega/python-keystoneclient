# Copyright 2011 OpenStack Foundation
# Copyright 2011 Nebula, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from keystoneclient import base


class DomainQuota(base.Resource):
    """Represents an domain Quota.
  
      """
    pass


class DomainQuotaManager(base.CrudManager):
    """Manager class for manipulating Identity domains."""
    resource_class = DomainQuota
    collection_key = 'domains'
    key = 'domain_id'

    def get(self, domain_id, region=None, services=None):
        return super(DomainQuotaManager, self).get_with_body(
            domain_id=base.getid(domain_id),
            region=region,
            services=services,
            complement='quotas')
