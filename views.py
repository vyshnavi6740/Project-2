from django.shortcuts import render
from django.contrib import messages
from user.models import Usermodel, Accuracymodel
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import urllib, base64
from django.db.models import Count

def index(request):
    return render(request, "index.html")

def Home(request):
    return index(request)

def adminlogin(request):
    return render(request, "admin/adminlogin.html")

def adminloginaction(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        passwd = request.POST['upasswd']
        if uname == 'admin' and passwd == 'admin':
            data = Usermodel.objects.all()
            return render(request, "admin/adminhome.html", {'data': data})
        else:
            messages.success(request, 'Incorrect Details')
            return render(request, "admin/adminlogin.html")
    return render(request, "admin/adminlogin.html")

def showusers(request):
    data = Usermodel.objects.all()
    return render(request, "admin/adminhome.html", {'data': data})

def AdminActiveUsers(request):
    if request.method == 'GET':
        id = request.GET.get('uid')
        status = 'activated'
        print("PID = ", id, status)
        Usermodel.objects.filter(id=id).update(status=status)
        data = Usermodel.objects.all()
        return render(request, "admin/adminhome.html", {'data': data})

def logout(request):
    return render(request, "admin/adminlogin.html")


def populate_data(request):
    gender_counts = Usermodel.objects.values('gender').annotate(count=Count('gender'))
    genders = [item['gender'] for item in gender_counts]
    counts = [item['count'] for item in gender_counts]

    plt.bar(genders, counts)
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.title('Gender Distribution')

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode()
    buffer.close()

    context = {
        'image_base64': image_base64,
    }

    return render(request, "admin/adminhome1.html", context)

def accuracy(request):
    accuracy_data = Accuracymodel.objects.all().first()

    if accuracy_data:
        svm_acc = float(accuracy_data.svm_acc)
        rfc_acc = float(accuracy_data.rfc_acc)
        gbc_acc = float(accuracy_data.gbc_acc)
        dnn_bert_acc = float(accuracy_data.dnn_bert_acc)
        
        # Create the bar chart
        accuracies = [svm_acc, rfc_acc, gbc_acc, dnn_bert_acc]
        labels = ['SVM', 'RFC', 'GBC', 'DNN-BERT']
        
        plt.figure(figsize=(10, 5))
        plt.bar(labels, accuracies, color=['blue', 'green', 'red', 'purple'])
        plt.xlabel('Models')
        plt.ylabel('Accuracy')
        plt.title('Model Accuracies')
        
        # Convert the plot to a PNG image
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.read()).decode()
        buffer.close()
        plt.close()
        context = {
            'image_base64': image_base64,
        }
        return render(request, "admin/adminhome2.html", context)