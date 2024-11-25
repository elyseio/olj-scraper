# Python CLI Tool to search for job in onlinejobs.ph

## Note: 
For now it'll only print the result on the first page of the search

## Usage:
```
python -m venv .venv
source .venv/bin/activate/
pip install -r requirements.txt
python main.py
```

## Sample Output:
```
Enter job search query: web

[INFO] Searching for: web

[INFO] Sending request to https://onlinejobs.ph/jobseekers/jobsearch?jobkeyword=web

[INFO] Found the following job postings:

====================================================================================
[JOB TITLE] Backend Magento Developer (Web Developer)Full Time
[LINK] https://onlinejobs.ph/jobseekers/job/1268872
====================================================================================

====================================================================================
[JOB TITLE] Tech Lead - Senior Magento Web Developer (Full Time)Full Time
[LINK] https://onlinejobs.ph/jobseekers/job/1268798
====================================================================================

...
```
