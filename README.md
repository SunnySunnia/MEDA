# MEDA

[Osample.py](Osample.py) finds 20 (maximum I can get) businesses in the mission district, San Francisco.   
-->There has all the information about each business, but a problem is the format isnt really good.  
  --->I am trying to manually adjust the format in R.  

[Ooutput1.txt](Ooutput1.txt) is the output text file.


-----------------------------------------------------------------------------------------
* Update

install ```requests```  
install ```requests-oauthlib```  
install ```yelpapi```  


The steps I took:  
clone the two repos:  
https://github.com/gfairchild/yelpapi  
https://github.com/requests/requests-oauthlib  
--can access the examples these two repos provided  
```
sudo apt-get install pip
sudo pip install requests requests-oauthlib yelpapi
python mission.py ->mission.txt
```

[mission.py](mission.py) is the script modified from the example given from the YelpAPI python module.
User can substitute search terms, search location in text or in lon-lan bounds, and search categories.

[mission.txt](mission.txt) is the corresponding resulting text file of the test search (can only obtain 20 results in each search)

