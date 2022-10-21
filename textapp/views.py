
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
import os
from django.conf import settings
from textapp import audio_formatter 


@login_required(login_url="signin")
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

        audio_formatter.convert_mp3_into_wav()
        audio_formatter.change_pitch_and_save(100)

    return render(request, "index.html",{"audio_file":file})

