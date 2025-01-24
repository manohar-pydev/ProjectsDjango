from django.shortcuts import render
from .models import Product
from django.contrib.postgres.search import SearchVector,SearchQuery,SearchRank,TrigramSimilarity
from django.db.models import Q
from django.views.decorators.cache import cache_page
from django.core.cache import cache
# Create your views here.
@cache_page(60,1)
def index(request):
    search = request.GET.get('search')
    if search:
        #results = Products.objects.filter(title__search = search)
        query = SearchQuery("Blue Handbag") # two keywords
        vector = SearchVector('title','category','brand','sku')
        rank = SearchRank(vector,query)
        results = Products.objects.annotate(
            search = SearchVector('title','category','description')
        ).filter(search=search)#.filter(search=query) --for using search query
        # Search vector applied for 2 fields can be applied for each single field
        # SearchVector('title')+SearchVector('category') +SearchVector('description')
        # 
    else:  
        results = Product.objects.all()
    return render(request,'index.html',{'results':results})

def index2(request):
    # Implementation of Trigram similarity
    search = request.GET.get('search')
    if search:
        query = SearchQuery(search)
        vector = SearchVector(
            "title",
            "description",
            "category",
            "brand"
        )
        rank = SearchRank(vector,query)
        results = Product.objects.annotate(
            rank = rank,
            similarity = TrigramSimilarity('title',search) +\
                          TrigramSimilarity('description',search) +\
                           TrigramSimilarity('category',search) +\
                            TrigramSimilarity('brand',search)
            
        ).filter(Q(rank__gte=0.3)|Q(similarity__gte=0.3)).distinct().order_by('-rank','-similarity')
    # to get unique brands 
    if request.GET.get('min_price') and request.GET.get('max_price'):
        min_price = float(request.GET.get('min_price'))
        max_price = float(request.GET.get('max_price'))
        results = Products.objects.filter(price__gte = min_price, price__lte = max_price).order_by('price')
    # Filter for brand
    if request.GET.get('brand'):
        results = results.filter(
            brand = request.GET.get('brand')
        ).order_by('price') 
    # Filter for category
    if request.GET.get('category'):
        results = results.filter(
            category=request.GET.get('category')
        ).order_by('price')
        
    if cache.get('brands'):
        brands = cache.get("brands")    
    else:
        cache.set("brands",Product.objects.all().distinct('brand').order_by('brand'),60*10)

    #brands = Product.objects.all().distinct('brand').order_by('brand')
    if cache.get('categories'):
        cache.get("categories")
    else:
        cache.set("categories", Product.objects.all().distinct('category').order_by('category'),60*10)
        
    return render(request,'index.html',{'results':results,
                                        'brands':brands,
                                        'categories':categories,
                                        'search':request.GET.get('search')})