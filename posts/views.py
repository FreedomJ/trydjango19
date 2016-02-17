from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages
# Create your views here.


# function based view
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():     # all field is exist
        instance = form.save(commit=False)
        print form.cleaned_data.get('title')
        instance.save()
    # if request.method == "POST":
    #     print request.POST.get("content")
    #     print request.POST.get("title")
        # message succeed
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)


def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": "Detail",
        "instance": instance
    }
    return render(request, "post_detail.html", context)


def post_list(request):
    querySet = Post.objects.all()
    context = {
            "object_list": querySet,
            "title": "List"
        }
    # if request.user.is_authenticated():
    #     context = {
    #         "title": "My User List"
    #     }
    # else:
    #     context = {
    #         "title": "List"
    #     }
    return render(request, "index.html", context)


def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():     # all field is exist
        instance = form.save(commit=False)
        print form.cleaned_data.get('title')
        instance.save()
        # message succeed
        messages.success(request, "Item Saved", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": "Detail",
        "instance": instance,
        "form": form,
    }
    return render(request, "post_form.html", context)


def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully Deleted")
    return redirect('posts:list')

# class based view
