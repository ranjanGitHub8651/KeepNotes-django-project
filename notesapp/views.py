from datetime import date
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import KeepNote

def BasePage(request):
    return render(request, 'base.html')

def Index(request):
    notes = KeepNote.objects.all()
    return render(request, 'index.html', {'notes':notes})

def AddNewNotes(request):
    note_created_on = timezone.now()
    if (request.method=="POST"):
        add = KeepNote()
        add.title = request.POST.get('title')
        add.notes = request.POST.get('note')
        add.created_on = note_created_on
        add.save()
        return HttpResponseRedirect('../home')

    return render(request, 'newnotes.html')

def UpdateNote(request, id):
    update = KeepNote.objects.get(id=id)
    if request.method=="POST":
        update.title = request.POST.get('title')
        update.notes = request.POST.get('note')
        update.save()
        return HttpResponseRedirect('../home')
    return render(request, "editnote.html", {"update":update})

def DeleteNote(request, id):
    noteDelete = KeepNote.objects.get(id=id)
    print(noteDelete, "\n\n\n\n")
    try:
        print("DDDDDDDDD \n\n\n\n\n")
        if noteDelete:
            print("DDDDDDDDD \n\n\n\n\n")
            noteDelete.delete()
            print("PRPRPRPPRPRPR \n\n\n\n")
            return HttpResponseRedirect('../home')
    except:
        raise ValueError(f"{id} Dosen't exist.")