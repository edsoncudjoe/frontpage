from flask import render_template, flash

from . import main
from .forms import ContactForm
from .emails import new_contact_mail, postmaster_email


@main.route('/', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        # subject = form.subject.data
        message = form.message.data
        try:
            new_contact_mail(name, email, message)
            postmaster_email(name, email, message)
            flash('Your message was sent successfully! I will get in contact with you very soon.')
        except Exception as contactFormError:
            print(contactFormError)
            flash('Sorry, there was a server error. If it continues please email me using the address on the left')
            return render_template('index.html', form=form)
    return render_template('index.html', form=form)
