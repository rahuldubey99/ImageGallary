
from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def gallary(request):
    page = request.GET.get('page')
    photosAll = Photo.objects.all()
    category = request.GET.get('category')
    photos = []
    if category == "None" or category == None:
        photos = Photo.objects.all()
    else:
        photosid = []
        for photo in photosAll:
            x = [i for i in photo.name]
            for j in x:
                if j == category:
                    photosid.append(photo.id)
                    break
        photosnamesitems = [Photo.objects.filter(
            id=photosid[x]) for x in range(len(photosid))]
        for x in photosnamesitems:
            for name in x:
                photos.append(name)
    all_photos = Paginator(photos, 8)
    try:
        post = all_photos.page(page)
    except PageNotAnInteger:
        post = all_photos.page(1)
    except EmptyPage:
        post = all_photos.page(all_photos.num_page)
    context = {"photos": post, "category": category}
    return render(request, 'photos/gallary.html', context)


def viewPhoto(request, pk):
    photos = Photo.objects.get(id=pk)
    context = {'photo': photos}
    return render(request, 'photos/photo.html', context)


def addPhoto(request):
    categorys = Photo.tags

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('image')
        item = data.getlist('category')
        for image in images:
            Photo.objects.create(name=item, image=image)
    categories = []

    for category in categorys:
        categories.append(category[1])
    return render(request, 'photos/add.html', {"categories": categories})
