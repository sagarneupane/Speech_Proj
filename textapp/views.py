
from django.shortcuts import render, HttpResponse
from django.http import FileResponse
import os
from django.conf import settings


def index(request):
    file = None
    if request.method == 'POST':

        import gtts
        language = 'en'
        sub = 'co.in'
        data = request.POST.get("text_to_speak")
        myobj = gtts.gTTS(text=data, lang=language,tld=sub ,slow=False)
        file = myobj.save("media/yourtext.mp3")

        file = open(os.path.join(settings.BASE_DIR, "media/yourtext.mp3"), 'rb')

        # return FileResponse(file, as_attachment=True) 

    return render(request, "index.html",{"audio_file":file})


