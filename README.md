# btcturk_python_api
Very basic btcturk python api <br>
When you create an api key, use ipv6 address<br>
Source:<br>
https://docs.btcturk.com/authentication/authentication-v1
<br>
Usage:
<br>
<pre>
<code>from btcturk_api import Btcturk
    
apiKey1 = "PUBLIC_KEY"
apiSecret1 = "PRIVATE_KEY"
    
api = Btcturk(apiKey1, apiSecret1)
    
params1={
    "quantity": 124,
    "price": 1.60,
    "stopPrice": 0,
    "newOrderClientId": "api_bot",
    "orderMethod": "limit",
    "orderType": "buy",
    "pairSymbol": "DOGETRY"
    }
    
#print(api.tick("BTCUSDT"))
#print(api.get_balance("TRY"))
#print(api.get_open_orders("DOGETRY"))
#print(api.submit_order(params1))
#print(api.cancel_order(16883735082))
</code></pre>
