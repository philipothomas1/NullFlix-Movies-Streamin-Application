from ast import For
from django.core.mail import EmailMessage
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import JsonResponse
from django.views.generic import ListView,DetailView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Avg
# from matplotlib.pyplot import title
# from matplotlib.style import context
# from matplotlib.pyplot import title
from actor.models import Actor
from movies.forms import RateForm
from .models import Movie, MovieGenre,Review,SubPlan,SubPlanFeature,Subscription
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from actor.models import Actor
from tvseries.models import TVSeries,Season,Episode
from django.core.paginator import Paginator
from django.contrib import messages
from django.template.loader import get_template
from datetime import timedelta,date
import stripe
import datetime
from movies import models
# Create your views here.

@login_required
def home(request):
    movies=Movie.objects.filter().order_by('-added_on')[0:8]
    mvies=Movie.objects.all()
    actors=Actor.objects.all()
    if 'term' in request.GET:
        qs=Movie.objects.filter(Title__istartswith=request.GET.get('term'))

        titles=list()
        for movie in qs:
            titles.append(movie.Title)
            return JsonResponse(titles,safe=False)
        

    
    context={
        'movies':movies,
        'actors':actors,
        'mvies':mvies
        

    }
    return render (request,'index.html',context)

# class MoviesListView(ListView):
#     model = Movie
#     # context_object_name='movies'
#     template_name = "index.html"


# class MovieDetailView(DetailView):
#     model = Movie
#     template_name = "movie_detail.html"
@login_required
def movieDetail(request,pk):
    
    queryset = Movie.objects.get(id=pk)
    related_movies=Movie.objects.filter(genre=queryset.genre).exclude(id=pk)
    # print(related_movies)
    actors = queryset.Actors.all()
    print(actors)
  
    # moviegenre=Movie.objects.all()
    # context={
    #     "queryset": queryset,  
    # }

    moviee=Movie.objects.get(id=pk)
    reviews = Review.objects.filter(movie=moviee)
    reviewsavg = reviews.aggregate(avg=Avg('rate'))['avg']
    reviews_avg=round(reviewsavg,1)
    # reviewsS = Review.objects.filter(movie=moviee).values()
    # print(reviews_avg)
    
    reviews_count = reviews.count()
    # print(reviewsavg['rate_avg'])
    
    # print(reviewsavg)
    # print(reviews_count)
    user=request.user



    if request.method=='POST':
        

        form=RateForm(request.POST)
        if form.is_valid():
            rate=form.save(commit=False)
            rate.user=user
            rate.movie=moviee
            rate.save()
            print("You have successfully rated this movie")
            messages.success(request, 'You have successfully rated this movie')
            # return HttpResponseRedirect(reverse('movies:movieDetail', args=[id]))
    else:
        form = RateForm()

    # template = loader.get_template('movie_detail.html')

    qs=[rate.user for rate in reviews]

    # print(reviewsS)
    print(qs)
    

    context = {
        "queryset": queryset,  
        'form': form, 
        'movie': moviee,
        'reviews': reviews,
        'reviewsavg': reviewsavg,
        'reviews_count': reviews_count,
        'reviews_avg':reviews_avg,
        'related_movies':related_movies,
        'actors':actors,
        'qs':qs
        

    }

    # return HttpResponse(template.render(context, request))




    return render(request, "movie_detail.html", context)


@login_required
def movies_in_genre(request,slug):
    movie_genre=get_object_or_404(MovieGenre, slug=slug)
    related_movies=Movie.objects.filter(genre=movie_genre)
    genres=MovieGenre.objects.all()
    # print(moviegenre)
    print(related_movies)

    context={'related_movies':related_movies,'movie_genre':movie_genre,'genres':genres}
    return render(request,'movies_in_genre.html',context)

@login_required
def moviespl(request,pk):

    # queryset = Movie.objects.get(id=pk)
    # related_movies=Movie.objects.filter(genre=queryset.genre).exclude(id=pk)
    # print(related_movies)
    queryset = Actor.objects.get(id=pk)
    # que=get_object_or_404(Actor, slug=slug)
    actorsmovies = queryset.movies.all()

    # print(moviegenre)
    print(actorsmovies)

    context={'actorsmovies':actorsmovies,}
    return render(request,'movieplayedbythisactor.html',context)


def search_items(request):
    if request.method == 'GET':
        # form=RateForm(request.POST)
        # if form.is_valid()
        query= request.GET.get('q')
        # pubs = Inventory.objects.aggregate(Count('item_name'))
        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(Title__icontains=query)
            results= Movie.objects.filter(lookups).distinct()
            context={'results': results,
                     'submitbutton': submitbutton,
                     }

            return render(request, 'searchresults.html', context)

        else:
            return render(request, 'searchresults.html')

    else:
        return render(request, 'searchresults.html')



@login_required
def tvseries(request):
    series=TVSeries.objects.all()
    # queryset = Season.objects.get(id=pk)
    # season=TVSeries.objects.filter(tv_series=queryset)
    page_num = request.GET.get('page', 1)

    paginator = Paginator(series, 1)
    tvseries = paginator.page(page_num)
    actors=Actor.objects.all()
    # print(season)
    # context= {
    #     'season':season
    # }
  
    
    context={
        'series':series,
        'tvseries':tvseries        

    }
    return render (request,'tvseries.html',context)
@login_required
def season_in_series(request,pk):
    queryset = TVSeries.objects.get(id=pk)
    series=Season.objects.filter(tv_series=queryset)
    series_count=series.count()

    print(series)
    print(series_count)
    context= {
        'series':series,
        'queryset':queryset,
        'series_count':series_count
    }

    return render(request,'tvseries_seasons.html',context)
@login_required
def episodes_in_season(request,pk):
    queryset = Season.objects.get(id=pk)
    episodes=Episode.objects.filter(season=queryset)
    episodes_count=episodes.count()
    print(episodes)
    print(episodes)
    context= {
        'episodes':episodes,
        'queryset':queryset,
        'episodes_count':episodes_count
    }

    return render(request,'episodes_in_season.html',context)
@login_required
def episode_detail(request,pk):
    # queryset = Season.objects.get(id=pk)
    # episodes=Episode.objects.filter(season=queryset)
    episode=Episode.objects.get(id=pk)
    print(episode)
    print(episode)
    context= {
        'episode':episode,
        # 'queryset':queryset
    }

    return render(request,'episode_detail.html',context)

from django.db.models import Count

@login_required

def choosesubscriptionplan(request):
    subplan = SubPlan.objects.all()
    # validity_days
    # subplan2 = SubPlan.objects.annotate(total=Count('subPlan_id')).all()
    # print(total)

    subplanfeatures=SubPlanFeature.objects.all();
    current_subplan=Subscription.objects.filter(user=request.user)
    print(current_subplan)
    # expire_date=current_subplan.reg_date+timedelta(days=current_subplan.plan.validity_days)
    current_date = datetime.date.today()
    # print(current_date)
    # print(expire_date)
    # if current_date == expire_date:
        # print("expired")

    # expired=False
    # pdays=None
    # pvalidity=None
    # # user=request.user
    # # if request.user.is_authenticated:
    # user=User.objects.get(id=user_id)
    # subplan=SubPlan.objects.get(id=plan_id)
    # check_package=Subscription.objects.filter(user=user,plan=subplan).count()

    # if check_package > 0:
    #     pdata=Subscription.objects.filter(user=user,plan=subplan).order_by('-id').first()
    #     today=date.today()
    #     pdate=pdata.reg_date
    #     pdays=(today-pdate).days
    #     pvalidity=pdata.plan.validity_days
    #     if pdays > pvalidity:
    #         expired=True
    # else:
    #     expired=False

    # return expiredplan
    # print(subplanfeatures.sub)
    # for feature in subplanfeatures:
    #     print(feature.subplan.title)

        # for feature in subplanfeatures:
        #     print(feature.subplan.title)
        # print(feature.title)
    # episodes=Episode.objects.filter(season=queryset)
    # episodes_count=episodes.count()
    # print(episodes)
    # print(episodes)
    # for pricing in subplanfeatures:
    #     for features in pricing.subplan.title:
    #         print(features)




    context= {
         'subplan':subplan,
         'subplanfeatures':subplanfeatures
    #     'queryset':queryset,
    #     'episodes_count':episodes_count
    }

    return render(request,'choosesubscriptionplan.html',context)
@login_required
def checkout(request,plan_id):
    subplanDetail=SubPlan.objects.get(pk=plan_id)  
    context= {
         'subplanDetail':subplanDetail,
         # 'queryset':queryset
     }

    return render(request,'checkout.html',context)


stripe.api_key = 'sk_test_51Kl7mfDc8sIiukTtsEtdlTVD477mRGgI9sAJHF4mJResY2uNHaqvAYX18iSfMJGZzuqyhQb3JyvAaDlntc9RDa2l00e33y9FCj'


def checkoutsession(request,plan_id):
    subplanDetail=SubPlan.objects.get(pk=plan_id) 
    subplan=SubPlan.objects.get(id=plan_id)
    print(subplan.id)
    print(subplanDetail)

    user=request.user.id
    # plan=SubPlan.objects.get(id=plan_id)
    check_package=Subscription.objects.filter(user=user,plan=subplan)
    # check_subplan=Subscription.objects.filter(user=user,plan=plan).count()
    current_subplan=Subscription.objects.filter(user=request.user).count()
    print(current_subplan)


    print(user)
    
    if current_subplan == 1 :
        print("True") 
    else:
        print("False") 
 

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items= [{
        'price_data': {
            'currency': 'tzs',
            'product_data': {
            'name': subplanDetail.title,
            },
            'unit_amount': subplanDetail.subprice * 100,
        },
        'quantity': 1,
        }],
    mode='payment',
    # These placeholder URLs will be replaced in a following step.
    success_url='http://127.0.0.1:8000/paymentsuccess?session_id={CHECKOUT_SESSION_ID}',
    cancel_url='http://127.0.0.1:8000/paymentcanceled',
    client_reference_id=plan_id
  )

    return redirect(session.url, code=303)
@login_required
def success(request):
    session = stripe.checkout.Session.retrieve(request.GET['session_id'])
    plan_id=session.client_reference_id
    user=request.user
    plan=SubPlan.objects.get(pk=plan_id)  
    Subscription.objects.create(
        plan=plan,
        user=user,
        price=plan.subprice,
        # reg_date=plan.reg_date
    )
    subject='Order Email'
    html_content=get_template('orderemail.html').render({'title':plan.title})
    from_email='philipthomas1738@gmail.com'
    msg = EmailMessage(subject, html_content, from_email, [request.user.email])
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()

    return render(request,'success.html')

def cancel(request):
    return render(request,'cancel.html')

@login_required
def userprofile(request):
    # user=request.user
    # if request.user.is_authenticated:
    username=request.user
    current_subplan=Subscription.objects.get(user=request.user)
    # print(current_subplan)
    expire_date=current_subplan.reg_date+timedelta(days=current_subplan.plan.validity_days)
    context={
        'username':username,
        'current_subplan':current_subplan,
        'expire_date':expire_date
    }
    return render(request,'profile.html',context)

# @login_required
# def check_validity(user_id,plan_id):
#     expired=False
#     pdays=None
#     pvalidity=None
#     # user=request.user
#     # if request.user.is_authenticated:
#     user=User.objects.get(id=user_id)
#     subplan=SubPlan.objects.get(id=plan_id)
#     check_package=Subscription.objects.filter(user=user,plan=subplan).count()

#     if check_package > 0:
#         pdata=Subscription.objects.filter(user=user,plan=subplan).order_by('-id').first()
#         today=date.today()
#         pdate=pdata.reg_date
#         pdays=(today-pdate).days
#         pvalidity=pdata.plan.validity_days
#         if pdays > pvalidity:
#             expired=True
#     else:
#         expired=False

#     return expired

    # context={
    #     'username':username,
    #     'current_subplan':current_subplan,
    #     'expire_date':expire_date
    # }


