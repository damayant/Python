import requests

# Base URL
url = "https://jsonmock.hackerrank.com/api/football_teams"

def get_football_teams(page,nation=''):
    params={
        'page':page,
        'nation':'nation'
    }
    response=requests.get(url)
    if response.status_code!=200:
        raise Exception(f'error fetching data:{response,status_code}')
    data=response.json()
    total_pages=data['total_pages']
    teams = data['data']
    return teams, total_pages


if __name__ == "__main__":
    page = 1
    teams, total_pages = get_football_teams(page,'Brazil')
    print(f"Total pages: {total_pages}")
    for team in teams:
        print(team['name'])
        
