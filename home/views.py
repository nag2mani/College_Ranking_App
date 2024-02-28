from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import *
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout #login for storing session.
from django.contrib.auth.decorators import login_required
from django.conf import settings
import pandas as pd
from home.models import *
import json

def home(request):
    return render(request, 'index.html')



def contest(request):

    if request.method == "POST":
        column_to_sort = request.POST.get('headline')
    else:
        column_to_sort = "Original_Rank"

    df = pd.read_excel("nirf.xlsx")

    # To sort the df according to user input.
    if column_to_sort in df.columns:
        sorted_df = df.sort_values(by=column_to_sort)
    else:
        sorted_df = df

    # Converting to json to send as context.
    json_data = sorted_df.reset_index().to_json(orient="records")
    # arr = []
    arr = json.loads(json_data)
    return render(request, 'contest.html', context={"dict_data" : arr})

