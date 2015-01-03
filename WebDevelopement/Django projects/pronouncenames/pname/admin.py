from django.contrib import admin
from pname.models import Word,Phoneme,RequestWord,WordKey
# Register your models here.

admin.site.register(Word)
admin.site.register(Phoneme)
admin.site.register(RequestWord)
admin.site.register(WordKey)
