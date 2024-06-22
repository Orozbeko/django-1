from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest

class AgeExperienceMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.path == '/register':
            age = int(request.POST.get('experience'))
            if age < 1:
                return HttpResponseBadRequest('Ваш опыт работы слишком мал')
            elif age >=2 and age <=3:
                request.experience = 'Junior'
            elif age >= 3 and age <= 5:
                request.experience = 'Middle'
            else:
                return HttpResponseBadRequest('Senior')
        elif request.path == '/register/' and request.method == 'GET':
            setattr(request, 'experience', 'Опыт работы не определен')




