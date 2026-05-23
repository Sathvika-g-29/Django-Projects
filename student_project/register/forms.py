from django import forms
from datetime import date

class StudentRegistrationForm(forms.Form):
    full_name = forms.CharField(min_length=3, max_length=100)
    email = forms.EmailField()
    mobile = forms.CharField(min_length=10, max_length=10)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    gender = forms.ChoiceField(
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
        widget=forms.RadioSelect
    )

    department = forms.ChoiceField(
        choices=[('IT', 'IT'), ('CSE', 'CSE'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('MECH', 'MECH')]
    )

    year_of_study = forms.ChoiceField(
        choices=[('1', '1st Year'), ('2', '2nd Year'),
                 ('3', '3rd Year'), ('4', '4th Year')]
    )

    roll_number = forms.CharField(max_length=20)

    address = forms.CharField(widget=forms.Textarea)

    state = forms.ChoiceField(
        choices=[
            ('AP', 'Andhra Pradesh'),
            ('TS', 'Telangana'),
            ('KA', 'Karnataka'),
            ('TN', 'Tamil Nadu')
        ]
    )

    pincode = forms.CharField(min_length=6, max_length=6)

    technical_skills = forms.MultipleChoiceField(
        choices=[
            ('Python', 'Python'),
            ('Java', 'Java'),
            ('C', 'C'),
            ('Web', 'Web Development')
        ],
        widget=forms.CheckboxSelectMultiple
    )

    learning_mode = forms.ChoiceField(
        choices=[
            ('online', 'Online'),
            ('offline', 'Offline'),
            ('hybrid', 'Hybrid')
        ],
        widget=forms.RadioSelect
    )

    resume = forms.FileField()

    about = forms.CharField(widget=forms.Textarea)

    agree = forms.BooleanField()

    # ---------- VALIDATION ----------
    def clean_dob(self):
        dob = self.cleaned_data['dob']
        if dob > date.today():
            raise forms.ValidationError("DOB cannot be a future date")
        return dob
