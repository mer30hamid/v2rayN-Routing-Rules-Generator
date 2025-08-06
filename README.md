[![en](https://img.shields.io/badge/lang-fa-red.svg) فارسی](https://github.com/mer30hamid/v2rayN-Routing-Rules-Generator/blob/main/README.fa-IR.md)

# My Config generator script for v2rayN

 A python script that generates Routing Rules in json format for [v2rayN application](https://github.com/2dust/v2rayN)

The main purpose of producing these rules is to solve the problem of opening Iranian sites, so that when we enter a site ftom iran, it doesn't get a problem that we are using a VPN, etc.

## Features:
   * "block list" for persian bad links (https://github.com/MasterKia/PersianBlocker/)
   * "white list" for persian sites (https://github.com/SamadiPour/iran-hosted-domains/)
   * when running script, it Caches downloaded lists ("block list" and "white list") and you can control cache time
   * Automatic Update using GitHub Actions

## Usage methods

### Method 1: Import Rules From Subscription url

  1. copy this address:
  ```
  https://raw.githubusercontent.com/mer30hamid/v2rayN-Routing-Rules-Generator/main/v2rayN_rules.json
  ```
  and paste it here:
     
  **Settings -> RoutingSetting -> Advanced Function -> Add -> URL(Optional)**
     
  >**Note: you can use your own server and url, this url in this repo updates every day automatically using github actions!**

  2. set a name (in Remarks for example "Iran")
  3. click on "Import Rules From Subscription URL"
  4. when asked "do you want to append rules? ..." press `yes`
  5. click "Confirm" to save rules.
    
  ![image](https://github.com/user-attachments/assets/cbbe22dc-4143-4e04-a161-2351d4eb433a)

  6. in the bottom of app (routing section), select it (Iran)

  ![image](https://github.com/user-attachments/assets/a38613e9-2126-429c-a22e-000a877dcced)
   
### Method 2: Import Rules from file

  1. go to **Settings -> RoutingSetting -> Advanced Function -> Add** 

     and set a name (in Remarks for example "Iran-local")

  2. click "Import Rules from file" and choose the generated (or downloaded) "v2rayN_rules.json" file.

  3. click "yes" and then "Confirm" to save rules.
  
  ![image](https://github.com/user-attachments/assets/69309327-4a4a-440b-a4b0-8c23bd7331bd)
  
  4. in the bottom of app (routing section), select it (Iran-local)

  ![image](https://github.com/user-attachments/assets/a38613e9-2126-429c-a22e-000a877dcced)

## Running and development hints
### Dependencies:
  * python 3 (https://www.python.org/downloads)
  * python requirements:
    * requests

### Generate config:
  * if you are running script for first time:
    * get and install requirements:`pip install -r requirements.txt`
  * run the script using python:`python generate-rules.py` this will generate a file with name `v2rayN_rules.json`
