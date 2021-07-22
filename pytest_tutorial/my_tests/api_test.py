import pprint

from woocommerce import API

wcapi = API(
            url="http://192.168.100.4/coolsite",
            consumer_key="ck_821c75cffaf5f6997b085b0e36e97521e7cc871f",
            consumer_secret="cs_1f9fdbcfc0594055133668e6c12597b8a36457d0",
            version="wc/v3"
            )

r = wcapi.get("products")
print(r.status_code)
pprint.pprint(r.json())
