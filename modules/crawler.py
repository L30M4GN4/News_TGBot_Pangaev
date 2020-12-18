from googlesearch import search
from requests import Session
from sys import setrecursionlimit
from re import sub
from date_extractor import extract_dates

#TODO: Too many requests, please wait urllib.error.HTTPError: HTTP Error 429: Too Many Requests
def run(text):
    query = text
    search_results_urls = []
    lang = 'ru'
    for i in search(query,    # The query you want to run
                tld = 'com',  # The top level domain
                lang = lang,  # The language
                num = 10,     # Number of results per page
                start = 0,    # First result to retrieve
                stop = None,  # Last result to retrieve
                pause = 0,  # Lapse between HTTP requests
               ):    
        search_results_urls.append(i)
    date_list = []
    for url in search_results_urls:
        url_context = str(get_content(url))
        dates = get_date(url_context, [lang])
        print(date)
        date_list.append(dates)
    print (date_list)
    # first_one(date_beautified)
    # return my_results_list

def get_content(url):
    session = Session()
    response = session.get(url)
    return response.text

def get_date(context, lang):
    setrecursionlimit(1000)
    dates = extract_dates(context)
    print (dates)
    return dates

def first_one(date_list):
    minDate = max(date_list)
    for date in date_list:
        if minDate > date:
            minDate = date
    print (minDate)
    return minDate

# run("Ученые лэти")

script_template = "<\w*?script.*?>(\s?.*?)*?<\/\w*?script>"
tag_template = "\s*?<\/?(\s?.*?)*?>\s*?"


templates = [
    "\\\w",
    script_template,
    tag_template,
    "\n",
    "&.+?;"
    ]

s = Session()
r = s.get("https://etu.ru/ru/nauchnaya-i-innovacionnaya-deyatelnost/novosti1/uchenye-leti-predlozhili-diagnostirovat-i-lechit-covid-19-s-pomoshhyu-peptidov").text
dates = extract_dates(r)
for template in templates:
    r = sub(template, " ", r)
dates = extract_dates(r)
print (dates)
