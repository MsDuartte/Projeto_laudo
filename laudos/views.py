from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LaudoForm, LaudoTemplateForm
from .models import LaudoTemplate, Laudo

class HomeView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Laudo
    form_class = LaudoForm
    template_name = 'home.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['templates'] = LaudoTemplate.objects.filter(user=self.request.user)
        return context

class AddTemplateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = LaudoTemplate
    form_class = LaudoTemplateForm
    template_name = 'add_template.html'

    def form_valid(self, form):
        form.instance.user = self.request.user  

        if LaudoTemplate.objects.filter(name=form.instance.name, user=self.request.user).exists():
            messages.error(self.request, "Já existe um template com esse nome para você.")
            return redirect('add_template')  

        self.object = form.save()  # Salva o template
        messages.success(self.request, "Template salvo com sucesso.")  # Mensagem de sucesso
        return redirect('add_template')  # Mantém na mesma página

    def form_invalid(self, form):
        messages.error(self.request, "Ocorreu um erro ao salvar o template. Verifique os dados.")
        return self.render_to_response(self.get_context_data(form=form))

class TemplateListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = LaudoTemplate
    template_name = 'template_list.html'
    context_object_name = 'templates'

    def get_queryset(self):
        return LaudoTemplate.objects.filter(user=self.request.user)

class LaudoListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Laudo
    template_name = 'laudo_list.html'
    context_object_name = 'laudos'

    def get_queryset(self):
        return Laudo.objects.filter(user=self.request.user)

class LaudoDetailView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = Laudo
    template_name = 'laudo_detail.html'
    context_object_name = 'laudo'

    def get_queryset(self):
        return Laudo.objects.filter(user=self.request.user)

class LaudoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Laudo
    form_class = LaudoForm
    template_name = 'laudo_update.html'
    success_url = reverse_lazy('laudo_list')

    def get_queryset(self):
        return Laudo.objects.filter(user=self.request.user)

class LaudoDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = Laudo
    template_name = 'laudo_confirm_delete.html'
    success_url = reverse_lazy('laudo_list')

    def get_queryset(self):
        return Laudo.objects.filter(user=self.request.user)
    

class TemplateDetailView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = LaudoTemplate
    template_name = 'template_detail.html'
    context_object_name = 'template'

    def get_queryset(self):
        return LaudoTemplate.objects.filter(user=self.request.user)
    
class TemplateUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = LaudoTemplate
    form_class = LaudoTemplateForm
    template_name = 'template_update.html'
    success_url = reverse_lazy('template_list')
    context_object_name = 'template'

    def form_valid(self, form):
        form.instance.user = self.request.user  

        if LaudoTemplate.objects.filter(name=form.instance.name, user=self.request.user).exclude(pk=self.object.pk).exists():
            messages.error(self.request, "Já existe um template com esse nome para você.")
            return redirect('template_edit', pk=self.object.pk)  

        self.object = form.save()  # Salva o template
        messages.success(self.request, "Template atualizado com sucesso.")  # Mensagem de sucesso
        return redirect('template_edit', pk=self.object.pk)  # Mantem na mesma página

    def form_invalid(self, form):
        messages.error(self.request, "Ocorreu um erro ao atualizar o template. Verifique os dados.")
        return self.render_to_response(self.get_context_data(form=form))

    def get_queryset(self):
        return LaudoTemplate.objects.filter(user=self.request.user)
    
class TemplateDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = LaudoTemplate
    template_name = 'template_confirm_delete.html'
    success_url = reverse_lazy('template_list')

    def get_queryset(self):
        return LaudoTemplate.objects.filter(user=self.request.user)
    
