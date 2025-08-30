from django.contrib import admin
from .models import Profile, Skill, Project, WorkExperience


# Inline to manage Projects directly from Profile admin
class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1


# Inline to manage WorkExperience directly from Profile admin
class WorkExperienceInline(admin.TabularInline):
    model = WorkExperience
    extra = 1


# Inline for Profile Skill Many-to-Many relation
class SkillInline(admin.TabularInline):
    model = Profile.skills.through
    extra = 1


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "user", "created_at")
    search_fields = ("full_name", "email", "education", "bio", "user__username")
    list_filter = ("created_at",)
    inlines = [SkillInline, ProjectInline, WorkExperienceInline]
    readonly_fields = ("created_at",)
    exclude = ("skills",)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "weight")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "profile", "created_at")
    search_fields = ("title", "description", "skills__name")
    list_filter = ("created_at", "skills")
    filter_horizontal = ("skills",)
    readonly_fields = ("created_at",)


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ("company", "role", "profile", "start_date", "end_date")
    search_fields = ("company", "role", "description")
    list_filter = ("start_date", "end_date")
