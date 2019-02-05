import hashlib
import sys


issuer_dn = sys.argv[1]
hashed_idp = hashlib.sha256(issuer_dn)
idp_id = hashed_idp.hexdigest()
print(idp_id)

