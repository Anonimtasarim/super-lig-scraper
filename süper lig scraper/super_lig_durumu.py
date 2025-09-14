import requests
from bs4 import BeautifulSoup

def süperlig(url):  
    try:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            sıralama = soup.select('td>b>a')[9:]
            # puandurumu = soup.select('tr>td.griBG1>b>span,tr>td.griBG2>b>span')

        if sıralama:
                print("---Trentyol Süperlig puan durumu--")
                print("")
                for takim in sıralama:
                    # Başlık metnini temizleyerek ekrana yazdırırız.
                    print(takim.get_text(strip=True) ) 
                    print("-" * 20)
                    print("")
        else:
            print(f"Hata: URL'ye erişilemedi. Durum Kodu: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Bir hata oluştu: {e}")



