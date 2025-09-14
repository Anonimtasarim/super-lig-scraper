import requests
from bs4 import BeautifulSoup
from super_lig_durumu import süperlig
from super_gol_kıralıgı import süpergol
from fanatik_haber import fanatik
from mackolik_haber import mackolik
print("""
  ##                                               #        #
 #  #                                              #
  #     #  #   ###     ##    # #                   #       ##     ##
   #    #  #   #  #   # ##   ## #                  #        #    #  #
 #  #   #  #   #  #   ##     #                     #        #    # ##
  ##     ###   ###     ###   #                     ####    ###    # #
               #                                                    #
               #                                                  ##

""")
print("Menü")
print("-puan durumu")
print("-gol kıralıgı")
print("-haberler")
while True:
    mesaj = input(">>>")
    if mesaj == "puan durumu":
        süperlig('https://www.tff.org/default.aspx?pageID=198')
    elif mesaj == "gol kıralıgı":
        süpergol('https://www.tff.org/default.aspx?pageID=821')
    elif mesaj == "q":
        break
    elif mesaj == "haberler":
        print("1-fanatik")
        print("2- mackolik")
        print("q-ile çkış yapabilrisiniz")

        while True:
            haberin = input(">>>")
            if haberin == "1":
                # print("trt spor açılıyor")
                fanatik('https://www.fanatik.com.tr/futbol/')
            elif haberin == "2":
                mackolik('https://www.mackolik.com/futbol/haberler/arsiv')
                
            elif haberin == "q":
                break
            else:
                print("lütfen bunlardan birini seçin!")
                print("1-fanatik")
                print("2- mackolik")
                print("q-ile çkış yapabilrisiniz")
    else:
        print("lütfen bunlardan birini seçin!")   
        print("-puan durumu")
        print("-gol kıralıgı")
        print("-haberler")
        print("q-ile çkış yapabilrisiniz")
