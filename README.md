# pyRobots  

pyRobots is a brute force crawler written in python3. This tool will check for a websites robots.txt file & if it exists, it will download it & then proceed to attempt to download everything else in each of its disallow entries.   

# Scans
1. Fast scanning, only attempts to download from robots.txt, no delay, no directory brute force.  
2. Slow scanning, attempts to download from robots.txt + use a wordlist for directory brute force, no delay.  
3. Slowest scanning, attempts to download from robots.txt + uses 2 wordlists which are selected by the user(1 for filename, 1 for extensions), directory brute forces (recognises directories & will brute force files), accepts delay set by user.  
  
All scans create a directory to save every downloaded file in '/Pulled-Data/Key/'.  
  
Key format: 0000000  

# Usage  
```
git clone https://github.com/4xx404/pyRobots  
cd pyRobots  
python3 -m pip install -r requirements.txt  
sudo chmod +x pyRobots.py && ./pyRobots
```
