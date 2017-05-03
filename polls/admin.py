from django.contrib import admin

# Register your models here.
from .models import Question,Choice

##admin.site.register(Question) # FOR DEFAULT FORM ON ADMIN 


# FOR CUSTOMIZING THE ADMIN FORM

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3



class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    fieldsets = [
        (None, {'fields' : ['question_text']}),
        ('Data Information' ,{'fields':['pub_date'], 'classes':['collapse']})
        ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question,QuestionAdmin)

