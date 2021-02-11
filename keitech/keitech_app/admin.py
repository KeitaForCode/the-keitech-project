from django.contrib import admin
from keitech_app.models import NewsLetter, Contacts, SignUp, Question, Answer, Comments, UpVote, DownVote

admin.site.register(NewsLetter)
admin.site.register(Contacts)
admin.site.register(SignUp)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Comments)
admin.site.register(UpVote)
admin.site.register(DownVote)
