import time, base64, hmac, hashlib, requests, json

apiKey1 = "Public_KEY"
apiSecret1 = "Private_KEY"

def tick(exchange): #BTCUSDT
    base = "https://api.btcturk.com"
    method = "/api/v2/ticker?pairSymbol={}".format(exchange)
    uri = base+method

    result = requests.get(url=uri)
    result = result.json()
    return result

def get_balance(symbol): #TRY
    base = "https://api.btcturk.com"
    method = "/api/v1/users/balances"
    uri = base+method

    apiKey = apiKey1
    apiSecret = apiSecret1
    apiSecret = base64.b64decode(apiSecret)

    stamp = str(int(time.time())*1000)
    data = "{}{}".format(apiKey, stamp).encode("utf-8")
    signature = hmac.new(apiSecret, data, hashlib.sha256).digest()
    signature = base64.b64encode(signature)
    headers = {"X-PCK": apiKey, "X-Stamp": stamp, "X-Signature": signature, "Content-Type" : "application/json"}

    result = requests.get(url=uri, headers=headers)
    result = result.json()
    for i in result["data"]:
        if i["asset"]==symbol:
            return i
    return None

def get_open_orders(symbol): # BTCTRY
    base = "https://api.btcturk.com"
    method = "/api/v1/openOrders?pairSymbol={}".format(symbol)
    uri = base+method

    apiKey = apiKey1
    apiSecret = apiSecret1
    apiSecret = base64.b64decode(apiSecret)

    stamp = str(int(time.time())*1000)
    data = "{}{}".format(apiKey, stamp).encode("utf-8")
    signature = hmac.new(apiSecret, data, hashlib.sha256).digest()
    signature = base64.b64encode(signature)
    headers = {"X-PCK": apiKey, "X-Stamp": stamp, "X-Signature": signature, "Content-Type" : "application/json"}

    result = requests.get(url=uri, headers=headers)
    result = result.json()
    return result["data"]["bids"]

def cancel_order(id): # order id as integer
    base = "https://api.btcturk.com"
    method = "/api/v1/order?id={}".format(id)
    uri = base+method

    apiKey = apiKey1
    apiSecret = apiSecret1
    apiSecret = base64.b64decode(apiSecret)

    stamp = str(int(time.time())*1000)
    data = "{}{}".format(apiKey, stamp).encode("utf-8")
    signature = hmac.new(apiSecret, data, hashlib.sha256).digest()
    signature = base64.b64encode(signature)
    headers = {"X-PCK": apiKey, "X-Stamp": stamp, "X-Signature": signature, "Content-Type" : "application/json"}

    result = requests.delete(url=uri, headers=headers)
    result = result.json()
    return result["success"]

def submit_order(params):
    base = "https://api.btcturk.com"
    method = "/api/v1/order"
    uri = base+method

    apiKey = apiKey1
    apiSecret = apiSecret1
    apiSecret = base64.b64decode(apiSecret)

    stamp = str(int(time.time())*1000)
    data = "{}{}".format(apiKey, stamp).encode("utf-8")
    signature = hmac.new(apiSecret, data, hashlib.sha256).digest()
    signature = base64.b64encode(signature)
    headers = {"X-PCK": apiKey, "X-Stamp": stamp, "X-Signature": signature, "Content-Type" : "application/json"}

    #params={"quantity": 0.001,"price": 50000,"stopPrice": 0, "newOrderClientId":"BtcTurk Python API Test", "orderMethod":"limit", "orderType":"sell", "pairSymbol":"BTCTRY"}
    params=params
    result = requests.post(url=uri, headers=headers, json=params)
    result = result.json()
    return result

params1={
    "quantity": 124,
    "price": 1.60,
    "stopPrice": 0,
    "newOrderClientId": "api_bot",
    "orderMethod": "limit",
    "orderType": "buy",
    "pairSymbol": "DOGETRY"
    }
#print(tick("BTCUSDT"))
#print(get_balance("TRY"))
#print(get_open_orders("DOGETRY"))
#print(submit_order(params1))
#print(cancel_order(16883735082))
