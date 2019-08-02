# keystone-devel

# To test tokenless auth

curl --cacert /etc/keystone/ca.pem --cert user_cert.pem --key user_private_key.pem https://192.168.0.10/identity/v3/projects -H 'X-project-name: admin' -H 'x-project-domain-name: Default' | python -m json.tool

