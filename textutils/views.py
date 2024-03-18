from django.shortcuts import render


# Create your views here.
def textutils(request):
    return render(request, 'Text_Utility.html')


def result_text(request):
    text = request.POST.get('message', 'default')  # request.GET.get('message', 'default') for get request
    punc = request.POST.get('punc', 'off')  # this is for post request
    caps = request.POST.get('caps', 'off')
    lower_caps = request.POST.get('cap_low', 'off')
    extra = request.POST.get('ex_space', 'off')
    newline = request.POST.get('new', 'off')
    punctuations = '''.,?!:;"'()[]{}-—.../&*#$%^@+=<>|~`'''
    analyzed = ''
    purpose = ""
    if punc == "on":
        purpose = purpose + "\npunctuation removed"
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char
    else:
        analyzed = text
    if caps == "on":
        purpose = purpose + "\nfull caps"
        blank = ""
        for char in analyzed:
            blank = blank + char.upper()
        analyzed = blank
    if lower_caps == "on":
        purpose = purpose + "\nlower caps"
        blank = ""
        for char in analyzed:
            blank = blank + char.lower()
        analyzed = blank
    if extra == "on":
        purpose = purpose + "\nextra space removed"
        blank = ""
        while analyzed and analyzed[-1] == " ":
            analyzed = analyzed[:-1]
        for index, char in enumerate(analyzed):
            if not (analyzed[index] == " " and analyzed[index + 1] == " "):
                blank += char
        analyzed = blank
    if newline == "on":
        purpose += "\nnewline removed"
        blank = ""
        for char in analyzed:
            if char != "\n" and char != "\r":
                blank = blank + char
        analyzed = blank
    char_count = len(analyzed)
    params = {"char": char_count, "pur": purpose, "text": analyzed}
    return render(request, 'resultant.html', params)
