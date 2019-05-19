# lnd playground
Spin up a quick lnd testnet playground in virtual env with neutrino

## requires
pipenv
tmux

## install
```
git clone git@github.com:dgnsrekt/quick_lnd_playground.git
cd quick_lnd_playground
pipenv install
git clone git@github.com:dgnsrekt/lnd_grpc.git
cd lnd_grpc
git checkout origin/lnddir-fix
cd ..
pipenv run pip install -e lnd_grpc
pipenv shell

tmux
```
after running tmux split the screen
## download and start lnd
```
invoke server
```

## create password
```
invoke create
```
enter password twice
hit enter twice

## unlock lnd
```
invoke unlock
```
enter password

## playground
```
python3 playground.py
```
