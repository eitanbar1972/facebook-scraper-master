import http.cookiejar
import urllib.request

# URL to interact with
url = 'https://www.facebook.com/'

# Create a cookie jar object
cookie_jar = http.cookiejar.CookieJar()

# Create an opener object
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))

# Interact with the URL
response = opener.open(url)
response.close()

# Saving cookies to a file
filename = 'cookies.txt'
cookie_jar.save(filename, ignore_discard=True, ignore_expires=True)

# To load cookies from the file later
file_cookie_jar = http.cookiejar.CookieJar()
file_cookie_jar.load(filename, ignore_discard=True, ignore_expires=True)

# Alternatively, keeping cookies in a variable
cookies_dict = {}
for cookie in cookie_jar:
    cookies_dict[cookie.name] = cookie.value

# Printing the cookies
print("Cookies saved to file:", filename)
print("Cookies in variable:", cookies_dict)
