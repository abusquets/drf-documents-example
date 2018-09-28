import requests

base_url = 'http://localhost:8000/api/v1/'
api_list_url = '%sdocuments/' % base_url
api_detail_url = '%sdocuments/%s/' % (base_url, 'test_upload_00')

headers = {}

data = {'title': 'test_upload_00'}
path = 'documents/tests/files/test_upload_00.txt'
project_file = open(path, 'rb')
files = {'project_file': ('test_upload_00.txt', project_file, "text/plain")}

response = requests.post(
    api_list_url,
    data=data,
    headers=headers,
    files=files
)
project_file.close()
print(response.text)
assert response.status_code == 201
print('POST:')
print(response.status_code)
print(response.text)


data = {'title': 'test_upload_00'}
path = 'documents/tests/files/test_upload_01.txt'
project_file = open(path, 'rb')
files = {'project_file': ('test_upload_01.txt', project_file, "text/plain")}
response = requests.put(
    api_detail_url,
    data=data,
    headers=headers,
    files=files
)
project_file.close()
assert response.status_code == 200
print('PUT:')
print(response.status_code)
print(response.text)

print('GET/DELETE:')
response = requests.get(api_list_url)
for f in response.json():
    api_detail_url = '%sdocuments/%s/' % (base_url, f['title'])
    print(api_detail_url)
    response = requests.delete(api_detail_url)
    assert response.status_code == 204
    print(response.text)
