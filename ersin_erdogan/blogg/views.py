from django.shortcuts import render
from models import headers, contents, list
from django.http import HttpResponse, Http404

def see_all(request):
    return render(request, "text.txt", {"list":list})

def see_one(request, blog_id):
    try:
        return render(request, "text2.txt", {"blog_id":int(blog_id)+1,"selected_head":list[int(blog_id)][0], "selected_body":list[int(blog_id)][1]})

    except IndexError:
        raise Http404("THERE ARE NO MORE ENTRY THAN "+blog_id)