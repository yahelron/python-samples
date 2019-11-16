import urllib.request, json
# This program  will convert ILS (Israeli Shekel) currency to USD (United States Dollars).
## server (the url) return something like this in json format:
# {"query":{"count":1},"results":{"ILS_USD":{"id":"ILS_USD","val":0.285413,"to":"USD","fr":"ILS"}}}
# we take the rate and * with amount of nis.

def welcome_msg():
    print("Welcome to currency converter")
    nis = float(input("Please enter an amount of Shekeles to convert:"))
    return nis

def convert_ils_to_usd():
    url = urllib.request.urlopen("https://free.currconv.com/api/v7/convert?q=ILS_USD&compa%20ct=n&apiKey=02e19d101006ae7f186d")
    data = json.loads(url.read().decode())  # Decoding a web request
    # Parsing results
    results = data['results']
    ILS_USD = results['ILS_USD']
    val = ILS_USD['val']
    return val
    # Decoding response to str

def user_results(nis):
    print("####################")
    print("nis = ", nis)
    print("currency rate", convert_ils_to_usd())
    print("####################")
    total_usd=nis*convert_ils_to_usd()
    return total_usd
def main():
    try:
        print("Your NIS value is", user_results(welcome_msg()),"$")
    except:
        print("InvalidChoice")
    finally:
        print("Thanks for using our currency converter.")



if __name__ == '__main__':
    main()

