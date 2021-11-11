# Son's Ethermining setup using PhoenixMiner :D

## Versions
```
Python 3.8
PhoenixMiner 5.7b
```
## Getting Started
1. Install latest version of Python 3.8 from python website below
   1. https://www.python.org/downloads/release/python-380/
1. Update pip and install [requirements.txt](requirements.txt) file
     
```     
# change into local directory 
cd C:\Users\Lance-PC\Desktop\github\crypto_mining\
pip install --upgrade pip
pip install -r requirements.txt
```
## How it works
1. Since I'm mining ethereum, I chose to go with the ethermine pool. You can update the .bat file to leverage any other pool you would rather mine with
   1. Reference to my mining rig's performance
      1. https://ethermine.org/miners/0620d26D5dDe3Ec053aA0ac49404EFcc8555A4A3/dashboard
1. Python executing the [ether_mining_start.py](python/ether_mining_start.py) script, it will automatically start the start_miner - Shortcut script inside the phoenix miner
```     
python python/ether_mining_start.py
```
3. Python executing the [ether_mining_stop.py](python/ether_mining_stop.py) script will stop the mining
```     
python python/ether_mining_stop.py
```

## Scripts to modify
1. Modify the [start_miner.bat](/PhoenixMiner_5.4c_Windows/start_miner.bat)
   1. update the target wallet (the guid after the -wal param should be your public ethereum address) location to personal wallet. or you can leave it and it'll mine to my location :D
   2. you can create a wallet using https://www.myetherwallet.com/
2. Ensure there is a shortcut file generated from the [start_miner.bat](/PhoenixMiner_5.4c_Windows/start_miner.bat). right click on the mentioned file and **create shortcut** 
3. Execute the [ether_mining_start.py](python/ether_mining_start.py)

## Scheduling
1. You can then schedule the [ether_mining_start.py](python/ether_mining_start.py) and [ether_mining_stop.py](python/ether_mining_stop.py) via task scheduler
   1. You can reference this picture below on using python to execute the python script inside the local directory
```
# get location of python exe on local machine
import sys
print(sys.executable)
```
   2. ![task scheduler](https://github.com/sonphan1/crypto_mining/blob/master/reference/schedule%20etherminer.png)

## References
1. https://www.reddit.com/r/EtherMining/comments/ksu60b/psa_to_the_new_miners_using_phoenixminer/
2. The official Phoenix miner download that is inside this repo [Phoenix miner 5.7b](https://bitcointalk.org/index.php?topic=2647654.0)
3. Leverage the following website to see top pools for coins or google best pools to join 
   1. https://www.poolwatch.io/

## Future Considerations
- When updating to new version of PhoenixMiner, ensure to update [start_miner.bat](/PhoenixMiner_5.4c_Windows/start_miner.bat) and create shortcut of the [start_miner.bat](/PhoenixMiner_5.4c_Windows/start_miner.bat) file

C:\Users\Lance-PC\AppData\Local\Programs\Python\Python38-32\python.exe C:\Users\Lance-PC\Desktop\github\crypto_mining\python\ether_mining_stop.py
