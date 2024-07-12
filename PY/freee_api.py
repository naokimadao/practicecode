import requests

ACCESS_TOKEN = '3d53eab07157cfcedeb122fbdb247f69dbc659913f6e35df32e0009e46f10c3f'
BASE_URL = 'https://api.freee.co.jp/hr/api/v1'
COMPANY_ID = '11449504'
EMPLOYEE_ID = '02010'
FROM_DATE = '2024-05-01'
TO_DATE = '2024-05-31'
LIMIT = 50
OFFSET = 0

url = f'{BASE_URL}/employees/{EMPLOYEE_ID}/time_clocks'
headers = {
    'accept': 'application/json',
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'FREEE-VERSION': '2022-02-01'
}
params = {
    'company_id': COMPANY_ID,
    'from_date': FROM_DATE,
    'to_date': TO_DATE,
    'limit': LIMIT,
    'offset': OFFSET
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")
    print(response.json())
