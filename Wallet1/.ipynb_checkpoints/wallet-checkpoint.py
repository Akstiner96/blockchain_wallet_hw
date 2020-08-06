import web3
from web3 import Web3
from dotenv import load_dotenv
load_dotenv()
import os
from pathlib import Path
import json
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
priv_key = os.getenv("private_key")
from web3.middleware import geth_poa_middleware
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
from constants import* 
import subprocess
import bit
from bit import Key
from bit.network import NetworkAPI
from eth_account import Account
from getpass import getpass
import ast

load_dotenv()
mnemonic = os.getenv("MNEMONIC", "INSERT MNEMONIC HERE")
constants = [BTCTEST,ETH]

def derive_wallets(mnemonic, constants):
    for name in constants:
        sub = subprocess.Popen(f"./derive -g --mnemonic='{mnemonic}' --coin={name} --numderive=3 --format=json")
    return sub

output=derive_wallets(mnemonic, constants)

with open("output.json", "w") as f:
    f.write(json.dumps(output))


btc_key = output['btc-test'][0]['privkey']
eth_key = output['eth'][0]['privkey']

def accounts(coin, priv_key):
    if coin=='eth':
        account = web3.Account.from_key(priv_key)
        return account
    elif coin=='btc-test':
        account = bit.PrivateKeyTestnet(priv_key)
        return account

    
btc1 = accounts('btc-test', output['btc-test'][0]['privkey'])
btc2 = accounts('btc-test', output['btc-test'][1]['privkey'])

eth1 = accounts('eth', output['eth'][0]['privkey'])
eth2 = accounts('eth', outputs['eth'][0]['privkey'])

def create_tx(coin, account, to, amount):
    if coin=='eth':
        gasEstimate = w3.eth.estimateGas({
            "from":account.address,
            "to":to.address,
            "value":amount
        })

        eth_dict={
            "from":account.address,
            "to":to.address,
            "value":amount,
            "gas":gasEstimate,
            "gasPrice":w3.eth.gasPrice,
            "nonce":w3.eth.getTransactionCount(account.address)
        }
        return eth_dict

    elif coin == 'btc-test':
        return bit.PrivateKeyTestnet.prepare_transaction(account.address,[(to.address, amount, BTC)])



def send_tx(coin, account, to, amount):
    if coin == 'eth':
        raw_tx = create_tx(coin, account, to, amount)
        signed_tx = account.sign_transaction(raw_tx)
        return w3.eth.sendRawTransaction(signed_tx.rawTransaction)

    elif coin == 'btc-test':
        raw_tx = create_tx(coin, account, to, amount)
        signed = account.sign_transaction(raw_tx)
        return NetworkAPI.broadcast_tx_testnet(signed)