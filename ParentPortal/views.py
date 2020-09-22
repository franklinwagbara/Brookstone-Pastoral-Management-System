from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from smtplib import SMTPException
from django.urls import reverse
from django.contrib import messages
from StudentManager.models import Students
from Dashboard.models import PrincipalInbox
from StudentManager.functions import FilterStudents
from StudentManager.forms import FilterStudentsForm
from .forms import ParentForm
import concurrent.futures
import threading
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def parentForm(request, pk):
    print("In ParentForm")
    #html_message = render_to_string('dashboard/mail_template.html', {'context': request.build_absolute_uri(reverse('dashboard-parentForm', args=(pk, )))})
    #plain_message = strip_tags(html_message)
    #send_mail('Hello Dear',
     #         plain_message,
     #         'wagbarafranklin@yahoo.com',
     #         ['franklinwagbara@gmail.com', 'wagbarafranklin@yahoo.com'],
     #         html_message=html_message,
     #         fail_silently=False)
    student = Students.objects.get(id=pk)
    student_name = student.LastName + ", " + student.FirstName + " " + student.MiddleName
    print(student_name)
    if request.method == 'POST':
        form = ParentForm(request.POST or None, request.FILES or None, initial={'StudentName': student_name}, instance=student)
        if form.is_valid():
            alternative = str(form.cleaned_data['Alternative'])
            form.save()
            if alternative == "True":
                if PrincipalInbox.objects.filter(student=student).exists() != True:
                    PrincipalInbox.objects.create(student=student, viewed="No", approved="No")
                    PrincipalInbox.save
                else:
                    PrincipalInbox.objects.update(student=student, viewed="No", approved="No")
                    PrincipalInbox.save
            messages.success(request, f'Saved successfully!')
            return redirect('ParentPortal-parentForm', pk)
    else:
        form = ParentForm(initial={'StudentName': student_name}, instance=student)
    return render(request, 'parentForm.html',
                  {'form': form})

def sendMail(request, student):
    msg=""
    if str(student.ParentEmail) != "None":
        html_message = render_to_string('mail_template.html', {
            'context': request.build_absolute_uri(reverse('ParentPortal-parentForm', args=(student.pk,)))})
        plain_message = strip_tags(html_message)
        try:
            send_mail('Brookstone School Ward Check-in Form',
                      plain_message,
                      'wagbarafranklin@yahoo.com',
                      [str('wagbarafranklin@yahoo.com')],
                      html_message=html_message,
                      fail_silently=False)
            msg = "Email sent Successfully!"
            messages.success(request, msg)
        except SMTPException:
            msg = "E-mail failed!"
            messages.error(request, SMTPException)
    else:
        msg = "No Email address specified."
        messages.error(request, msg)
    return msg

@login_required(login_url='login')
def EmailParentForms(request, student):
    # message="Email failed!"
    # with concurrent.futures.ThreadPoolExecutor() as executor:
    #     results = [executor.submit(sendMail, request, st) for st in student]
    #
    #     for f in concurrent.futures.as_completed(results):
    #         if f.result() != "EmailNoneResult":
    #             message = f.result()
    #         return message

    i = 0
    message = []
    for s in student:
        th = threading.Thread(target=sendMail, args=[request, s])
        message.append(th.start())
        i += 1
        print(i)

    for a in range(i):
        print(message)

    return message

@login_required(login_url='login')
def homepage(request):
    if request.method == 'POST':
        form = FilterStudentsForm(request.POST)
        if form.is_valid():
            students = FilterStudents(form)
            if "send" in request.POST:
                message = EmailParentForms(request, students)
                return render(request, 'FeedBack.html', {'message': message})
            else:
                return render(request, 'sendParentForm.html',
                              {'students': students.order_by('LastName'), 'form': form})
    else:
        form = FilterStudentsForm()

    if "send" in request.POST:
        message = EmailParentForms(request, Students.objects.all().filter())
        return render(request, 'FeedBack.html', {'message': message})
    else:
        return render(request, 'sendParentForm.html',
                  {'students': Students.objects.all().filter().order_by('LastName'), 'form': form})