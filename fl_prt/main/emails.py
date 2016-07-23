from flask import render_template

from .. import mail

from flask_mail import Message


def welcome_email(subject, sender, recipient, txt_body, html_body):
    welcome = Message(subject, sender=sender, recipients=recipient)
    welcome.body = txt_body
    welcome.html = html_body
    mail.send(welcome)


def new_contact_mail(name, contact_email, message):
    welcome_email('Edson Cudjoe - Message received confirmation',
                  sender='mail@edsoncudjoe.com',
                  recipient=[contact_email],
                  txt_body=render_template('contact_reply',
                                           user=name,
                                           addr=contact_email,
                                           msg=message),
                  html_body=render_template('contact_reply.html',
                                            user=name,
                                            addr=contact_email,
                                            msg=message))


def postmaster_email(name, email, message):
    welcome_email('You have a new message from EdsonCudjoe.com',
                  sender='mail@edsoncudjoe.com',
                  recipient=['e.cudjoe@hotmail.co.uk'],
                  txt_body=render_template('postmaster_notify',
                                           user=name,
                                           addr=mail,
                                           msg=message),
                  html_body=render_template('postmaster_notify.html',
                                            user=name,
                                            addr=email,
                                            msg=message))


def send_emails(name, email, message):
    new_contact_mail(name, email, message)
    postmaster_email(name, email, message)
