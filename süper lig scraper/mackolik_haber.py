import requests
from bs4 import BeautifulSoup

def mackolik(url):
    try:
        response = requests.get(url)
        

        if response.status_code == 200:
 
            soup = BeautifulSoup(response.text, 'html.parser')
            

            haber = soup.select('a>h2.widget-article__teaser')[:10]
            
            if haber:
                print("---mackolik haber --")
                print("")
                for fotball in haber:
                    print(fotball.get_text(strip=True))
                    print("-" * 30)
                    print("")
            else:
                print("Sayfada haber başlığı bulunamadı.")
                
        else:
            print(f"Hata: URL'ye erişilemedi. Durum Kodu: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Bir hata oluştu: {e}")