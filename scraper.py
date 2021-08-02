import request
from bs4 import BeautifulSoup


url = 'https://en.wikipedia.org/wiki/History_of_Mexico'

def get_citations_needed_count(URL):
    response = request.get(URL)
    soup = BeautifulSoup(response.text,'html.parser')
      

def get_citations_needed_report(URL):
    response = request.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    

