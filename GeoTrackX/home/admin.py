from django.contrib import admin
from django.urls import path
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from .models import Contact
from django.utils.html import format_html


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'timestamp', 'admin_reply', 'view_and_reply_button']

    def view_and_reply_button(self, obj):
        return format_html('<a href="/admin/home/contact/{}/view_and_reply/" class="button">View and Reply</a>', obj.id)

    view_and_reply_button.short_description = 'View and Reply'


@admin.register(Contact)
class ContactFormAdminWithActions(ContactFormAdmin):
    actions = ['send_reply']

    def send_reply(self, request, queryset):
        # Implement the logic to send replies to selected contact forms
        for form_instance in queryset:
            send_mail(
                f'Re: {form_instance.admin_reply}',
                form_instance.admin_reply,
                'your_admin_email@example.com',
                [form_instance.email],
                fail_silently=False,
            )
        self.message_user(request, f'Replies sent successfully to {queryset.count()} contact forms.')

    send_reply.short_description = 'Send Replies to Selected Contact Forms'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<path:object_id>/view_and_reply/', self.admin_site.admin_view(self.view_and_reply),
                 name='admin-view-and-reply'),
        ]
        return custom_urls + urls

    def view_and_reply(self, request, object_id, *args, **kwargs):
        form_instance = get_object_or_404(Contact, id=object_id)
        context = {
            'form_instance': form_instance,
        }
        return render(request, 'home/admin_view_template.html', context)
