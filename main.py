from bs4 import BeautifulSoup
import requests

def get_job_query():
    '''
    Prompt for search query and return it formatted: query+query
    '''
    job_q = input('job search: ').lower()
    print(f'Searching for: {job_q}')
    return job_q.replace(' ', '+')

def scrape(site):
    # Make request
    req = requests.get(site).text

    soup = BeautifulSoup(req, 'lxml')

    job_board = soup.find_all('div', class_='jobpost-cat-box latest-job-post card-hover-default')

    for job in job_board:
        print('=====================================================================')
        title = job.find('h4', class_='fs-16 fw-700').get_text(strip=True)
        print(title)

        link = job.find('a')['href']
        link_href = f'{dn}{link}'
        print(f'{link_href}')

        print('=====================================================================\n')

        with open('jobs.txt', 'a') as f:
            f.write("=====================================================================\n")
            f.write(title + '\n')
            f.write(link_href + '\n')
            f.write("=====================================================================\n\n")

def main():
    # Domain Name
    dn = 'https://onlinejobs.ph'

    # Get job query
    job_query = get_job_query()

    # Full dn + search query
    site = f'{dn}/jobseekers/jobsearch?jobkeyword={q}'

    # Perform scrape
    scrape(site)


