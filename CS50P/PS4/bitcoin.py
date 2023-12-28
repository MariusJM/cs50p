import requests
import sys
import json

try:
    if len(sys.argv) == 2:
        response = requests.get(
        " https://api.coindesk.com/v1/bpi/currentprice.json"
        )
        o = response.json()
        #print(int(sys.argv[1]) * 100)
        #print(json.dumps(response.json(), indent=2))
        price = response.json()["bpi"]["USD"]["rate_float"]
        output = price * float(sys.argv[1])
        #print(output)
        print(f"${output:,.4f}")
except requests.RequestException:
    print("Missing command-line argument")
    sys.exit(1)
