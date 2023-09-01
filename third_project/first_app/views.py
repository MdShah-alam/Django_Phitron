from django.shortcuts import render

# Create your views here.

# def contact(request):
#     return render(request , './first_app/index.html',{'courses' : [
#         {
#             'id':'1',
#             'course' : 'c',
#             'teacher' : 'Rahim'
#         },
#         {
#             'id' :'2',
#             'course' : 'c++',
#             'teacher' : 'karim'
#         },
#         {
#             'id' :'3',
#             'course' :'python',
#             'teacher':'Fahim'
#         }
#     ]})

def contact(request):
    return render(request,'./first_app/index.html', {"name":"I am Shah_Alam","marks":90,"lst":[10,20,4,23],
    "blog":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Nobis non a molestias veritatis voluptatibus aliquam architecto illo fugiat nam, eos molestiae praesentium? Magni, eos debitis? Itaque vero esse dolore dolores!"})
