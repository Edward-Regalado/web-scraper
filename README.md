# Lab 17 - Web Scraper

### Author
**Tony Regalado**

### Code
[Pull Request](https://github.com/Edward-Regalado/web-scraper/pull/1)

### Overview

Build a web scraper that can automate the process of manually using the site.

### Feature Tasks & Requirements

- [x] Scrape a Wikipedia page and record which passages need citations.
  - [x] E.g. [History of Mexico](https://en.wikipedia.org/wiki/History_of_Mexico) has few "citations needed" (5).
- [x] Web scraper should report the number of citations needed.
- [x] Web scraper should identify those cases AND include the relevant passage.
  - [x] E.g. Citation needed for "lorem spam and impsum eggs".
  - [x] Consider the "relevant passage" to be the parent element that contains the passage, often a paragraph element.

### Implementation Notes

- [x] Count function must be named **get_citations_needed_count**.
  - get_citations_needed takes in a url and returns an integer.
- [x] Report function must be named **get_citations_needed_report**.
  - get_citations_needed_report takes in a url and returns a string.
  - the string should be formatted with each citation needed on own line, in order found.
- [x] Module must be named scraper.py.

### Stretch Goals

- [o] Organize the needed citations by section (i.e. the parent heading tag).
  - Name additional function **get_citations_needed_by_section**.
- [o] Automatically do a citation scan for any links from the main section of wikipedia page.

### User Acceptance Tests

- [x] Verify that the correct count of citations needed is calculated.
- [x] Verify that preceding passage

### Collaboration & Credit

- [Crummy](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Youtube](https://www.youtube.com/watch?v=XVv6mJpFOb0)

### Configuration 
- $*poetry new web-scraper*
- Use the folder created by Poetry as the root of your project's git repository
- Refer to [Lab Submission Instructions](https://codefellows.github.io/code-401-python-guide/reference/submission-instructions/labs/) for detailed instructions.
