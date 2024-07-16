# My Config generator script for v2rayN

 A python script that generates Routing Rules in json format for [v2rayN application](https://github.com/2dust/v2rayN)

## Features:
   * "block list" for persian bad links (https://github.com/MasterKia/PersianBlocker/)
   * "white list" for persian sites (https://github.com/SamadiPour/iran-hosted-domains/)
   * Cache downloaded lists ("block list" and "white list") and control cache time

## Dependencies:
  * python 3 (https://www.python.org/downloads)
  * python requirements:
    * requests

## Generate config:

  * if you are running script for first time:
    * get and install requirements:`pip install -r requirements.txt`

  * run the script using python:`python generate-rules.py` this will generate a file with name `v2rayN_rules.json`

## Usage methods

#### Import Rules From Subscription url :

  1. paste `https://raw.githubusercontent.com/mer30hamid/v2rayN-Routing-Rules-Generator/main/v2rayN_rules.json` in:
     
     **Settings -> RoutingSetting -> Advanced Function -> Add -> URL(Optional)**
     
     >**Note: you can use your own server and url, this url in this repo updates every day automatically using github actions!**

  3. set a name (in Remarks for example "Iran")
  4. click on "Import Rules From Subscription URL"
  5. when asked "do you want to append rules? ..." press `yes`
  6. click "Confirm" to save rules.
    
  ![image](https://github.com/user-attachments/assets/cbbe22dc-4143-4e04-a161-2351d4eb433a)

  7. in the bottom of app (routing section), select it (Iran)

  ![image](https://github.com/user-attachments/assets/a38613e9-2126-429c-a22e-000a877dcced)


     

#### Import Rules from file:

  1. go to **Settings -> RoutingSetting -> Advanced Function -> Add** 

     and set a name (in Remarks for example "Iran-local")

  2. click "Import Rules from file" and choose the generated (or downloaded) "v2rayN_rules.json" file.

  3. click "yes" and then "Confirm" to save rules.
  
  ![image](https://github.com/user-attachments/assets/69309327-4a4a-440b-a4b0-8c23bd7331bd)
  
  4. in the bottom of app (routing section), select it (Iran-local)

  ![image](https://github.com/user-attachments/assets/a38613e9-2126-429c-a22e-000a877dcced)

