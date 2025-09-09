from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406424814',
        'name': 'Nuril Izza Ahmady',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)