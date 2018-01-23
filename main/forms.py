from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from .models import Staff


class Signup(forms.Form):
    """
    This is the signup form.
    """
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
        'id_not_found': _("This ID is not available."),
        'info_not_matched': _("The information didn't match."),
        'username_exists': _("The username already exists."),
        'staff_username_exists': _("This staff already has an account please login to it."),
    }
    staff_id = forms.IntegerField(label='ID')
    first_name = forms.CharField(label=_("First Name"), max_length=50)
    middle_name = forms.CharField(label=_('Middle Name'), required=False, max_length=50)
    last_name = forms.CharField(label=_("Last Name"), max_length=50)
    contact_no = forms.CharField(label=_('Contact No'), max_length=15)
    email = forms.EmailField(label=_("Email"), max_length=50)
    username = forms.CharField(label=_("Username"), max_length=32)
    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"), widget=forms.PasswordInput,
                                help_text=_("Enter the same password as above, for verification."))

    def clean(self):
        staff_id = self.cleaned_data.get('staff_id')
        first_name = self.cleaned_data.get('first_name')
        middle_name = self.cleaned_data.get('middle_name')
        last_name = self.cleaned_data.get('last_name')
        contact_no = self.cleaned_data.get('contact_no')
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username').lower()
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        s = Staff.objects.filter(staff_id__exact=staff_id)
        u = User.objects.filter(username__iexact=username)
        if s.count():
            st = Staff.objects.get(staff_id__exact=staff_id)
            if st.user:
                raise forms.ValidationError(
                    self.error_messages['staff_username_exists'],
                    code='staff_username_exits',
                )
            elif first_name != st.first_name or middle_name != st.middle_name or last_name != st.last_name or email != st.email_address or contact_no != st.contact_no:
                raise forms.ValidationError(
                    self.error_messages['info_not_matched'],
                    code='info_not_matched',
                )
        else:
            raise forms.ValidationError(
                self.error_messages['id_not_found'],
                code='id_not_found',
            )

        if u.count():
            raise forms.ValidationError(
                self.error_messages['username_exists'],
                code='username_exists',
            )

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )

    def save(self):
        user = User.objects.create(
            username=self.cleaned_data['username'].lower(),
            password=self.cleaned_data['password1'],
            first_name=self.cleaned_data['first_name'].title(),
            last_name=self.cleaned_data['last_name'].title(),
            email=self.cleaned_data['email'].lower(),
        )
        return user
