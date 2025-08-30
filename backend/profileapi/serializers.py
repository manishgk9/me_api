from rest_framework import serializers
from .models import Profile, Project, Skill, WorkExperience
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ("username", "email", "password")

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"]
        )
        return user


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'weight']


class ProjectSerializer(serializers.ModelSerializer):
    skills = serializers.SlugRelatedField(
        many=True,
        slug_field="name",
        queryset=Skill.objects.all(),
        required=False
    )

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'link', 'skills', 'created_at']


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ['id', 'company', 'role', 'start_date', 'end_date', 'description']


class ProfileSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)
    work = WorkSerializer(many=True, read_only=True)

    # incoming list of skill names
    skills = serializers.ListField(
        child=serializers.CharField(), write_only=True, required=False
    )
    # outgoing serialized skills
    skills_display = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name",
        source="skills"
    )

    class Meta:
        model = Profile
        fields = [
            "id", "user", "full_name", "email", "education", "bio",
            "skills", "skills_display", "projects", "work",
            "github", "linkedin", "portfolio", "created_at"
        ]
        read_only_fields = ("user", "created_at")

    def create(self, validated_data):
        skills_data = validated_data.pop("skills", [])
        profile = super().create(validated_data)
        for skill_name in skills_data:
            skill, _ = Skill.objects.get_or_create(name=skill_name)
            profile.skills.add(skill)
        return profile

    def update(self, instance, validated_data):
        skills_data = validated_data.pop("skills", None)
        profile = super().update(instance, validated_data)
        if skills_data is not None:
            profile.skills.clear()
            for skill_name in skills_data:
                skill, _ = Skill.objects.get_or_create(name=skill_name)
                profile.skills.add(skill)
        return profile
