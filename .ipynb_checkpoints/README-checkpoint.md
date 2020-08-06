# blockchain_wallet_hw

Follow these steps in order to create your own wallet using hd-wallet-derive

Repository can be found here: https://github.com/dan-da/hd-wallet-derive

Clone the repo in the folder of your choice  

```git clone https://github.com/dan-da/hd-wallet-derive```

Change your directory to the newly created hd-wallet-derive  
```cd hd-wallet-derive```  

Use the following 2 commands to install the composer package and its required extension  
```php -r "readfile('https://getcomposer.org/installer');" | php```  
```php composer.phar install```

Lastly, use the following command to create a link to the hd-derive folder to the input ./derive  
```ln -s hd-wallet-derive/hd-wallet-derive.php derive```  


### Python output from hd-wallet
Use the wallet.py file to create multiple addresses and keys converted from your BIP39 mnemonic. The output should look like the following:

![''](./screenshots/btc0.png)


### Testing your Wallet
Next we will need to send some test transactions by using a [testnet faucet](https://testnet-faucet.mempool.co/).  

Input your address in the box and send over some test-net bitcoin. Make sure to grab and save the TxID.  
![''](./screenshots/btc1.png)


Check to make sure the transaction went through using a [block tracker](https://tbtc.bitaps.com/).  

As you can see below we have sent our account .001 test-net bitcoin.  
![''](./screenshots/btc3.png)  

### Send a transaction
Lastly we will send a transaction using the wallet.py file.  
Call the send_tx function from the wallet.py file and use 2 of the accounts as the 'account' and 'to' dependencies inside the function.  
Run the function and check your wallet to make sure the transaction succeeded.

![''](./screenshots/finaltx.png)