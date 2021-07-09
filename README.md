# Bitcoin Polybar
The purpose of these configuration files is to show up periodically the price of one or several criptocurrencies with an API that provide us that information. The data will be shown directly on the polybar.
## Installation
In order to get the desired results you must have installed the polybar and optionally one polybar theme. In addition, we will not be able to access to the  API https://coinmarketcap.com/api/ if we do not create a new API KEY and replace it in *YOUR API KEY*  field. It is important to mention that there will be only 333 requests per two days if the Basic Plan is chosen.
## Configuration
The API provides us with plenty of information to get. However, I will only access to the price field of the criptocoin selected. If anyone wants to get information from another criptocurrency, it is needed to make another request where you access to the field "name" and it will show up all the names of the criptocoins or changing the number where is allocated the coin in the JSON file. 
For ease purposes, this configuration will only show up the **Bitcoin** price.

Once the key is replaced, the python file is ready and we will have to tell the polybar where is the file that executes the python code and how to show it. The sh file which does that action is bitcoin.sh. (It is important to mention that you have to install **Nerd Fonts** and select them, in order to show the bitcoin logo that is configured in the sh file).
In my particular case, I have installed the polybar mode **hack**. So in the **modules.ini** file configuration which is in ~/.config/polybar/hack/modules.ini, you have to add this new module:
 ```
[module/bitcoin]
type = custom/script
  
format-padding = 1

interval = 600
exec = ~/route_to_bitcoin.sh
 ```
In order to not overcome the requests limit per two days, the frequency of request will be 1 each 10 min, which is consistently enough to the general purpose.

Then in ~/.config/polybar/config.ini you have to add that module where you want to show it. In my case it wil be on the **bottom bar** in the **modules-right** field.

Finally, restart your polybar or window manager and you will have it!!