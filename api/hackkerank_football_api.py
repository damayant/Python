import requests

# Base URL
BASE_URL = "https://jsonmock.hackerrank.com/api/football_teams?params=page_number"
DEFAULT_TIMEOUT=10

def get_response(params=None):
    page_num=2
    params={"page_number": page_num}
    try:
        response=requests.get(BASE_URL,params=params,timeout=DEFAULT_TIMEOUT)
        print(response.json())
        return response.json()
    except requests.RequestException as e:
        if response.status_code!=200:
            raise Exception(f'error fetching data:',e)

def get_all_pages():
    data=get_response()
    return data['total_pages']

def get_data_from_all_pages():
    total_pages=int(get_all_pages())
    data_agg=[]
    for page_num in range (1,total_pages):
        params={"page_number":page_num}
        data_per_page=get_response(params=params)
        if data_per_page:
            data_agg.append(data_per_page)
    print(data_agg)        
    
   


if __name__ == "__main__":
    # page = 1
    # teams, total_pages = get_football_teams(page,'Brazil')
    # print(f"Total pages: {total_pages}")
    # for team in teams:
    #     print(team['name'])
    get_data_from_all_pages()      
