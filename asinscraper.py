from requests_html import HTMLSession

url = 'https://www.amazon.com/s?k=nvme+1tb'

s = HTMLSession()
r = s.get(url)
r.html.render(timeout=20)

#print(r.html.find('title', first=True).full_text)

products = r.html.find('div[data-asin]')
#print(products)
asins = []
for product in products:
    if product.attrs['data-asin'] !='':
        asins.append(product.attrs['data-asin'])

print(asins)
print(len(asins))
