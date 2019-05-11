import nox
from pathlib import Path

ROOT_DIR = Path(__file__).parent
LND_DIR = ROOT_DIR / ".lnd"

nox.options.envdir = str(ROOT_DIR)


@nox.session
def server(session):
    """Setup"""
    session.run("rm", "-f", "lnd-linux-amd64-v0.6.1-beta.tar.gz", external=True)
    session.run("rm", "-rf", "lnd-linux-amd64-v0.6.1-beta", external=True)

    session.run(
        "wget",
        "https://github.com/lightningnetwork/lnd/releases/download/v0.6.1-beta/lnd-linux-amd64-v0.6.1-beta.tar.gz",
        external=True,
    )

    session.run("tar", "-xzf", "lnd-linux-amd64-v0.6.1-beta.tar.gz", external=True)
    session.run("ls", external=True)
    session.run("cp", "lnd-linux-amd64-v0.6.1-beta/lnd", session.bin, external=True)
    # session.run("cp", "lnd-linux-amd64-v0.6.1-beta/lncli", session.bin, external=True)
    session.run("mkdir", "-p", str(LND_DIR), external=True)

    session.run("rm", "-f", "lnd-linux-amd64-v0.6.1-beta.tar.gz", external=True)
    session.run("rm", "-rf", "lnd-linux-amd64-v0.6.1-beta", external=True)

    session.run(
        "./lnd",
        "--bitcoin.active",
        "--bitcoin.testnet",
        "--debuglevel=info",
        "--bitcoin.node=neutrino",
        "--neutrino.connect=faucet.lightning.community",
        f"--lnddir={LND_DIR}",
    )
