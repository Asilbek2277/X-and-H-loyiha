from django.shortcuts import render

from .models import *

def index(request):

    search=request.GET.get('search')

    togri_sozlar=Togri_soz.objects.filter(soz=search)

    if togri_sozlar and search:
        togri_soz=togri_sozlar[0]
        notogri_sozlar=Notogri_soz.objects.filter(t_soz=togri_soz)

        context={
            'togri_soz': togri_soz,
            'notogri_sozlar':notogri_sozlar
        }
        return render(request, 'index.html', context)
    elif search:
        notogriSoz=Notogri_soz.objects.filter(soz=search).first()
        if notogriSoz:
            togri_soz=Togri_soz.objects.get(id=notogriSoz.t_soz.id)
            notogriSozlar=Notogri_soz.objects.filter(t_soz=togri_soz)

            context={
                'togri_soz': togri_soz,
                'notogri_sozlar': notogriSozlar
            }
            return render(request, 'index.html', context)
        n=Notogri_soz.objects.all()
        for i in n:
            if i!=search:
                context = {
                    'togri_soz': Togri_soz.objects.filter(soz='Mavjud emas')[0],
                    'notogri_sozlar': Notogri_soz.objects.filter(soz='Mavjud emas')
                }
                return render(request, 'index.html', context)

    elif search=='':
        context = {
            'togri_soz': Togri_soz.objects.filter(soz='Malumot kiriting')[0],
            'notogri_sozlar': Notogri_soz.objects.filter(soz='Malumot kiriting')
        }
        return render(request, 'index.html', context)


    return render(request, 'index.html')


