from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Story, Historical, Biography, Contact ,Orders
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib import messages


def index(request):
    Story_books = Story.objects.all()
    Historical_books = Historical.objects.all()
    Biography_books = Biography.objects.all()
    return render(request, 'index.html', {'Story_books': Story_books, 'Historical_books': Historical_books, 'Biography_books': Biography_books})


def searchMatch(query, item):
    if query in item.book_name.lower() or query in item.book_title.lower():
        return True
    else:
        return False


def search(request):
    my_query = request.GET.get('search_query')
    Story_books = Story.objects.all()
    Historical_books = Historical.objects.all()
    Biography_books = Biography.objects.all()
    new_Story_books = [i for i in Story_books if searchMatch(my_query, i)]
    new_Historical_books = [
        i for i in Historical_books if searchMatch(my_query, i)]
    new_Biography_books = [
        i for i in Biography_books if searchMatch(my_query, i)]
    return render(request, 'index.html', {'Story_books': new_Story_books, 'Historical_books': new_Historical_books, 'Biography_books': new_Biography_books})


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        return redirect('/')
    return render(request, 'contact.html')


def tracker(request):
    return render(request, 'tracker.html')


def productview(request, book, id):
    # fetch the product according to the id
    # sbook = Story.objects.filter(id=id)
    # hbook = Historical.objects.filter(id=id)
    # bbook = Biography.objects.filter(id=id)
    # if sbook is not None:
    #     print(sbook)
    #     return render(request, 'productview.html', {'product': sbook[0]})
    # if hbook is not None:
    #     print(hbook)
    #     return render(request, 'productview.html', {'product': hbook[0]})
    # if bbook is not None:
    #     print(bbook)
    #     return render(request, 'productview.html', {'product': bbook[0]})

    if book == "story_book":
        sbook = Story.objects.filter(id=id)
        return render(request, 'productview.html', {'product': sbook[0]})
    if book == "historical_book":
        hbook = Historical.objects.filter(id=id)
        return render(request, 'productview.html', {'product': hbook[0]})
    if book == "biography_book":
        bbook = Biography.objects.filter(id=id)
        return render(request, 'productview.html', {'product': bbook[0]})

    # return render(request, 'productview.html',{'sbook':sbook[0],'hbook':hbook[0],'bbook':bbook[0]})


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'checkout.html', {'thank': thank, 'id': id})
    return render(request, 'checkout.html')
