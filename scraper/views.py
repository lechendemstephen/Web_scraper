from django.shortcuts import render, redirect
import requests 
from bs4 import BeautifulSoup
from .models import Link
from .forms import LinkForm
# Create your views here.

def scrape(request):
    if request.method == "POST": 

            website = request.POST.get('site', '')

            page = requests.get(website)
            soup = BeautifulSoup(page.text, 'html.parser')

            for link in soup.find_all('a'): 
                link_address = link.get('href')
                link_text = link.string
                Link.objects.create(
                    address = link_address,
                    name = link_text
                )
                return redirect('home')

    return render(request, 'scraper/result.html', {
        'links': Link.objects.all(),
    })


def delete(request): 
     data = Link.objects.all()
     data.delete()
     return redirect('home')
     



     
     
     