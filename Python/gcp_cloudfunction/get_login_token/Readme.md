# Introduction

We have two cloud functions one is to authenticate and generate jwt token 
and the other one is to return a response after authenticating using that jwt.

1. [get_login_token](https://asia-south1-cc-dev-sandbox-20200619.cloudfunctions.net/get_login_token) 
    make a post call with `username` and `password` as Basic Auth to get a jwt token that will be valid for next `20 min`
    * `username = <can be anything>`
    * `password = password`
    
    #### Request
    ```commandline 
        curl --location --request POST 'https://asia-south1-cc-dev-sandbox-20200619.cloudfunctions.net/get_login_token' --user sudhanshu:password 
    ```
    #### Response
    ```json
    {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoicGFua2FqIiwiZXhwIjoxNjM4ODU4NTUxfQ.xMSOR5PoiwLYv3kAid5ufhkGsNlUn_H1y_jL1_BSozE",
    }
    ```
2. [Get the list of Organisations](https://asia-south1-cc-dev-sandbox-20200619.cloudfunctions.net/get_quote_summary)
    #### Request
      ```commandline
    curl --location --request GET 'https://asia-south1-cc-dev-sandbox-20200619.cloudfunctions.net/get_quote_summary' \ 
     --header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoicGFua2FqIiwiZXhwIjoxNjM4ODU5MDAzfQ.0wpnv_0M2DEbTdYz1MYcJPHJX1JKlxQ-4vWWS023ILc' \
     --data-raw ''
     ```

   #### Response
    ```json
    {
        "Listed_Orgnisations": [
            "AAPL",
            "BABA",
            "GOOG",
            "TSLA"
        ]
    }
    ```
3. [Get Data for Given Organisations](https://asia-south1-cc-dev-sandbox-20200619.cloudfunctions.net/get_quote_summary)
   Get Data for Organisations mentioned in request. it will return null if no data available for that organization
    #### Request
    ```commandline
    curl --location --request POST 'https://asia-south1-cc-dev-sandbox-20200619.cloudfunctions.net/get_quote_summary' \
    --header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoic3VkaGFuc2h1IiwiZXhwIjoxNjM4OTQ1OTMzfQ.Bt0Lc-8Yb_sk7Mf4_Qzp-V1Tsmgu9vqruhv1tMu6iBg' \
    --header 'Content-Type: application/json' \
    --data-raw '{"orgs": [
        "TSLA"
    ]}'
    ```
    ####Response
    ```json
      {
    "TSLA": {
        "quoteSummary": {
            "error": "null",
            "result": [
                {
                    "price": {
                        "averageDailyVolume10Day": {},
                        "averageDailyVolume3Month": {},
                        "circulatingSupply": {},
                        "currency": "USD",
                        "currencySymbol": "$",
                        "exchange": "NMS",
                        "exchangeDataDelayedBy": 0,
                        "exchangeName": "NasdaqGS",
                        "fromCurrency": "null",
                        "lastMarket": "null",
                        "longName": "Tesla, Inc.",
                        "marketCap": {
                            "fmt": "1.02T",
                            "longFmt": "1,019,293,728,768.00",
                            "raw": 1019293728768
                        },
                        "marketState": "PRE",
                        "maxAge": 1,
                        "openInterest": {},
                        "postMarketChange": {
                            "fmt": "-6.97",
                            "raw": -6.9699707
                        },
                        "postMarketChangePercent": {
                            "fmt": "-0.69%",
                            "raw": -0.006867169
                        },
                        "postMarketPrice": {
                            "fmt": "1,008.00",
                            "raw": 1008.0
                        },
                        "postMarketSource": "DELAYED",
                        "postMarketTime": 1638579600,
                        "preMarketChange": {
                            "fmt": "-11.74",
                            "raw": -11.73999
                        },
                        "preMarketChangePercent": {
                            "fmt": "-1.16%",
                            "raw": -0.011566835
                        },
                        "preMarketPrice": {
                            "fmt": "1,003.23",
                            "raw": 1003.23
                        },
                        "preMarketSource": "FREE_REALTIME",
                        "preMarketTime": 1638788402,
                        "priceHint": {
                            "fmt": "2",
                            "longFmt": "2",
                            "raw": 2
                        },
                        "quoteSourceName": "Nasdaq Real Time Price",
                        "quoteType": "EQUITY",
                        "regularMarketChange": {
                            "fmt": "-69.63",
                            "raw": -69.630005
                        },
                        "regularMarketChangePercent": {
                            "fmt": "-6.42%",
                            "raw": -0.06419879
                        },
                        "regularMarketDayHigh": {
                            "fmt": "1,090.58",
                            "raw": 1090.5753
                        },
                        "regularMarketDayLow": {
                            "fmt": "1,000.21",
                            "raw": 1000.21
                        },
                        "regularMarketOpen": {
                            "fmt": "1,084.79",
                            "raw": 1084.79
                        },
                        "regularMarketPreviousClose": {
                            "fmt": "1,084.60",
                            "raw": 1084.6
                        },
                        "regularMarketPrice": {
                            "fmt": "1,014.97",
                            "raw": 1014.97
                        },
                        "regularMarketSource": "FREE_REALTIME",
                        "regularMarketTime": 1638565203,
                        "regularMarketVolume": {
                            "fmt": "30.52M",
                            "longFmt": "30,516,306.00",
                            "raw": 30516306
                        },
                        "shortName": "Tesla, Inc.",
                        "strikePrice": {},
                        "symbol": "TSLA",
                        "toCurrency": "null",
                        "underlyingSymbol": "null",
                        "volume24Hr": {},
                        "volumeAllCurrencies": {}
                    }
                }
            ]
        }
    }
}
    ```