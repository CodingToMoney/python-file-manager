
# app/views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, FileResponse
from .models import UploadedFile

def file_list(request):
    if request.method == 'POST' and 'file' in request.FILES:
        uploaded_file = request.FILES['file']
        if UploadedFile.objects.filter(file='uploads/' + uploaded_file.name).exists():
            return JsonResponse({'error': 'File with this name already exists.'})

        mime_type = uploaded_file.content_type
        new_file = UploadedFile(file=uploaded_file, mime_type=mime_type)
        new_file.save()

        return JsonResponse({'file': {'id': new_file.id, 'name': new_file.file.name}})

    files = UploadedFile.objects.all()
    return render(request, 'index.html', {'files': files})

def delete_file(request, file_id):
    try:
        file = UploadedFile.objects.get(id=file_id)
        file.file.delete()  # 删除文件
        file.delete()       # 删除数据库记录
        return redirect('file_list')
    except UploadedFile.DoesNotExist:
        return HttpResponse("File not found.", status=404)

def download_file(request, file_id):
    try:
        file = UploadedFile.objects.get(id=file_id)
        response = FileResponse(file.file)
        return response
    except UploadedFile.DoesNotExist:
        return HttpResponse("File not found.", status=404)
