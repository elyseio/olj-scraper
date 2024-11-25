import random
from user_agents import user_agents
import requests
from bs4 import BeautifulSoup

def get_job_query():
    '''
    Prompt for search query and return it formatted: query+query
    '''
    job_q = input('Enter job search query: ').lower()
    print(f'\n[INFO] Searching for: {job_q}\n')
    return job_q.replace(' ', '+')

def get_full_dn(base_url, search_query):
    '''
    Return the full dn (str)
    '''
    return f'{base_url}/jobseekers/jobsearch?jobkeyword={search_query}'

def scrape_jobs(site_url, base_url, user_agent):
    '''Scrape job postings from the website'''
    # Make HTTP Request
    try:
        # Random User-Agent
        headers = {
            'User-Agent': user_agent
        }
        print(f"[INFO] Sending request to {site_url}")
        response = requests.get(site_url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad status codes (4xx, 5xx)
    except requests.exceptions.Timeout:
        print("[ERROR] Request timed out. Please check your internet connection or try again later.")
        return
    except requests.exceptions.RequestException as e:
        # Catch all other request-related exceptions
        print(f"[ERROR] Error requesting site: {e}")
        return

    soup = BeautifulSoup(response.text, 'lxml')
    job_board = soup.find_all('div', class_='jobpost-cat-box latest-job-post card-hover-default')

    if not job_board:
        print("[INFO] No jobs found matching your query.")
        return

    print("\n[INFO] Found the following job postings:")
    for job in job_board:
        # Extract Job Details
        title = job.find('h4', class_='fs-16 fw-700').get_text(strip=True)
        link = job.find('a')['href']
        full_link = f'{base_url}{link}'

        # Print job details in a clear, uniform format
        dash_num = 84
        print()
        print("=" * dash_num)
        print(f"[JOB TITLE] {title}")
        print(f"[LINK] {full_link}")
        print("=" * dash_num)
        print

def main():
    """
    Main function to run the job scraper
    - Defines domain_name (str): contains the domain name


    """
    # Domain Name
    domain_name = 'https://onlinejobs.ph'

    # Get job query
    job_query = get_job_query()

    # Full dn + search query
    full_domain_name = get_full_dn(domain_name, job_query)

    # Random User-Agent
    user_agent = random.choice(user_agents)

    # Perform scrape
    scrape_jobs(full_domain_name, domain_name, user_agent)

if __name__ == '__main__':
    main()
