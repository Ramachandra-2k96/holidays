from django.shortcuts import render
from  myapp.forms import inputform
import os
# Create your views here.
def home(request):
    if request.method=="POST":
        form =  inputform(request.POST)
        if form.is_valid():
            data = form.cleaned_data.get('stateinput')
            list1=give_holidays(data)
            return render(request,'myapp/index.html',{"data":list1,"form":form})
    else :
        form = inputform()
    return render(request,'myapp/index.html',{"form":form})

def give_holidays(data):
    import csv
    list1 =[]
    holiday=[]
    with open("myapp/templates/myapp/Holidays_2024.csv", 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            list1 .append([row[0],row[1], row[2], row[3].replace("\n", " ").replace('&',',')])
    for l in list1:
        if data in l[3]:
            if "except" not in l[3]:
                holiday.append([l[0],l[1],l[2]]) # It wil print if the KA is present in column and the word except is not present
        elif "National" in l[3] and "except" not in l[3]:
            holiday.append([l[0],l[1],l[2]])# print if its a national holiday
    return holiday


