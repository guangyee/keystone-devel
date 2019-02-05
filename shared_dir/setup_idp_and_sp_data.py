#!/bin/bash

set -e

source ~/devstack/openrc admin admin

openstack service provider create --service-provider-url http://localhost/Shibboleth.sso/SAML2/ECP --auth-url  http://localhost/identity/v3/OS-FEDERATION/identity_providers/myidp/protocols/saml2/auth mysp

openstack identity provider create --remote-id http://localhost/v3/OS-FEDERATION/saml2/idp myidp
#openstack domain create federated_domain
#openstack project create federated_project --domain federated_domain
#openstack group create federated_users
openstack role add --group federated_users --domain federated_domain Member
openstack role add --group federated_users --project federated_project Member
openstack mapping create --rules k2k_mapping.json myidp_mapping
openstack federation protocol create saml2 --mapping myidp_mapping --identity-provider myidp

openstack group add user --group-domain federated_domain --user-domain Default federated_users admin
