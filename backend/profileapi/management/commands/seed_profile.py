from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from profileapi.models import Profile, Skill, Project, WorkExperience


class Command(BaseCommand):
    help = "Seed DB with a sample profile, projects, and skills."

    def handle(self, *args, **options):
        # Create or get user
        user, _ = User.objects.get_or_create(username="manishgk9")
        # Create or get profile
        profile, created = Profile.objects.get_or_create(
            user=user,
            defaults={
                "full_name": "Manish Yadav",
                "email": "emanish365@gmail.com",
                "education": "B.Tech in Computer Science",
                "bio": "A passionate developer who is always eager to learn new technologies.",
                "github": "https://github.com/manishgk9",
                "linkedin": "https://linkedin.com/in/manishgk9",
                "portfolio": "https://manishgk9.github.io/site/",
            },
        )

        # --- Global skills ---
        skills = [
            "python", "django", "drf", "fastapi", "reactjs", "tailwindcss",
            "flutter", "bloc", "getx", "docker", "mysql", "sqlite", "firebase",
            "redis", "celery", "rest api", "redux", "javascript", "html", "css",
            "git", "github", "java", "machine learning", "tensorflow", "nlp",
            "selenium", "beautifulsoup", "spacy", "requests", "hive"
        ]
        for s in skills:
            skill, _ = Skill.objects.get_or_create(name=s)
            profile.skills.add(skill)

        # --- Projects with related skills ---
        projects = [
            {
                "title": "Internshala Auto Job Applier",
                "description": "Automates internship/job applications on Internshala with Selenium, Celery, Redis, FastAPI, AI integration for assignments, and smart bulk apply.",
                "link": "https://github.com/manishgk9/internshala-auto-job-applier",
                "skills": ["python", "django", "fastapi", "celery", "redis", "selenium", "beautifulsoup", "reactjs"]
            },
            {
                "title": "Twitter Sentiment Miner",
                "description": "Sentiment analysis tool using Logistic Regression, TF-IDF, NLP preprocessing. Achieved 87% accuracy on real-world tweets.",
                "link": "https://github.com/manishgk9/twiiter_openion_miner",
                "skills": ["python", "django", "drf", "nlp", "reactjs", "tailwindcss"]
            },
            {
                "title": "LinkedIn & PDF Resume Analyzer",
                "description": "ATS resume analyzer + LinkedIn scraper using FastAPI, NLP, Spacy, Selenium, Gemini. Suggests keywords to improve recruiter selection rates.",
                "link": "https://github.com/manishgk9/linkedLensAnalyzer",
                "skills": ["fastapi", "nlp", "spacy", "selenium", "beautifulsoup", "reactjs"]
            },
            {
                "title": "Brain Tumor Detection API",
                "description": "CNN-based model with 90%+ accuracy for MRI scan classification, exposed via FastAPI with React frontend.",
                "link": "https://github.com/manishgk9/brain_tumer_detection_system",
                "skills": ["tensorflow", "cnn", "fastapi", "reactjs"]
            },
            {
                "title": "AI Email Generator & Sender",
                "description": "Automates professional email writing using Gemini API. Includes secure sending pipeline with tracking features.",
                "link": "https://github.com/manishgk9/ai_email_sender_2",
                "skills": ["fastapi", "gemini", "smtp", "reactjs", "tailwindcss"]
            },
            {
                "title": "Gemini Chatbot App",
                "description": "Flutter app using Gemini API + Bloc state management with real-time conversational responses. Hive for storage.",
                "link": "https://github.com/manishgk9/chatbotgimini",
                "skills": ["flutter", "bloc", "hive", "gemini"]
            },
            {
                "title": "Awesome VPN App",
                "description": "Flutter VPN app with OpenVPN, Hive, GetX. Features server selection, ping indicators, and optimized UI.",
                "link": "https://github.com/manishgk9/flutter-owsomevpn",
                "skills": ["flutter", "getx", "hive", "openvpn"]
            },
            {
                "title": "Telegram Bot (Work Automation)",
                "description": "Built with Django + Telebot. Automates login, daily updates, task management, stats, and leave tracking.",
                "link": "https://github.com/manishgk9/persist_automation_bot",
                "skills": ["django", "drf", "telebot", "sqlite"]
            },
            {
                "title": "Suno.com Song Generation Automation",
                "description": "Automates song generation on Suno.com with Selenium + Requests, bypasses hCaptcha using cookies & sessions.",
                "link": "https://github.com/manishgk9/suno_song_generation_automation_without_captcha",
                "skills": ["python", "selenium", "requests"]
            },
        ]

        for proj in projects:
            project, created = Project.objects.get_or_create(
                profile=profile,
                title=proj["title"],
                defaults={
                    "description": proj["description"],
                    "link": proj["link"],
                },
            )
            if not created:
                # Update description & link if they changed
                project.description = proj["description"]
                project.link = proj["link"]
                project.save()

            # Add related skills
            for skill_name in proj["skills"]:
                skill, _ = Skill.objects.get_or_create(name=skill_name)
                project.skills.add(skill)

        # WorkExperience.objects.get_or_create(
        #     profile=profile,
        #     company="ABC Corp",
        #     role="Software Engineer",
        #     start_date="2022-01-01",
        #     end_date=None,
        #     description="Worked on backend services."
        # )

        self.stdout.write(self.style.SUCCESS("Seeded profile, skills, and projects with project-wise skills"))
