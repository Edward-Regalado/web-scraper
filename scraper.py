import requests
from bs4 import BeautifulSoup


URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'
# page = requests.get(URL)
# print(page.content)

def get_citations_needed_count(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content,'html.parser')
    citations = soup.find_all(class_="noprint Inline-Template Template-Fact")
    return f'\n The number of Citations needed is: {len(citations)} \n'

def get_citations_needed_report(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    citations = soup.find_all(class_="noprint Inline-Template Template-Fact")
    list = 0
    for x in (citations):
        list += 1
        print(f'{list}. Citations needed for report: \n {x.parent.text}')
        # print(f'Citations needed for report: \n {list}')

print(get_citations_needed_count(URL))
print(get_citations_needed_report(URL))