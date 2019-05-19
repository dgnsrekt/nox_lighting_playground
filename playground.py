from lnd_grpc import Client
from pathlib import Path

ROOT_DIR = Path(__file__).parent
LND_DIR = ROOT_DIR / ".lnd/"
NETWORK = "testnet"
client = Client(lnd_dir=str(LND_DIR), network=NETWORK)

print(client.version)
print(client.get_info())
print(client.wallet_balance())
print(client.channel_balance())
print(client.list_peers())
print(client.new_address(address_type="p2wkh"))
