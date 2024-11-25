from django.contrib import admin
from .models import Personal, Contact, Address, Complementary_Courses, Education, Experience, Interests, Skills, Workflow, Message  # noqa E201


class PersonalAdmin(admin.ModelAdmin):
    ...


class AddressAdmin(admin.ModelAdmin):
    ...


class ContactAdmin(admin.ModelAdmin):
    ...


class Complementary_CoursesAdmin(admin.ModelAdmin):
    ...


class EducationAdmin(admin.ModelAdmin):
    ...


class ExperienceAdmin(admin.ModelAdmin):
    ...


class InterestsAdmin(admin.ModelAdmin):
    ...


class SkillsAdmin(admin.ModelAdmin):
    ...


class WorkflowAdmin(admin.ModelAdmin):
    ...


class MessageAdmin(admin.ModelAdmin):
    ...


admin.site.register(Personal, PersonalAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Complementary_Courses, Complementary_CoursesAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Interests, InterestsAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(Workflow, WorkflowAdmin)
admin.site.register(Message, MessageAdmin)
