######################################################################
# Sbd Alert v1
# by Murat Tatar
# January 2018
######################################################################

import os
import requests
import re
import time

def e():
  exit()

# catch the requested word
def Between(bas,son,cumle):
    b1 = cumle.split(bas)
    b2 = b1[1].split(son)
    ar = b2[0]
    return ar

o = open('_alert_level.txt'); oi= o.read(); o.close();
alertLevel = float(oi)

o = open('_check_every_N_minutes.txt'); oi= o.read(); o.close();
checkTime = int(oi)


print alertLevel



## BitTrex SBD #########################################

def CheckSBD():
  url = "https://coinmarketcap.com/currencies/steem-dollars/#markets"
  bring = requests.get(url)
  arrival = bring.content # content into arrival

  # find the SBD price in arrival, that means coinmarketcap's web page source codes
  bitSbd1 = Between('Bittrex','Recently',arrival); 
  bitSbd2  = Between('price','</td>',bitSbd1)
  bitSbd   = Between('$','</span>',bitSbd2)

  bitSbd = float(bitSbd) # convert string to float

  print bitSbd
  return bitSbd



# prepare HTML file

html = '''
<html>
<title>Hey! SBD is over $''' + str(alertLevel) + '''</title>
<head>
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<style type="text/css">
  html { height: 100%; width: 100%; font-family: sans-serif;}
  body { background-color: rgb(42,73,84); background-image:url("alert.gif"); 
  background-position: center center;
  background-repeat: no-repeat; background-size: 63% 100%;} 

  .bb { position: absolute; bottom: 20px; color: rgb(210,135,135); }
  a, a:link {color: rgb(1,175,175);}
  .cc { color: rgb(250,100,100); }


  .outer {
    display: table;
    position: absolute;
    height: 97%;
    width: 97%; }

  .middle {
    display: table-cell;
    vertical-align: middle; }

  .inner { color: rgb(255,255,255);
    margin-left: auto;
    margin-right: auto; text-align: center;
    width: 100%; /*whatever width you want*/}


</style>
<body>
  <audio id="myTune" autoplay loop>
    <source src="hey.mp3"p>
  </audio>


<div class="outer">
  <div class="middle">
    <div class="inner">

  <div>Hey!  SBD is over <span class="cc">$''' + str(alertLevel) +'''</span>
    <br>
    You should check it
  </div>

    </div>
  </div>
</div>




  <div class="bb">
    gif from <a href="https://www.pinterest.co.uk/pin/108227197273406051/">here</a>
    <br>
    easy sbd alert by <a href="https://steemit.com/@murattatar">Murat Tatar</a>
  </div>
</body>
</html>
'''



# Run Forest! 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


while 1:  
  sbdnow = CheckSBD() # Check SBD price
  if sbdnow > alertLevel: # If current SBD price bigger than alert level
    o = open("alert.html","w"); o.write(html.encode("utf-8")); o.close() # create alert.html
    os.startfile("alert.html") # open alert.html

  time.sleep(checkTime*60) ## covert from minute to second and wait










