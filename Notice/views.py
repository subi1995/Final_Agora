from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import ListView
from .models import Agora
from .forms import AgoraForm



class homeLV(ListView):
    model = Agora
    template_name = 'bsr/home.html'
    paginate_by = 5
    
	def get_queryset(self):
		qs = Agora.objects.all()
		q = self.request.GET.get('q', '') # GET request의 get 인자중에 q 가 있으면 가져오고, 없으면 빈 문자열

		if q:
			qs = qs.filter(title__icontains=q)

		return qs

####AGORA

class agoraLV(ListView):
	model = Agora
	template_name = 'bsr/agora_list.html'
	context_object_name = 'agoras'
	paginate_by = 10

	def get_queryset(self):
		qs = Agora.objects.all()
		q = self.request.GET.get('q', '') # GET request의 get 인자중에 q 가 있으면 가져오고, 없으면 빈 문자열

		if q:
			qs = qs.filter(title__icontains=q)

		return qs

def agora_detail(request, pk_2):
    agora = get_object_or_404(Agora, pk=pk_2)
    if request.method == "POST":
        if request.user.is_anonymous():
            return redirect('login')

        return render(request, 'bsr/agora_detail.html', {'agora':agora, 'form':form})

@login_required
def agora_new(request):
    if request.method == "POST":
            form = AgoraForm(request.POST, request.FILES)
            if form.is_valid():
                    agora = form.save(commit=False)
                    agora.author = request.user
                    agora.save()
                    return redirect(agora)
    else:
            form = AgoraForm()
    return render(request, 'bsr/agora_new.html', {'form': form})


@login_required
def agora_edit(request, pk_2):
    agora = get_object_or_404(Agora, pk=pk_2)
    if request.method == 'POST':
            form = AgoraForm(request.POST, request.FILES, instance=agora)
            if form.is_valid():
                    agora = form.save()
                    return redirect(agora)

    else:
            if agora.author == request.user:
                    form = AgoraForm(instance=agora)
                    return render(request, 'bsr/agora_edit.html', {'form':form})
            else:
                    return render(request, 'bsr/warning.html')


@login_required
def agora_remove(request, pk_2):
    agora = get_object_or_404(Agora, pk=pk_2)
    if agora.author == request.user:
        agora.delete()
        return redirect('study:agora_list')
    else:
        return render(request, 'bsr/warning.html')
	    
