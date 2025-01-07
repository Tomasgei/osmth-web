from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import SharedDocument
from .forms import SharedDocumentForm

def is_admin(user):
    return user.is_staff

@login_required
def shared_documents_list(request):
    general_documents = SharedDocument.objects.filter(document_type='general')
    meeting_documents = SharedDocument.objects.filter(document_type='meeting')
    return render(request, 'intranet/shared_documents_list.html', {
        'general_documents': general_documents,
        'meeting_documents': meeting_documents,
    })

@login_required
@user_passes_test(is_admin)
def upload_shared_document(request):
    if request.method == 'POST':
        form = SharedDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shared_documents_list')
    else:
        form = SharedDocumentForm()
    return render(request, 'intranet/upload_shared_document.html', {'form': form})
