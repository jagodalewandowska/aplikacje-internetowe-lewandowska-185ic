from bs4 import BeautifulSoup
import requests
from django.shortcuts import render

from django.views import generic
# Create your views here.
class HomePageView(generic.ListView):
    template_name = 'home.html'

def requestText(request):
    if request.method == "POST":
        website_link = request.POST.get('web_link', None)
        #requests
        url = website_link #url
        source=requests.get(url).text # url source
        soup = BeautifulSoup(source, "html.parser")

        all_links = []
        links = soup.select("a")
        for i in links:
            text = i.text
            text = text.strip() if text is not None else ""
            all_links.append({"text": text})
        return render(request, 'scraping.html', {'all_links':all_links})

    return render(request, 'scraping.html')