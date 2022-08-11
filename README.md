# From Google Sheets copy and update
This script takes data from [the sheet](https://docs.google.com/spreadsheets/d/1f-qZEX1k_3nj5cahOzntYAnvO4ignbyesVO7yuBdv_g/edit#gid=0), then saves it to the [new sheet](https://docs.google.com/spreadsheets/d/1f-qZEX1k_3nj5cahOzntYAnvO4ignbyesVO7yuBdv_g/edit#gid=0) (open for all to ease testing, but can have restricted mode).

In the target sheet it converts usd value to rub value accordingly to today's RCB rate.

It also marks outdated supply. 

How to run:
- download main.py
- create goeath 2 or service account [(for KS only) ](https://drive.google.com/file/d/1XBN1CsCpbr_dttv7gm6eTVEVivibq2jd/view?usp=drivesdk) 
- put all files in a single directory 
- run main.py (IDE recommended) 

There might be issues running the script on a network hardware since the script uses local files system to store price rate.
