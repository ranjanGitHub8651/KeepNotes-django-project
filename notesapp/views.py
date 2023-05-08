from datetime import date

from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.utils import timezone

from .models import KeepNote


def BasePage(request):
    return render(request, 'base.html')

def Index(request):
    notes = KeepNote.objects.all()
    # Showing all notes per page > 3
    paginator = Paginator(notes, 6)
    page_number = request.GET.get('page')
    notes = paginator.get_page(page_number)
    if(request.method=='GET'):
        noteTitle = request.GET.get('searchtitle')
        if noteTitle:
            notes = KeepNote.objects.filter(title__icontains=noteTitle)
    data = {'notes':notes}
    return render(request, 'index.html', data)

def AddNewNotes(request):
    note_created_on = timezone.now()
    if (request.method=="POST"):
        add = KeepNote()
        add.title = request.POST.get('title')
        add.notes = request.POST.get('note')
        add.created_on = note_created_on
        add.save()
        return redirect('/home')

    return render(request, 'newnotes.html')

def UpdateNote(request, id):
    update = KeepNote.objects.get(id=id)
    if request.method=="POST":
        update.title = request.POST.get('title')
        update.notes = request.POST.get('note')
        update.save()
        return redirect('/home')
    return render(request, "editnote.html", {"update":update})

def DeleteNote(request, id):
    noteDelete = KeepNote.objects.get(id=id)
    try:
        if noteDelete:
            noteDelete.delete()
            return redirect('/home')
    except:
        raise ValueError(f"{id} Dosen't exist.")
