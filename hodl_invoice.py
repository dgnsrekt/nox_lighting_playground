from lnd_grpc import Client
from lnd_grpc.protos import rpc_pb2 as ln

from random import randint
from hashlib import sha256
from time import sleep

from pathlib import Path

ROOT_DIR = Path(__file__).parent
LND_DIR = ROOT_DIR / ".lnd/"
NETWORK = "testnet"

client = Client(lnd_dir=str(LND_DIR), network=NETWORK)


def create_random_hash():
    n = str(randint(0, 1e32))
    hash = sha256(n.encode())
    return hash.digest(), n


HASH, PREIMAGE = create_random_hash()
MEMO = "TESTING HODL INVOICES"
SATOSHIS = 10

print("HASH", HASH, type(HASH))
print("PREIMAGE", PREIMAGE)

invoice = client.add_hold_invoice(memo=MEMO, hash=HASH, value=SATOSHIS)
single_sub = client.subscribe_single_invoice(r_hash=HASH)

for status in single_sub:
    print("status:", status.state)
    print(status)
    if status.state == 3:
        print("ACCEPTED")
        print("VERIFYING SOMETHING", end="")
        for _ in range(10):
            print(".", end="", flush=True)
            sleep(1)
        else:
            print()
        if randint(0, 1):
            print("EVERYTHING LOOKS GOOD. SETTLING PAYMENT.")
            sleep(1)
            client.settle_invoice(preimage=PREIMAGE.encode())
            print("PAYMENT SETTLED!")
            sleep(1)
        else:
            print("OH NO! SOMETHING WENT WRONG. CANCELING PAYMENT.")
            sleep(1)
            client.cancel_invoice(HASH)
            print("PAYMENT CANCELED!")
            sleep(1)
        break
    else:
        print(status)
        sleep(1)
