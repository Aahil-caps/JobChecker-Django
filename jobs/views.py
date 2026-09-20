from django.shortcuts import render


def home(request):

    name = request.GET.get('name', '')
    age = int(request.GET.get('age', 0))
    experience = int(request.GET.get('experience', 0))
    python_skill = request.GET.get('python_skill', '')

    submitted = 'name' in request.GET


    context = {
        'name': name,
        'age': age,
        'experience': experience,
        'python_skill': python_skill,
        "submitted":submitted,
    }

    return render(request, 'base.html', context)