from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages


# Create your views here.
def home(request): # when you create a page, create a view
    # pk_fcecccc2b1054292b671060ad9f9418
    import requests # you need to request the API
    import json # then parse it using JSON
    if request.method  == 'POST':
        ticker = request.POST['ticker'] # this becomes the data that the user enters into the form (search bar)
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_fcecccc2b1054292b671060ad9f94188") 
        # you can then concatenate ticker into the URL

        try:
            api = json.loads(api_request.content) # parses api_request and throws an error if it returns nothing
        except Exception as e:
            api = "Error..." # this is returned if the API isn't returned
            return render(request, 'home.html', {'api' : api})
    else:
        return render(request, 'home.html', {'ticker' : 'Enter a Ticker Symbol above'}) # if user hasn't submitted anything return to homepage and post text
    

    return render(request, 'home.html', {'api' : api}) # then you need to pass a request object, the page you want and the brackets are the content you want to access



def about(request):
    return render(request, 'about.html', {})

def add_stock(request):
    import requests
    import json 

    if request.method  == 'POST': # if a post request has been made to the database
        form = StockForm(request.POST or None)  # creates a stock form regardless of whether a post request has been made  
        
        if form.is_valid(): # if form fits criteria i.e. if ticker symbol is 5 characters or less
            form.save()
            messages.success(request, ("Stock Has Been Added")) # if form exists post this message
            return redirect('add_stock')
    else:
        ticker = Stock.objects.all()

        output = []

        for ticker_item in ticker:
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_fcecccc2b1054292b671060ad9f94188")
            try:
                api = json.loads(api_request.content) # parses api_request and throws an error if it returns nothing
                output.append(api) # save output to the list
            except Exception as e:
                api = "Error..." # this is returned if the API isn't returned

        return render(request, 'add_stock.html', {'ticker' : ticker, 'output' : output}) # outputs api data 

def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id) # you must first grab the item's id from database, pk is the id number
    item.delete() # you then need to call delete on the item
    messages.success(request, ('Your stock has been deleted.'))
    return redirect(delete_stock)

def delete_stock(request):
    ticker = Stock.objects.all()

    return render(request, 'delete_stock.html', {'ticker': ticker})

