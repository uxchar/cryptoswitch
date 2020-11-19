# CryptoSwitch

CryptoSwitch is a simple app for those interested in cryptocurrency values in relation to the US Dollar. Currently, there are a total of 5 popular cryptocurrency choices to choose from such as Bitcoin, Ethereum, Litecoin, Ripple, and Binance. Users can perform as many conversions as they like and when prompted, may quit the app. The crypto value information is pulled from the CoinMarketCap API. I used the free version of the API which somewhat limits some of the information that can be pulled and how instant the information will be. 



## Running the Project

1. Install Python 3.8
2. Clone the repository to your machine using `git clone https://github.com/uxchar/cryptoswitch.git`
4. Run cryptoswitch.py in your interpreter

## Features

1. Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program (**App can continue to do numerous conversions until user types "no" at the app start or at the end of the last conversion**. **The user can also exit the app at anytime by typing 'quit' or 'q'**)

2. Read data from an external file, such as text, JSON, CSV, etc and use that data in your application(**App grabs the JSON file from the CoinMarketCap API and uses that data to make conversions.**)

3. Build a conversion tool that converts user input to another type and displays it (ex: converts cups to grams) (**App converts from USD to cryptocurrency or vice versa then displays it.**)

4. Create and call at least 3 functions, at least one of which must return a value that is used. (**4 functions are called in the app which are main(), convert_1(), convert_2(), and yes_no() which returns a True or False used to quit app or do a conversion**)