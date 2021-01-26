from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import View

# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')
    def post(self,request):
        data=request.POST

        # from gtts import gTTS

        # import os
        number = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
        ty = ['', '', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninty']
        tens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
                'ineteen']
        n = int(data["nu"])
        if n == 1000000:
            return HttpResponse("Ten Lakhs")
            # print("Ten lakhs")
            # ans="Ten Lakhs"
            # return render(request, 'answer.html', {'nu': ans})

        elif n < 1000000:
            list = [0, 0, 0, 0, 0, 0]
            i = 0
            while n > 0:
                list[i] = n % 10
                i += 1
                n = n // 10
            num = ""

            if list[5] != 0:
                num += number[list[5]] + " Lakh "

            if list[4] != 0:
                if (list[4] == 1):
                    num += tens[list[3]] + " thousand "
                else:
                    num += ty[list[4]] + " " + number[list[3]] + ' thousand '

            else:
                if list[3] != 0:
                    num += number[list[3]] + " thousand "
            if list[2] != 0:
                num += number[list[2]] + " hundred "
            if list[1] != 0:
                if (list[1] == 1):
                    num += tens[list[0]]
                else:
                    num += ty[list[1]] + " " + number[list[0]]

            else:
                if list[0] != 0:
                    num += number[list[0]]

            return HttpResponse(num)
            # return render(request, 'answer.html', {'ny': num})

            # print(num)
        else:
            return HttpResponse("The number must be less than Ten lakhs")
            # ny="The number must be less than Ten lakhs"
            # return render(request, 'answer.html', {'ny': ny})
            # print('the number must be less than Ten lakhs')
            # mytext = num
            # language = 'en'
            # myobj = gTTS(text=mytext, lang=language, slow=False)
            # myobj.save("welcome.mp3")
            #
            # # Playing the converted file
            # os.system("mpg321 welcome.mp3")







# class Answer(View):
#     def get(self,request):
#         return render(request,'answer.html')