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

## Added in-class heading example
def get_citation_headings(URL):
    headings = []
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    anchors = soup.find_all('a')
    heading_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    for anchor in anchors:
        text = anchor.get_text()
        if 'citation needed' in text:
            element = anchor.parent.parent.parent
            for ps in element.previous_siblings:
                if ps.name in heading_tags:
                    headings.append(ps.text)
                    break
    return headings

print(get_citations_needed_count(URL))
print(get_citations_needed_report(URL))
print(get_citation_headings(URL))