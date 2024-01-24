from django.http import HttpResponse
from django.template import loader

from .services.minigame import play_minigame

from .models import Member


def home(request):
   template = loader.get_template('home.html')
   return HttpResponse(template.render())

def minigame(request):
   start_purse = 1000
   purse = start_purse

   if request.method == 'POST':
      bet = int(request.POST.get('bet'))
      marble, result, purse, game_over = play_minigame(bet, purse, start_purse)

      context = {
         'purse': purse,
         'marble': marble,
         'result': result,
         'game_over': game_over,
      }
      template = loader.get_template('minigame.html')
      return HttpResponse(template.render(context, request))
   else:
      template = loader.get_template('minigame.html')
      context = {'start_purse': start_purse}
      return HttpResponse(template.render(context, request))

def users(request):
   mymembers = Member.objects.all().values()
   template = loader.get_template('all_users.html')
   context = {
     'mymembers': mymembers,
   }
   return HttpResponse(template.render(context, request))

def details(request, slug):
   mymember = Member.objects.get(slug=slug)
   template = loader.get_template('details.html')
   context = {
      'mymember': mymember
   }
   return HttpResponse(template.render(context, request))


def testing(request):
   mymembers = Member.objects.all().values()
   template = loader.get_template('template.html')
   context = {
      'mymembers': mymembers,
   }
   return HttpResponse(template.render(context, request))