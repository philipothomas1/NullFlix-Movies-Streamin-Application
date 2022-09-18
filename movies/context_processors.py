from .models import MovieGenre,Movie
from django.shortcuts import render
from django.db.models import Q

def moviegenre(request):
    return{'moviegenre':MovieGenre.objects.all()}


def movies(request):
    movies=Movie.objects.all()
    context={
        'movies':movies,   
    }
    return render (context)
    
# def search_items(request):
#     if request.method == 'GET':
#         # form=RateForm(request.POST)
#         # if form.is_valid()
#         query= request.GET.get('q')
#         # pubs = Inventory.objects.aggregate(Count('item_name'))
#         submitbutton= request.GET.get('submit')

#         if query is not None:
#             lookups= Q(Title__icontains=query)
#             results= Movie.objects.filter(lookups).distinct()
#             context={'results': results,
#                         'submitbutton': submitbutton,
#                         }

#             return render(request, 'index.html', context)

#         else:
#             return render(request, 'index.html')

#     else:
#         return render(request, 'index.html')