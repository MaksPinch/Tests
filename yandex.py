import requests

def create_folder(name):
    yd_url = 'https://cloud-api.yandex.net/v1/disk/resources'
    token = 'y0__xC3krj5BxjblgMgwcDEqBK5Y1vHXzbZ5ivKTKLF9q7RKOxfaQ'
    params = {'path': name}
    headers = {'Authorization': f'OAuth {token}'}

    response = requests.put(yd_url, params=params, headers=headers)

    if response.status_code == 201:
        return 'Папка успешно создана.'

    elif response.status_code == 409:
        return 'Папка уже существует.'

    else:
        return 'Ошибка'



