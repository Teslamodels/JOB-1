from django.forms.models import BaseModelForm
from django.http import HttpResponse
from .models import Article
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

class AHome(ListView):
    model = Article
    template_name = 'ahome.html'


class ADetail(DetailView):
    model = Article
    template_name = 'adetail.html'


class AUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = 'aupdate.html'
    fields = ['title', 'summary', 'body', 'photo']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ADelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'adelete.html'
    success_url = reverse_lazy('article')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ACreate(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'acreate.html'
    fields = ['title', 'summary', 'body', 'photo']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)