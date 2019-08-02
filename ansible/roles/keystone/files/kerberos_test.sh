#!/bin/bash

kinit -t kerberos_demo_user.keytab -k kerberos_demo_user
curl -v -k -L --negotiate -u : -H 'content-type: application/json' -d @kerberos_auth.json -X POST http://keystone-idp/krb/identity/v3/auth/tokens
