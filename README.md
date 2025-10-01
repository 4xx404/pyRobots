# PyRobots

![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/github/license/4xx404/pyrobots)

**PyRobots** is a web reconnaissance tool developed in **Python 3**, designed to analyze and extract potentially sensitive paths from a target website’s `robots.txt` file. It supports both direct downloading of explicitly listed paths as well as a brute-force discovery mechanism to uncover hidden directories and resources that may be restricted from crawlers.

---

## Features

- Downloads and parses the `robots.txt` file from the target host.
- Identifies and extracts `Disallow`, `Allow`, `Sitemap`, and `Crawl-delay` directives.
- Supports two scanning modes:
  - **Quick Scan**: Downloads explicitly listed paths from the `robots.txt`.
  - **Directory Scan**: Performs recursive brute-force enumeration using customizable wordlists for filenames and file extensions.
- Respects `Crawl-delay` directives where specified.
- Multithreaded for performance, with intelligent throttling and retry mechanisms.
- Supports user-agent aware parsing (e.g., separate rules for `*`, `Googlebot`, etc.).

---

## Scan Modes

| Mode          | Description                                                                                                                                                    |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Quick**     | Parses `robots.txt` and downloads all entries listed under `Disallow` and `Allow` directives.                                                                  |
| **Directory** | Extends Quick mode by performing brute-force discovery against extracted directories using a combination of filename and extension wordlists.                  |

---

## Output

All results are saved in the following directory structure:
**`output/<domain>/`**

---

### Usage

```bash
cd pyRobots
python3 -m pip install -r requirements.txt
sudo chmod +x pyRobots.py
python3 pyRobots.py
```

You will be prompted to enter a target URL. The tool will then:

* Retrieve and parse the robots.txt file.
* Execute the selected scan mode.
* Optionally download exposed or disallowed resources.
* Present an interactive prompt to initiate directory brute-forcing.

### Requirements

- Python 3.8+
- Internet access (for retrieving target robots.txt and resources)
- Dependencies listed in requirements.txt

Install required packages with:
```pip install -r requirements.txt```

### Wordlists

Two customizable wordlists are used for brute-forcing:

- wordlists/common.txt — common directory or file names.
- wordlists/extensions.txt — common file extensions (e.g., .php, .bak, .old).

You may modify or extend these wordlists to suit your needs.

### Disclaimer
See [pyRobots Disclaimer](https://github.com/4xx404/pyRobots/blob/main/DISCLAIMER.md)
