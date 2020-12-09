from bs4 import BeautifulSoup
import requests
from django.shortcuts import render
from django.views import generic
from lxml import html

class HomePageView(generic.ListView):
    template_name = 'home.html'

def getHtml(request):
    if request.method == "POST":
        website_link = request.POST.get('web_link', None)
        element = request.POST.get('element', None)
        url = website_link
        source=requests.get(url).text 
        all_links = []
        
        soup = BeautifulSoup(source, "html.parser")

        # Wszystkie elementy
        items = soup.find_all(element)
        amount = len(items)     

        for i in items:
            # Szukanie klasy
            find_class = i.get('class')
            if find_class is None:
                find_class = "--"   

            # Szukanie id
            find_id = i.get('id')
            find_id = find_id.strip() if find_id is not None else "-"

            # Szukanie href
            find_href = i.get('href')
            find_href = find_href.strip() if find_href is not None else "-"

            # Tekst
            get_text = i.text
            get_text = get_text.strip() if get_text is not None else "-"

            # Obrazki
            find_src = i.get('src')            
            if find_src is None:
                find_src = "-"
            
            find_alt = i.get('alt')
            find_alt = find_alt.strip() if find_alt is not None else "-"

            all_links.append({"find_id": find_id, "find_class": find_class, "find_href": find_href, "get_text": get_text, 'find_alt':find_alt, 'find_src': find_src})

        return render(request, 'scrapped.html', {'all_links':all_links, 'amount': amount, 'url': url, 'element':element})

    return render(request, 'scraping.html')

def xml(request):

    # zad1    
    url = 'https://starwars.fandom.com/wiki/Star_Wars'    
    path = '//*[@id="toc"]/ul/li[2]/ul/li[1]/ul/li[1]/a' 
    # odpowiedź na zapytanie   
    response = requests.get(url)
    # ciąg bajtów    
    data = response.content    
    # fromstring wymaga ciągu bajtów
    source = html.fromstring(data)    
    # element na stronie
    tree = source.xpath(path)
    # wybranie pierwszego elementu
    lxml1 = tree[0].text_content()
    
    # zad2    
    url = 'https://starwars.fandom.com/wiki/Star_Wars'    
    path = '//*[@class="quote"]'    
    response = requests.get(url)    
    data = response.content    
    source = html.fromstring(data)    
    tree = source.xpath(path)
    lxml2 = tree[0].text_content()

    return render(request, 'xpath.html', {'lxml1': lxml1,'lxml2': lxml2 })

def labs(request):   
    # ------------ przykład 1 ---------------------------------------------- 
    url = requests.get("https://starwars.fandom.com/wiki/Star_Wars")
    soup = BeautifulSoup(url.content, "html.parser")

    all_ex = []
    first_p = soup.select("p")[0].text
    another_p = soup.select("p")[1].text
    p_amount = len(soup.select("p"))
    
    # ------------ przykład 2 ---------------------------------------------
    page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/"
    )
    soup = BeautifulSoup(page.content, "html.parser")

    top_items = []

    products = soup.select("div.thumbnail")
    for elem in products:
        title = elem.select("h4 > a.title")[0].text
        review_label = elem.select("div.ratings")[0].text
        info = {"title": title.strip(), "review": review_label.strip()}
        top_items.append(info)

    # ------------ przykład 3 ---------------------------------------------

    page = requests.get(
        "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/"
    )
    soup = BeautifulSoup(page.content, "html.parser")

    image_data = []

    images = soup.select("img")
    for image in images:
        src = image.get("src")
        alt = image.get("alt")
        image_data.append({"src": src, "alt": alt})

    # ------------ przykład 4 ---------------------------------------------

    all_products = []

    for product in products:
        name = product.select('h4 > a')[0].text.strip()
        description = product.select('p.description')[0].text.strip()
        price = product.select('h4.price')[0].text.strip()
        reviews = product.select('div.ratings')[0].text.strip()
        image = product.select('img')[0].get('src')

        all_products.append({
            "name": name,
            "description": description,
            "price": price,
            "reviews": reviews,
            "image": image
        })


    return render(request,'labs.html',{'first_p':first_p, 'another_p':another_p, 'p_amount':p_amount, 'top_items':top_items, 'image_data':image_data, 'all_products':all_products})
    