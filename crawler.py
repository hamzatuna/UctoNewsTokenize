import requests
import justext
from selenium import webdriver

FIRST_COL_XPATH = '/html/body/div[2]/table[2]/tbody/tr[2]/td[1]/div[3]/table/tbody/tr[2]/td[1]/span'
SECOND_COL_XPATH = '/html/body/div[2]/table[2]/tbody/tr[2]/td[1]/div[3]/table/tbody/tr[2]/td[3]/span'

def crawl_month_page(url, driver):
    """
    url: month page url
    driver: initilized selenium web driver
    """

    links = []
    driver.get(url)

    # get rows from calender table
    table = driver.find_element_by_id('calender')
    tbody = table.find_element_by_tag_name('tbody')
    rows = tbody.find_elements_by_tag_name('tr')

    # extract links from rows
    for row in rows:
        cols = row.find_elements_by_tag_name('td')
        
        for col in cols:
            try:
                link = col \
                    .find_element_by_tag_name('a') \
                    .get_attribute('href')
                links.append(link)
            
            except:
                pass

    return links

def crawl_second_page(url, driver):
    """
    url: url that extracted from month page
    driver: selenium web driver
    """

    driver.get(url)

    # extract links from first column of page
    first_col = driver.find_element_by_xpath(FIRST_COL_XPATH)
    raw_links = first_col.find_elements_by_tag_name('a')
    first_col_links = [raw_link.get_attribute('href') for raw_link in raw_links]

    # extract links from second column of page
    second_col = driver.find_element_by_xpath(SECOND_COL_XPATH)
    raw_links1 = second_col.find_elements_by_tag_name('a')
    second_col_links = [raw_link.get_attribute('href') for raw_link in raw_links1]

    return first_col_links+second_col_links

def boilerplate_content_page(url):
    """
    url: url of news page
    """

    # get page
    response = requests.get(url)
    paragraphs = justext.justext(response.content, justext.get_stoplist("English"))

    # filter boilerplate content
    filtered_paragraphs = filter(lambda p: p.is_boilerplate, paragraphs)
    texts = map(lambda p: p.text, filtered_paragraphs)

    return ' '.join(texts)

if __name__=='__main__':
    month_page_url = 'https://timesofindia.indiatimes.com/archive/year-2005,month-1.cms'
    driver = webdriver.Chrome()
    month_page_links = crawl_month_page(month_page_url, driver)
    second_page_links = []
    
    for month_page_link in month_page_links:
        print('crwaling {}'.format(month_page_link))
        links = crawl_second_page(month_page_link, driver)
        second_page_links.extend(links)
    
    for second_page_link in second_page_links:
        print('crwaling content page: {}'.format(second_page_link))
        content = boilerplate_content_page(second_page_link)
        print('content: {}', content)

