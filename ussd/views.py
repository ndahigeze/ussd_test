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


# Handle crime menu
def handle_choose_crime(lang):
    response=""
    if lang == '1':  # kinyarwanda
        response = "CON Hitamo Icyaha  \n"
        response += "1. Gusambanya umwana \n"
        response += "2. Gufata kungufu \n"
        response += "3. Guhohoterwa \n"
        response += "4. Ibindi"
    elif lang=='2':
        response = "CON Choose a crime \n"
        response += "1. Gusambanya umwana \n"
        response += "2. Gufata kungufu \n"
        response += "3. Guhohoterwa \n"
        response += "4. Ibindi"
    elif lang=='3':
        response = "CON Choisir a crime \n"
        response += "1. Gusambanya umwana \n"
        response += "2. Gufata kungufu \n"
        response += "3. Guhohoterwa \n"
        response += "4. Ibindi"
    return response

def handle_choose_province(lang):
    response=''
    if lang == '1':  # kinyarwanda
        response = "CON Hitamo Aho muherereye: \n"
        response += "1. Umujyi wa Kigali \n"
        response += "2. Iburasirazuba \n"
        response += "3. Iburengerazuba \n"
        response += "4. Amajyepfo \n"
        response += "5. Amajyaruguru"
    elif lang == '2':  # Icyonjereza
        response = "CON Choose your location: \n"
        response += "1. Kigali \n"
        response += "2. Eastern Province \n"
        response += "3. Western Province \n"
        response += "4. South Province \n"
        response += "5. Norther Province"

    elif lang == '3':  # Ijyifaransa
        response = "CON Choisissez votre emplacement: \n"
        response += "1. Ville de Kigali \n"
        response += "2. Province East \n"
        response += "3. Province Ouest \n"
        response += "4. Province Sud \n"
        response += "4. Province Nord"
    return response

def handle_choose_district(lang,pro):
    response=''
    if lang == '1':  # kinyarwanda
        if pro == '1':  # kigali districts
            response = "CON Hitamo akarere: \n"
            response += "1. Umujyi wa Kigali \n"
            response += "2. Iburasirazuba \n"
            response += "3. Iburengerazuba \n"
            response += "4. Amajyepfo"
        elif pro == '2':  # Province East district
            response = "CON Hitamo akarere: \n"
            response += "1. Umujyi wa Kigali \n"
            response += "2. Iburasirazuba \n"
            response += "3. Iburengerazuba \n"
            response += "4. Amajyepfo"
        elif pro == '3':  # Province Ouest
            response = "CON Hitamo akarere: \n"
            response += "1. Umujyi wa Kigali \n"
            response += "2. Iburasirazuba \n"
            response += "3. Iburengerazuba \n"
            response += "4. Amajyepfo"
        elif pro == '4':  # amajyepfo  districts
            response = "CON Hitamo akarere: \n"
            response += "1. Umujyi wa Kigali \n"
            response += "2. Iburasirazuba \n"
            response += "3. Iburengerazuba \n"
            response += "4. Amajyepfo"
        elif pro == '5':  # amajyaruguru  districts
            response = "CON Hitamo akarere: \n"
            response += "1. Umujyi wa Kigali \n"
            response += "2. Iburasirazuba \n"
            response += "3. Iburengerazuba \n"
            response += "4. Amajyepfo"
        else:
            response = "END Mwahisemo umubare utariwo  \n"

    elif lang == '2':  # English
        if pro == '1':  # kigali districts
            response = "CON Choose your district: \n"
            response += "1. Umujyi wa Kigali \n"
            response += "2. Iburasirazuba \n"
            response += "3. Iburengerazuba \n"
            response += "4. Amajyepfo"
        elif pro == '2':  # Province East district
            response = "CON Choose your district: \n"
            response += "1. Umujyi wa Kigali \n"
            response += "2. Iburasirazuba \n"
            response += "3. Iburengerazuba \n"
            response += "4. Amajyepfo"
        elif pro == '3':  # Province Ouest
            response = "CON Choose your district: \n"
            response += "1. Umujyi wa Kigali \n"
            response += "2. Iburasirazuba \n"
            response += "3. Iburengerazuba \n"
            response += "4. Amajyepfo"
        elif pro == '4':  # Southern  districts
            response = "CON Choose your district: \n"
            response += "1. Umujyi wa Kigali \n"
            response += "2. Iburasirazuba \n"
            response += "3. Iburengerazuba \n"
            response += "4. Amajyepfo"
        elif pro == '5':  # Northern districts
            response = "CON Choose your district: \n"
            response += "1. Umujyi wa Kigali \n"
            response += "2. Iburasirazuba \n"
            response += "3. Iburengerazuba \n"
            response += "4. Amajyepfo"
        else:
            response = "END You choose the incorect number \n"
    elif lang == '3':  # france
        if pro == '1':  # kigali districts
            response = "CON Choisissez votre district: \n"
            response += "1. Umujyi wa Kigali \n"
            response += "2. Iburasirazuba \n"
            response += "3. Iburengerazuba \n"
            response += "4. Amajyepfo"
        elif pro == '2':  # East districts
            response = "CON Choisissez votre district: \n"
            response += "1. Umujyi wa Kigali \n"
            response += "2. Iburasirazuba \n"
            response += "3. Iburengerazuba \n"
            response += "4. Amajyepfo"
        elif pro == '3':  # Province Ouest
            response = "CON Choisissez votre district: \n"
            response += "1. Umujyi wa Kigali \n"
            response += "2. Iburasirazuba \n"
            response += "3. Iburengerazuba \n"
            response += "4. Amajyepfo"
        elif pro == '4':  # Southern districts
            response = "CON Choisissez votre district: \n"
            response += "1. Umujyi wa Kigali \n"
            response += "2. Iburasirazuba \n"
            response += "3. Iburengerazuba \n"
            response += "4. Amajyepfo"
        elif pro == '5':  # Amajyaruguru districts
            response = "CON Choisissez votre district: \n"
            response += "1. Umujyi wa Kigali \n"
            response += "2. Iburasirazuba \n"
            response += "3. Iburengerazuba \n"
            response += "4. Amajyepfo"
        else:
            response = "END Vous choisissez numéro incorrect \n"
    return response

def end_process_msg(lang):
    response=""
    if lang=='1':
        response="END Twakiriye ikirego cyanyu "
    elif lang=='2': #ENGLISH
        response='END Crime report is successfully received'
    elif lang=='3': #FRENCH
        response='END Votre crime rapport a reçu'
    return response


def wrong_choice_msg(lang):
    response=""
    if lang=='1':
        response="END Mwahisemo umubare utariwo "
    elif lang=='2': #ENGLISH
        response='END You choose the incorect number'
    elif lang=='3': #FRENCH
        response='END Vous choisissez numéro incorrect '
    return response





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
                        response += "2. Gufata kungufu \n"
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
                if splited_text[1]=='2': #if user choose Other as victim will choose crime before choosing province
                    response = handle_choose_crime(splited_text[0])
                else:
                    if splited_text[2] == '4':
                        if splited_text[0] == '1':  # kinyarwanda
                            response = "CON Andika icyaha"
                        elif splited_text[0] == '2':
                            response = "CON Write a crime"
                        elif splited_text[0] == '3':  # Ijyifaransa
                            response = "CON écris a crime"
                    else:
                        response= handle_choose_province(splited_text[0])

            elif len(splited_text)==4 and splited_text[1]=='2' and (not splited_text[2].isnumeric() or len(splited_text[2])>1) and splited_text[3]=='4': #step 4
                #if victim is other and crim is other
                if splited_text[0] == '1':  # kinyarwanda
                    response = "CON Andika icyaha"
                elif splited_text[0] == '2':
                    response = "CON Write a crime"
                elif splited_text[0] == '3':  # Ijyifaransa
                    response = "CON écris a crime"
            elif len(splited_text)==4 and splited_text[1]=='2' and (not splited_text[2].isnumeric() or len(splited_text[2])>1) and splited_text[3] is not'4':
                #if victim is other and crime is not other
                response = handle_choose_province(splited_text[0])
            elif len(splited_text)==4 and splited_text[1] is not '2' and splited_text[2]=='4' and (len(splited_text[3])>1 or not splited_text[3].isnumeric):
                # if victim is not other but crime is other
                response = handle_choose_province(splited_text[0])
            elif len(splited_text)==4 and splited_text[1] is not '2' and splited_text[2] is not '4': #choose district
                #if victim and crime are not other
                response=handle_choose_district(splited_text[0],splited_text[3])
            elif len(splited_text)==5 and splited_text[1] =='2' and (not splited_text[2].isnumeric() or len(splited_text[2])>1) and splited_text[3]=='4' and (len(splited_text[4])>1 or not splited_text[4].isnumeric):
                #choose province
                # if victim is other and crime is other and wrote the crime
                response = handle_choose_province(splited_text[0])

            elif len(splited_text)==5 and splited_text[1] =='2' and (not splited_text[2].isnumeric() or len(splited_text[2])>1) and splited_text[3] is not '4': #choose district
               #if victim is other and crime number and write the crime and choose the province
                response = handle_choose_district(splited_text[0], splited_text[4])
            elif len(splited_text)==5 and splited_text[1] =='1' and splited_text[2]=='4' and (len(splited_text[3])>1 or not splited_text[3].isnumeric): #choose district
                #if victim is number, crime is other, crime and province are provided
                response = handle_choose_district(splited_text[0], splited_text[4])
            elif len(splited_text) == 5 and splited_text[1] is not '2' and splited_text[2] is not '4' and splited_text[2].isnumeric: #end process
                #end process if crime and victim are not other
                response =end_process_msg(splited_text[0])

            elif len(splited_text)==6 and splited_text[1] =='2' and (not splited_text[2].isnumeric() or len(splited_text[2])>1) and splited_text[3]=='4' and (len(splited_text[4])>1 or not splited_text[4].isnumeric):
                #choose district
                # if victim is other and crime is other and wrote the crime and province was choosen
                response = handle_choose_district(splited_text[0], splited_text[5])
            elif len(splited_text)==6 and splited_text[1] =='2' and (not splited_text[2].isnumeric() or len(splited_text[2])>1) and (splited_text[3] is not '4'and splited_text[3].isnumeric): #end process
                #end process if victim is other and crime is not other
                response = end_process_msg(splited_text[0])
            elif  len(splited_text)==6 and splited_text[1] =='1'and splited_text[2]=='4' and (len(splited_text[3])>1 or not splited_text[3].isnumeric): #end process
                # if victim is number, crime is other, crime and province are provided
                response = end_process_msg(splited_text[0])
            elif len(splited_text)==7 and splited_text[1] =='2' and (not splited_text[2].isnumeric() or len(splited_text[2])>1) and splited_text[3]=='4' and (len(splited_text[4])>1 or not splited_text[4].isnumeric):
                #end process
                #if victim and crime are both other
                response = end_process_msg(splited_text[0])
            else:
                response = wrong_choice_msg(splited_text[0])


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
