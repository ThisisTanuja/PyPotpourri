import requests
from bs4 import BeautifulSoup
from plyer import notification 

# Function for getting data from the given url
def getData(url):
    request = requests.get(url)
    return request.text

# Pass the url into the function and convert it into html code
htmlData = getData("https://weather.com/en-IN/weather/today/l/a8b03859a74c46682a335f81da65465fc1155f642c8e55a7fbd5f115d4825dee")
beautifulSoup = BeautifulSoup(htmlData, 'html.parser')
#print(beautifulSoup.prettify())

# Find the required details and filter them
temperature = beautifulSoup.find("span", {"data-testid": "TemperatureValue"}).text
humidity = beautifulSoup.find("span", {"data-testid": "PercentageValue"}).text

result = f"Current temperature: {temperature} in Fort Wayne, Indiana\nHumidity: {humidity}"

# Pass the result into notifications object
notification.notify(title="Weather Update", message=result, timeout=10)