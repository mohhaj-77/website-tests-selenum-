from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time



tarayici = webdriver.Chrome('./chromedriver') #nesne oluşturarak chrome ile iletişimi kurduk.
tarayici.get("https://www.google.com") # google adresine gidiyoruz
print(tarayici.title) #ekrana çıkartıyoruz
arama_alan1 = tarayici.find_element_by_name("q") #arama boş alanı adıyla kullandık
arama_alan1.clear() #boş alanı yazı varsa temizle dedik
arama_alan1.send_keys("hello world") # hello world yaz
time.sleep(3) #3 saniye dur sonra devam et
arama_alan1.send_keys(Keys.RETURN) #boş alana verdiğimiz değeri döndür
time.sleep(3)

arama_alan2 = tarayici.find_element_by_name("q") #yine den çağır
arama_alan2.clear() #önceki yazı temizle
arama_alan2.send_keys("java") #boş alanda java yaz
time.sleep(3)
tarayici.find_element_by_name("q").send_keys(Keys.ENTER) # enter e bas
time.sleep(3)

tarayici.get("https://www.google.com/search?q=java&rlz=1C1GCEA_enTR994TR994&tbm=isch&sxsrf=APq-WBtN4fwhHDCMZQNQ8hyWyzm1s2FJOg:1649493358119&source=lnms&sa=X&ved=2ahUKEwjV3q3NyYb3AhU2REEAHSlaCO4Q_AUoAXoECAEQAw&biw=944&bih=625&dpr=1")
time.sleep(2)
tarayici.get("https://www.google.com/search?q=java&rlz=1C1GCEA_enTR994TR994&tbm=isch&sxsrf=APq-WBtN4fwhHDCMZQNQ8hyWyzm1s2FJOg:1649493358119&source=lnms&sa=X&ved=2ahUKEwjV3q3NyYb3AhU2REEAHSlaCO4Q_AUoAXoECAEQAw&biw=944&bih=625&dpr=1#imgrc=oQsIfeD6p6_vIM")
time.sleep(2)


tarayici.get("https://github.com/login")
time.sleep(2)

email = "180290608@edu.firat.tr"
parola = "1234567"

tarayici.find_element_by_id("login_field").send_keys(email)# id yi kullanarak boş alana mail değeri aktarıyoruz.
time.sleep(1)
tarayici.find_element_by_id("password").send_keys(parola) # id yi kullanarak boş alana parola değeri aktarıyoruz.
time.sleep(3)
tarayici.find_element_by_name("commit").click() #bottuna bas diyoruz.

tarayici.close() #pencereyi (nesneyi) kapat.
