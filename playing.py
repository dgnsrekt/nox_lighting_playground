from lnd_grpc.lnd_grpc import Client
from pathlib import Path

ROOT_DIR = Path(__file__).parent

LND_DIR = ROOT_DIR / ".lnd/"
TLS_CERT = LND_DIR / "tls.cert"
MACAROON = LND_DIR / "data/chain/bitcoin/testnet/admin.macaroon"

print(TLS_CERT, "exists", TLS_CERT.exists())
print(MACAROON, "exists", MACAROON.exists())

stub = Client(tls_cert_path=TLS_CERT, macaroon_path=MACAROON)

print(stub.version)
print(stub.get_info())
# print(stub.wallet_balance())
# print(stub.channel_balance())
# print(stub.list_peers())
# print(stub.new_address(address_type="p2wkh"))
