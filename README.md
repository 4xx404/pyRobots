# pyRobots  

pyRobots is a brute force crawler written in python3. This tool will check for a websites robots.txt file & if it exists, it will download it & then proceed to attempt to download everything else in each of its disallow entries by brute forcing for files in directories.   

# Scans
1. Only attempts to download from robots.txt (no directory brute force).  
2. Attempts to download from robots.txt + directory brute force using 2 wordlists (1 for filename, 1 for extensions).  
  
Scans create a directory to save downloaded files to: '/Pulled-Data/Key/' [Key format: 0000000]  

# Usage  
```
git clone https://github.com/4xx404/pyRobots  
cd pyRobots  
python3 -m pip install -r requirements.txt  
sudo chmod +x pyRobots.py && ./pyRobots
```
