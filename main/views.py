from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from .models import (
		UserProfile,
		Blog,
		Portfolio,
		Testimonial,
		Certificate,
		Skill,
        Experience,
        Service,
        Social
	)

from django.views import generic
from . forms import ContactForm


class IndexView(generic.TemplateView):
    template_name = "main/index.html"
    pattern_name = 'home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Assuming only one user profile is expected
        context["testimonials"] = Testimonial.objects.filter(is_active=True)
        context["certificates"] = Certificate.objects.filter(is_active=True)
        context["blogs"] = Blog.objects.filter(is_active=True)
        context["portfolios"] = Portfolio.objects.filter(is_active=True)
        context["experience"] = Experience.objects.all()
        context["skills"] = Skill.objects.all()
        context['user_profile'] =  UserProfile.objects.filter(user__is_active=True)

        return context
class ContactView(generic.FormView):
    template_name = "main/contact.html"
    success_url = "/"  # Corrected attribute name
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['socials'] = Social.objects.all()
        return context

    def form_valid(self, form):
        subject = 'Message from my site'
        sender_email = form.cleaned_data["email"]
        message = f'from:  {sender_email} ,\n{form.cleaned_data["message"]}'
        sender_name = form.cleaned_data['name']
        recipients = ["ahmed01223330@gmail.com"]
        
        send_mail(
            subject,
            message,
            sender_email,  # Use the user's email as the "from" address
            recipients,
            fail_silently=False,    
        )

        context = {'message': f'Thank you, {sender_name}. We will be in touch soon.'}
        return self.render_to_response(context)



class PortfolioView(generic.ListView):
    model = Portfolio
    template_name = "main/work-listing.html"
    context_object_name = "portfolios"  # Change this line
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name = "main/work-single.html"
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        context['testimonials'] = Testimonial.objects.all()

        return context

class AboutView(generic.ListView):
    model = UserProfile
    template_name = "main/about.html"
    pattern_name = 'about'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['socials'] = Social.objects.all()
        context['skills'] = Skill.objects.all()
        context['experience'] = Experience.objects.all()

        return context

class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "main/work-single.html"
	pattern_name = 'work-single'
