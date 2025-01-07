from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project, Comment, Interest
from .forms import ProjectForm, CommentForm


@login_required
def project_list(request):
    projects = Project.objects.all().order_by('-created_at')
    form = ProjectForm()
    return render(request, 'projects/project_list.html', {'projects': projects, 'form': form})


@login_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    comments = project.comments.all()
    is_interested = project.interests.filter(user=request.user).exists()

    if request.method == 'POST':
        if 'add_comment' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.project = project
                comment.user = request.user
                comment.save()
                return redirect('project_detail', project_id=project.id)
        elif 'express_interest' in request.POST:
            Interest.objects.get_or_create(project=project, user=request.user)
            return redirect('project_detail', project_id=project.id)

    comment_form = CommentForm()
    return render(request, 'projects/project_detail.html', {
        'project': project,
        'comments': comments,
        'is_interested': is_interested,
        'comment_form': comment_form
    })

@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'projects/add_project.html', {'form': form})


