# My Config generator script for v2rayN - v6.23

 A python script that generates Routing Rules in json format for [v2rayN application](https://github.com/2dust/v2rayN)

## Features:
   * "block list" for persian bad links (https://github.com/MasterKia/PersianBlocker/)
   * "white list" for persian sites (https://github.com/SamadiPour/iran-hosted-domains/)
   * Cache downloaded lists ("block list" and "white list") and control cache time

## Dependencies:
  * python 3 (https://www.python.org/downloads)
  * python requirements:
    * requests

## Usage
  ### Generate config:
  * if you are running script for first time:
    * get and install requirements:`pip install -r requirements.txt`

  * then run the script using python:`python generate-rules.py` this will generate a file with name `v2rayN_rules.json` beside the script.

  ### Using in the Application (quick hint!)

Follow these paths in the app:

​    **Settings -> RoutingSetting -> Advanced Function -> Add -> Import Rules From File**

select generated config (`v2rayN_rules.json`) Set a name (in remarks section) and confirm it, and in the bottom of app (routing section), select it!
