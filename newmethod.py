from requests_html import HTMLSession

urls = ['https://www.amazon.com/Sceptre-E275W-19203R-Monitor-Speakers-Metallic/dp/B077SRKKHQ/ref=sr_1_1_sspa?crid=20JTH18KOA8M7&keywords=tv&qid=1660742104&s=electronics&sprefix=t%2Celectronics-intl-ship%2C289&sr=1-1-spons&th=1',
           'https://www.amazon.com/Hisense-40-Inch-Chromecast-Compatibility-40A4H/dp/B09WQ3FQ2G/ref=sr_1_1?crid=20JTH18KOA8M7&keywords=tv&qid=1660748338&s=electronics&sprefix=t%2Celectronics-intl-ship%2C289&sr=1-1',
           'https://www.amazon.com/Samsung-Electronics-UN32N5300AFXZA-1080p-Smart/dp/B07CL4GLQW/ref=sr_1_5?crid=20JTH18KOA8M7&keywords=tv&qid=1660748338&s=electronics&sprefix=t%2Celectronics-intl-ship%2C289&sr=1-5']

def getPrice(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(timeout=20)
    # r.html.render(sleep=1)


    product = {
        'title': r.html.xpath('//*[@id="productTitle"]', first = True).text,
        'price': r.html.xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[1]', first = True).text
    }
    print(product)
    return product

tvprices = []
for url in urls:
    tvprices.append(getPrice(url))

print(len(tvprices))
