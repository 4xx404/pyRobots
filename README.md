# pyRobots  

pyRobots is a brute force crawler written in python3. This tool will check for a websites robots.txt file & if it exists, it will download it & then proceed to attempt to download everything else in each of its disallow entries. pyRobots has 3 scan types. The major difference between scan 1 vs scan 2 & 3, is the added brute force element against what it recognises as directories. The major difference between scan 2 vs scan 3 will be request delay control, character shifting/replacement if wordlist entry includes characters such as ".#~" & testing each combination.  

# Scans
1. Fast scanning, only attempts to download from robots.txt, no delay, no directory brute force.  
2. Slow scanning, attempts to download from robots.txt + use a wordlist for directory brute force, no delay.  
3. Slowest scanning, attempts to download from robots.txt + uses 2 wordlists which are selected by the user(1 for filename, 1 for extensions), directory brute forces, accepts delay set by user.  
* All scans create a directory to save every downloaded file in '/Pulled-Data/Key/'.  
  
* Key format: 0000000  

# Usage  
git clone https://github.com/Bl1xY/pyRobots  
cd pyRobots  
sudo python3 pyRobots.py  
Enter URL (http/s://www.url.com/)
