import imagecrawler as imcr

#imcr.save_image_urls_as_file(keyed_image_urls, './testdata/test_urls.txt')

urls = imcr.read_image_urls_from_file('./testdata/test_urls.txt')
print(urls)

imcr.write_image_urls_as_file(urls, './testdata/test_urls2.txt')
urls2 = imcr.read_image_urls_from_file('./testdata/test_urls2.txt')

assert (str(urls) == str(urls2))
print('test ok')