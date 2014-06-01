from django.http import HttpResponse

def index(request):
    outstring = '''
這是首頁!<br />
<a href="admin">admin</a><br />
<a href="polls">polls</a><br />
'''
    return HttpResponse(outstring)
