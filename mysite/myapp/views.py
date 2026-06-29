from django.shortcuts import render, redirect
from .models import Profile


def save_profile(request):
    if request.method == "POST":

        profile = Profile.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            degree=request.POST.get("degree"),
            school=request.POST.get("school"),
            university=request.POST.get("university"),
            summary=request.POST.get("summary"),
            previous_work=request.POST.get("previous_work"),
            skills=request.POST.get("skills"),
        )

        # Redirect to resume page
        return redirect("resume", id=profile.id)

    return render(request, "myapp/accept.html")


def resume(request, id):
    user_profile = Profile.objects.get(id=id)

    return render(
        request,
        "myapp/resume.html",
        {
            "user_profile": user_profile
        }
    )