# pyRobots  

pyRobots is a brute force crawler written in python3. This tool will check for a websites robots.txt file & if it exists, it will download it & then proceed to attempt to download everything else in each of its disallow entries. pyRobots has 3 scan types. The major difference between scan 1 vs scan 2 & 3, is the added brute force element against what it recognises as directories. The major difference between scan 2 vs scan 3 will be request delay control, character shifting/replacement if wordlist entry includes characters such as ".#~" & testing each combination.  
NOTE: Advanced Scan is still in development  

# Usage  
git clone https://github.com/Bl1xY/pyRobots  
cd pyRobots  
python3 pyRobots.py  
Enter URL (http/s://www.url.com/)
