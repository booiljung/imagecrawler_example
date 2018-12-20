from selenium import webdriver
import imagecrawler as imcr

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('headless')
chrome_options.add_argument('--window-size=1024,1024')
#chrome_options.add_argument("disable-gpu")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")
chrome_options.add_argument("--lang=en_US")
#chrome_options.add_argument("--lang=ko_KR")

driver = webdriver.Chrome('/home/booil/Downloads/chromedriver', chrome_options=chrome_options)
driver.implicitly_wait(3)

keyed_image_urls = imcr.search_images_urls(driver, ['얼룩말', '연필'])
print(keyed_image_urls)

imcr.write_image_urls_as_file(keyed_image_urls, './testdata/test_urls.txt')

