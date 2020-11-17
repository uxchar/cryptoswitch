# CryptoSwitch

CryptoSwitch is a simple app for those interested in cryptocurrency values in relation to the US Dollar. Currently, there are a total of 5 popular cryptocurrency choices to choose from such as Bitcoin, Ethereum, Litecoin, Ripple, and Binance. The crypto value information is pulled from the CoinMarketCap API. I used the free version which somewhat limited some of the information I could pull and how instant the information would be. User can perform as many conversions as they like and when prompted, may quit the app.



## Requirements



## Features

Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program (**App can continue to do numerous conversions until user types "no" at the app start or at the end of the last conversion**)

Read data from an external file, such as text, JSON, CSV, etc and use that data in your application(**CoinMarketCap API JSON file is pulled and data is extracted for conversions .**)

Connect to an external/3rd party API and read data into your app (**App is connected to the CoinMarketCap API for up-to-date data on cryptocurrency values and the data is used for conversions**)

Build a conversion tool that converts user input to another type and displays it (ex: converts cups to grams) (**App converts from USD to cryptocurrency or vice versa then displays it.**)

Create and call at least 3 functions, at least one of which must return a value that is used. (**4 functions are called in the app which are main(), convert_1(), convert_2(), and yes_no() which returns a True or False used to quit app or do a conversion**)