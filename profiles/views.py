from django.shortcuts import render, get_object_or_404, reverse
from django.views import View
from django.views.generic.edit import UpdateView
from .models import Profile
from .forms import ProfileForm
from videos.models import Video

class ProfileView(View):
    def get(self, request, pk):
        profile = get_object_or_404(Profile, user=request.user)
        videos = Video.objects.filter(uploader=request.user).order_by('-date_posted')

        context = {
            'profile': profile,
            'videos': videos,
        }

        return render(request, 'profiles/profile.html', context)



class UpdateProfile(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profiles/update_profile.html'

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # Assuming you have a OneToOneField relationship between User and Profile
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
