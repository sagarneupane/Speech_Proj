from curses.ascii import HT
from django.shortcuts import render, HttpResponse
from django.http import FileResponse
import os
from django.conf import settings


def index(request):

    if request.method == 'POST':

        import gtts
        language = 'en'
        sub = 'co.in'
        data = request.POST.get("text_to_speak")
        myobj = gtts.gTTS(text=data, lang=language,tld=sub ,slow=False)
        myobj.save("yourtext.mp3")

        file = open(os.path.join(settings.BASE_DIR, "yourtext.mp3"), 'rb')

        return HttpResponse(file, content_type="audio/mpeg") 


    return render(request, "index.html")