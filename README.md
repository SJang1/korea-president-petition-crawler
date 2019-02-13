# korea-president-petition-crawler

This code can be written very easy for everyone.

## Why I made this
Korea GOV seems to tring to delete petitions' agree. this code tracks agrees for the specific petition(s) every 2.5minutes and log it, you can know if GOV had deleted agree easier than before.

## How to use it
Download this project

Install requests at stage.py

Install bs4 at stage.py

Install time at stage.py

Install time at stage.py

change codes = ["000000"] to whatever you want (like ["522031"] or ["522031", "522062"]) at stage.py

Run stage.py

Check output.txt file. It will be look like this : 
{'time': 'Wed Feb 13 08:50:39 2019', 'title': '(title)', 'agrees': '104,661'}
and added each 150 seconds.

## What is the update plan
* Makeing question when starting code first.
* Checking +- so you can find easier
* Auto generating JSON format so can be used in other services easier.
* build it so can make everyone use it easier.
