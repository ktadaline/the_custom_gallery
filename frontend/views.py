from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt



# Create your views here.

def index(request):
   # @csrf_exempt
    #@need_post_parameters([PARAM_MESSAGE_OBJ])
    #def post(self, request, *args, **kwargs):
     #   data = request.POST.get(PARAM_MESSAGE_OBJ)
      #  try:
      #      message_obj = json.loads(data)
       # except Exception as e:
        #    return HttpResponseBadRequest(error_json("Could not parse Json"))
    return render(request, 'frontend/index.html')
