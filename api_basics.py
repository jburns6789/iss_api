import requests

url = "http://api.open-notify.org/iss-now.json"
response = requests.get(url)

# print(response.status_code)
#
# print(response.json())
#
#print(response.json()['iss_position'])
#
# print(response.json()['iss_position']['latitude'])

latitude = response.json()['iss_position']['latitude']
longitude = response.json()['iss_position']['longitude']

# to tuple...
iss_position = (latitude, longitude)

print(iss_position)

# 1xx: Informational, Hold on Working
# 2xx: Success, Here is what you requested
# 3xx: Redirection, Go away you dont have permission
# 4xx: Client Errors, You made an error
# 5xx: Server Errors, We have an error
# https://www.webfx.com/web-development/glossary/http-status-codes/
# https://docs.python-requests.org/en/latest/

def api_return():
    import requests
    try:
        url = "https://api.kanye.rest"
        response = requests.get(url)
        response.raise_for_status()
        quote = response.json().get('quote')
        if quote:
            print(quote)
        else:
            print("No quote found in the response")
    except requests.RequestsException as e:
        print(f"An error occured: {e}")

api_return()