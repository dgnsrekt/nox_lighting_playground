from invoke import task, Responder
from pathlib import Path

ROOT_DIR = Path(__file__).parent

BIN_DIR = ROOT_DIR / "bin"
LND_DIR = ROOT_DIR / ".lnd"
VERSION = "v0.6.1-beta"
FILENAME = f"lnd-linux-amd64-{VERSION}"
ZIPNAME = f"{FILENAME}.tar.gz"
LND_URL = f"https://github.com/lightningnetwork/lnd/releases/download/{VERSION}/{ZIPNAME}"


@task
def download(c):
    print("downloading")
    c.run(f"wget --no-clobber {LND_URL}")


@task(download)
def unzip(c):
    print("unzipping")
    c.run(f"mkdir -p {BIN_DIR}")
    c.run(f"tar -xzf {ZIPNAME} -C {BIN_DIR}")

    if not Path(f"{BIN_DIR}/lnd").exists():
        c.run(f"cp {BIN_DIR}/{FILENAME}/lnd {BIN_DIR}")
    if not Path(f"{BIN_DIR}/lncli").exists():
        c.run(f"cp {BIN_DIR}/{FILENAME}/lncli {BIN_DIR}")

    c.run(f"rm -rf {BIN_DIR}/{FILENAME}", pty=True)


@task(unzip)
def server(c):
    c.run(
        f"{BIN_DIR}/lnd --bitcoin.active --bitcoin.testnet --debuglevel=info --bitcoin.node=neutrino --neutrino.connect=faucet.lightning.community --lnddir={LND_DIR}"
    )


@task(unzip)
def unlock(c):
    c.run(f"{BIN_DIR}/lncli --network=testnet --lnddir={LND_DIR} unlock", pty=True)


@task(unzip)
def create(c):
    c.run(f"{BIN_DIR}/lncli --network=testnet --lnddir={LND_DIR} create", pty=True)
