from .models import Articles
import random


not_required = []
def less_recommended_articles(request,pk,messages):
    '''
    Filter less recommended articles from the user who is logged in
    '''
    get_category = Articles.objects.get(id=pk).category
    articles_not_required = Articles.objects.filter(category=get_category)
    for article in articles_not_required:
        not_required.append(article.id)

    articles_required = Articles.objects.exclude(id__in=not_required)

    # print(' Articles ids not required are ',not_required)
    # order by ids which are not required at the end of the list > [i.id for i in articles_required] + not_required
    
    all_articles = Articles.objects.filter\
    (id__in = [i.id for i in articles_required] \
    + random.sample(not_required, 1) ).order_by('-category')

    messages.success(request, f'We have Got your response, \
        we will do the redundancy\
        for these articles ')
    return all_articles