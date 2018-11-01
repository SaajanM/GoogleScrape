import urllib.request
from bs4 import BeautifulSoup
import urllib3

userAgent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED')

def getNumResults(query):
    url = "https://www.google.com/search?q=" + query.replace(" ", "+")
    req = http.request('GET',url, headers=userAgent)
    soup = BeautifulSoup(req.data,'html.parser')
    numResultsDiv = soup.find('div', attrs={'id': 'resultStats'})
    numResults = int(numResultsDiv.text.split(" ")[1].replace(",",""))
    return numResults

