from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic import ListView
from .models import Reservation
from .forms import ReservationForm

# Create your views here.

## Reservation

class reservationLV(ListView):
	model = Reservation
	template_name = 'reservation/reservation_list.html'
	context_object_name = 'reservations'
	paginate_by = 10

	def get_queryset(self):
		qs = Reservation.objects.all()
		q = self.request.GET.get('q', '') # GET request의 get 인자중에 q 가 있으면 가져오고, 없으면 빈 문자열

		if q:
			qs = qs.filter(name__icontains=q)

		return qs

##def Room_Reservation (request):
##    reservations = Reservation.objects.all()
##    return render (request, 'reservation/reservation_list.html',{'reservations': reservations})

def reservation_detail(request, pk_2):
    reservation = get_object_or_404(Reservation, pk=pk_2)
    return render(request, 'reservation/reservation_detail.html', {'reservation': reservation})

@login_required
def reservation_new(request):
    print(request.method, '1')
    if request.method == "POST":
        print(request.method, '2')
        form = ReservationForm(request.POST)
        print(form, '4156')
        if form.is_valid():
            print(request.method, '3')
            reservation = form.save(commit=False)
            reservation.author = request.user
            reservation.updated_date = timezone.now()
            reservation.save()
            return redirect('reservation_detail', pk_2=reservation.pk)
    else:
        print(request.method, '4')
        form = ReservationForm()
    return render(request, 'reservation/reservation_edit.html', {'form': form})

@login_required
def reservation_remove(request, pk_2):
    reservation = get_object_or_404(Reservation,pk = pk_2)
    reservation.delete()
    return redirect('reservation/resrervation_list.html')

@login_required
def reservation_edit(request,pk_2):
    reservation = get_object_or_404(Reservation, pk=pk_2)    
    if request.method == "POST":
        form = ReservationForm(instance=reservation)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.author = request.user
            reservation.updated_date = timezone.now()
            reservation.save()
            return redirect('reservation_detail', pk_2=reservation.pk)
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'reservation/reservation_edit.html', {'form': form})

