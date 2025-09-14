import requests
from bs4 import BeautifulSoup

def süpergol(url):
    try:
        response = requests.get(url)
        

        if response.status_code == 200:
 
            soup = BeautifulSoup(response.text, 'html.parser')
            

            golcü = soup.select('td>b>a')[:10]
            golsayısı = soup.select('td>b>span')[:10]
            
            
            if golcü and golsayısı:
                print("---Trentyol Süperlig gol kıralıgı --")
                print("")
                for golcu, golsayisi in zip(golcü, golsayısı):
                    print(f"{golcu.get_text(strip=True)}: {golsayisi.get_text(strip=True)} gol")
                    print("-" * 30)
                    print("")
            else:
                print("Sayfada haber başlığı bulunamadı.")
                
        else:
            print(f"Hata: URL'ye erişilemedi. Durum Kodu: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Bir hata oluştu: {e}")
