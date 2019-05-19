from lnd_grpc import Client
from pathlib import Path

root_path = Path(__file__).parent
lnd_path = root_path / ".lnd"
print(lnd_path)

x = Client(lnd_dir=str(lnd_path))
print(x.get_info())
