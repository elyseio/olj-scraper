from bs4 import BeautifulSoup
import requests

def get_job_query():
    '''
    Prompt for search query and return it formatted: query+query
    '''
    job_q = input('job search: ').lower()
    print(f'\nSearching for: {job_q}.....\n')
    return job_q.replace(' ', '+')

def get_full_dn(base_url, search_query):
    '''
    Return the full dn
    '''
    return f'{base_url}/jobseekers/jobsearch?jobkeyword={search_query}'

def scrape_jobs(site_url, base_url):
    '''Scrape job postings from the website'''
    try:
        # Make HTTP Request
        response = requests.get(site_url)
        response.raise_for_status() # Raise an error for HTTP issues
    except requests.exceptions.RequestException as e:
        print(f'Error requesting site: {e}')
        return

    soup = BeautifulSoup(response.text, 'lxml')
    job_board = soup.find_all('div', class_='jobpost-cat-box latest-job-post card-hover-default')

    if not job_board:
        print("No jobs found")
        return

    for job in job_board:
        # Extract Job Details
        title = job.find('h4', class_='fs-16 fw-700').get_text(strip=True)
        link = job.find('a')['href']
        full_link = f'{base_url}{link}'

        # Print job details
        print("=====================================================================")
        print(f"Title: {title}")
        print(f"Link: {full_link}")
        print("=====================================================================\n")

def main():
    """Main function to run the job scraper."""
    # Domain Name
    dn = 'https://onlinejobs.ph'

    # Get job query
    job_query = get_job_query()

    # Full dn + search query
    full_dn = get_full_dn(dn, job_query)

    # Perform scrape
    scrape_jobs(full_dn, dn)

if __name__ == '__main__':
    main()
