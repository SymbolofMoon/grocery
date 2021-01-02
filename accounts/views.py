from django.shortcuts import render,redirect,get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from .models import Item
from .forms import ListForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.



def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')    
def home(request):
	# item=None  

	if request.method == "GET" :
		date1 = request.GET.get('date1','')
		if(date1==''):
			item = Item.objects.filter(buyer=request.user)
			data = {'item':item}
			return render(request, 'index.html', data)

			
		else:
			item = Item.objects.filter(buyer=request.user, added_date=date1)
			data={'item': item}
			
			return render(request,'index.html',data)
    
	# data= {'item':item}
	# print(data)
	# return render(request,'index.html',data)			
	# if request.method == "GET":
	# 	date1 = request.GET.get('date1','')
	# 	if (date1==''):
	# 		item = Item.objects.filter(buyer=request.user)
    #     else:
	# 	    item = Item.objects.filter(buyer=request.user)

	# data = {'item': item} 
	# return render(request, "index.html",data)		
		
		
    # item = Item.objects.filter(buyer=request.user)

    
    # 
    
    # 
    

@login_required(login_url='login')
def update(request,pk):
    item=Item.objects.get(id=pk)

    form=ListForm(instance=item)
    if request.method=="POST":
        form=ListForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form}
    return render(request, "update.html",context)

@login_required(login_url='login')       
def add(request):

    # form=ListForm()
    # if request.method=="POST":
    #     form=ListForm(request.POST)
    #     if form.is_valid():
	# 		pass

			
    # context = {'form':form}
    # return render(request, "add.html",context)    

	form=ListForm()
	if request.method=="POST":
		form=ListForm(request.POST)
		if form.is_valid():
			item=form.save(commit=False)
			item.buyer=request.user
			item.save()
			return redirect('/')


	context = {'form': form}
	return render(request,"add.html",context)		
    
def search(request):

	date1 = request.GET['date']
	if date1=='':
		return redirect('/')
	item = Item.objects.filter(buyer=request.user, added_date=date1)
	data = {'item':item}
	return render(request,"index.html", data)


def delete(request,pk):
	
	obj = Item.objects.filter(id=pk)

	
	obj.delete()

	item = Item.objects.filter(buyer=request.user  )
	context ={'item':item}
	return redirect("/")

    
		

	return render(request,"index.html",context)	



