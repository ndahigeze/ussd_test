from django.shortcuts import render

# Create your views here.
from rest_framework import status, renderers
from rest_framework.response import Response
from rest_framework.views import APIView


class PlainTextRenderer(renderers.BaseRenderer):
    media_type = 'text/plain'
    format = 'txt'

    def render(self, data, media_type=None, renderer_context=None):
        return data.encode(self.charset)

class HandleUssd(APIView):

    renderer_classes = [PlainTextRenderer]

    def post(self,request):

        session_id = request.POST['sessionId']
        serviceCode = request.POST['serviceCode']
        phone_number = request.POST['phoneNumber']
        text = request.POST['text']
        response = ""
        # print(text)

        if len(text)<2:
            if text == '':
                response = "CON Murakaza neza k’ubutabazi bw’Umwana Hitamo ururimi: \n"
                response += "1. Kinyarwanda \n"
                response += "2. English \n"
                response += "3. French "
            elif text == '1':
                response = "CON Hitamo uwo ubariza \n"
                response += "1. Njye \n"
                response += "2. Undi"
            elif text == '2':
                response = "CON Choose victim \n"
                response += "1. Me \n"
                response += "2. Other"
            elif text == "3":
                response = "CON Choisir victim \n"
                response += "1. Moi \n"
                response += "2. Autre"
        else:
            print(text.split("*"))

            splited_text=text.split("*")

            if len(splited_text)==2: #step 2 after choosing who is reporting

                if splited_text[0]=='1': # kinyarwanda

                    if splited_text[1]=='2':
                        response = "CON Uzuza amazina ye \n"
                    elif splited_text[1] == '1':
                        response = "CON Hitamo Icyaha  \n"
                        response += "1. Gusambanya umwana \n"
                        response += "2. Gufata kungufu"
                        response += "3. Guhohoterwa \n"
                        response += "4. Ibindi"
                    else:
                        response = "END Mwahisemo umubare utariwo  \n"
                elif splited_text[0]=='2': # Icyonjereza
                    if splited_text[1] == '2':
                        response = "CON Write victim name \n"
                    elif splited_text[1] == '1':
                        response = "CON Choose a crime \n"
                        response += "1. Gusambanya umwana \n"
                        response += "2. Gufata kungufu \n"
                        response += "3. Guhohoterwa \n"
                        response += "4. Ibindi"
                    else:
                        response = "END You choose the incorect number  \n"

                elif splited_text[0]=='3': # Ijyifaransa
                    if splited_text[1] == '2':
                        response = "CON écris victim name \n"
                    elif splited_text[1] == '1':
                        response = "CON Choisir a crime \n"
                        response += "1. Gusambanya umwana \n"
                        response += "2. Gufata kungufu \n"
                        response += "3. Guhohoterwa \n"
                        response += "4. Ibindi"
                    else:
                        response = "END Vous choisissez numéro incorrect  \n"

            elif len(splited_text)==3: #step 3 for choosing province after choosing a crime

                if splited_text[0] == '1':  # kinyarwanda
                    response = "CON Hitamo Aho muherereye: \n"
                    response += "1. Umujyi wa Kigali \n"
                    response += "2. Iburasirazuba \n"
                    response += "3. Iburengerazuba \n"
                    response += "4. Amajyepfo \n"
                    response += "5. Amajyaruguru"
                elif splited_text[0] == '2':  # Icyonjereza
                    response = "CON Choose your location: \n"
                    response += "1. Kigali \n"
                    response += "2. Eastern Province \n"
                    response += "3. Western Province \n"
                    response += "4. South Province \n"
                    response += "5. Norther Province"

                elif splited_text[0] == '3':  # Ijyifaransa
                    response = "CON Choisissez votre emplacement: \n"
                    response += "1. Ville de Kigali \n"
                    response += "2. Province East \n"
                    response += "3. Province Ouest \n"
                    response += "4. Province Sud \n"
                    response += "4. Province Nord"
            elif len(splited_text)==4: #step 4 for choosing district after choosing province

                if splited_text[0] == '1':  # kinyarwanda
                    if splited_text[3]=='1': #kigali districts
                        response = "CON Hitamo akarere: \n"
                        response += "1. Umujyi wa Kigali \n"
                        response += "2. Iburasirazuba \n"
                        response += "3. Iburengerazuba \n"
                        response += "4. Amajyepfo"
                    elif splited_text[3]=='2': #Province East district
                        response = "CON Hitamo akarere: \n"
                        response += "1. Umujyi wa Kigali \n"
                        response += "2. Iburasirazuba \n"
                        response += "3. Iburengerazuba \n"
                        response += "4. Amajyepfo"
                    elif splited_text[3]=='3': #Province Ouest
                        response = "CON Hitamo akarere: \n"
                        response += "1. Umujyi wa Kigali \n"
                        response += "2. Iburasirazuba \n"
                        response += "3. Iburengerazuba \n"
                        response += "4. Amajyepfo"
                    elif splited_text[3]=='4': #amajyepfo  districts
                        response = "CON Hitamo akarere: \n"
                        response += "1. Umujyi wa Kigali \n"
                        response += "2. Iburasirazuba \n"
                        response += "3. Iburengerazuba \n"
                        response += "4. Amajyepfo"
                    elif splited_text[3]=='5': #amajyaruguru  districts
                        response = "CON Hitamo Aho akarere: \n"
                        response += "1. Umujyi wa Kigali \n"
                        response += "2. Iburasirazuba \n"
                        response += "3. Iburengerazuba \n"
                        response += "4. Amajyepfo"
                    else:
                        response = "END Mwahisemo umubare utariwo  \n"

                elif splited_text[0] == '2':  # English
                    if splited_text[3]=='1': #kigali districts
                        response = "CON Choose your district: \n"
                        response += "1. Umujyi wa Kigali \n"
                        response += "2. Iburasirazuba \n"
                        response += "3. Iburengerazuba \n"
                        response += "4. Amajyepfo"
                    elif splited_text[3]=='2': #Province East district
                        response = "CON Choose your district: \n"
                        response += "1. Umujyi wa Kigali \n"
                        response += "2. Iburasirazuba \n"
                        response += "3. Iburengerazuba \n"
                        response += "4. Amajyepfo"
                    elif splited_text[3]=='3': #Province Ouest
                        response = "CON Choose your district: \n"
                        response += "1. Umujyi wa Kigali \n"
                        response += "2. Iburasirazuba \n"
                        response += "3. Iburengerazuba \n"
                        response += "4. Amajyepfo"
                    elif splited_text[3]=='4': #Southern  districts
                        response = "CON Choose your district: \n"
                        response += "1. Umujyi wa Kigali \n"
                        response += "2. Iburasirazuba \n"
                        response += "3. Iburengerazuba \n"
                        response += "4. Amajyepfo"
                    elif splited_text[3]=='5': #Northern districts
                        response = "CON Choose your district: \n"
                        response += "1. Umujyi wa Kigali \n"
                        response += "2. Iburasirazuba \n"
                        response += "3. Iburengerazuba \n"
                        response += "4. Amajyepfo"
                    else:
                        response = "END You choose the incorect number   \n"
                elif splited_text[0] == '3': #france
                    if splited_text[3]=='1': #kigali districts
                        response = "CON Choisissez votre district: \n"
                        response += "1. Umujyi wa Kigali \n"
                        response += "2. Iburasirazuba \n"
                        response += "3. Iburengerazuba \n"
                        response += "4. Amajyepfo"
                    elif splited_text[3]=='2': #East districts
                        response = "CON Choisissez votre district: \n"
                        response += "1. Umujyi wa Kigali \n"
                        response += "2. Iburasirazuba \n"
                        response += "3. Iburengerazuba \n"
                        response += "4. Amajyepfo"
                    elif splited_text[3]=='3': #Province Ouest
                        response = "CON Choisissez votre district: \n"
                        response += "1. Umujyi wa Kigali \n"
                        response += "2. Iburasirazuba \n"
                        response += "3. Iburengerazuba \n"
                        response += "4. Amajyepfo"
                    elif splited_text[3]=='4': #Southern districts
                        response = "CON Choisissez votre district: \n"
                        response += "1. Umujyi wa Kigali \n"
                        response += "2. Iburasirazuba \n"
                        response += "3. Iburengerazuba \n"
                        response += "4. Amajyepfo"
                    elif splited_text[3]=='5': #Amajyaruguru districts
                        response = "CON Choisissez votre district: \n"
                        response += "1. Umujyi wa Kigali \n"
                        response += "2. Iburasirazuba \n"
                        response += "3. Iburengerazuba \n"
                        response += "4. Amajyepfo"
                    else:
                        response = "END Vous choisissez numéro incorrect \n"











        # print(session_id,serviceCode,phone_number,text)
        #     print(text)
        # print("------")
        # print(text)


        return Response(response,status=status.HTTP_200_OK)



class HandleEvent(APIView):

    def post(self,request):

        session_id = request.POST['sessionId']
        serviceCode = request.POST['serviceCode']
        r_status = request.POST['status']
        r_msg = request.POST['errorMessage']
        print(r_status,r_msg)
        response = "END message"
        return Response(response,status=status.HTTP_200_OK,headers={"Content-Type":"text/plain"})
