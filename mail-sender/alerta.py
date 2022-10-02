import ssl
import os
import smtpd
from email.message import EmailMessage
import smtplib

# Function
def alerta(dts):
    # credentials
    emisor = 'terracubistasspaceapp@gmail.com'
    password = 'anwiduowrvqpmhmh'
    receptor = ['a.talice@alumno.etec.um.edu.ar','n.bartolomeo@alumno.etec.um.edu.ar','germanguillomarquez@gmail.com']

    # Email content
    asunto = 'Warning!'
    
    if dts <= -100 and dts > -250:
        cuerpo = """
        Strong solar storm is coming!!
        dts:
        """ + str(dts)
    elif dts <= -250:
        cuerpo = """
        Super solar storm incoming! 
        For your security and your device's safety, 
        please turn off and disconnect all electronic gadgets.
        
        Tips for a solar storm:
        1. Keep calm. The initial effects of an extreme solar storm would be very similar to those of a "big blackout" and the most important thing in a first reaction would not worsen the situation in those "30 minutes".
        2. Avoid traveling on any public road, given what is expected to be a sharp increase in accidents on public roads due to the failure of traffic lights and signs in the following minutes. 30 minutes before such an event is not the time to go anywhere that is not immediate and unless we are somewhere with greater exposure.
        3. In buildings avoid taking any elevator or similar
        4. If we find ourselves on the metro network or any public or private means of transport, leave it / park it calmly, - for which we have plenty of time in 30 minutes -, and go to any open space such as a square or inside any local easily accessible as a simple cafeteria. In other words, place ourselves outside transport, but also outside public roads as much as possible. If we are near power stations, gas stations or especially sensitive places like these, we will also move away normally.
        5. Nor would it be advisable to make telephone calls, and in any case it is possible to foresee the momentary collapse of the lines, since that would be the reaction of many people. A brief SMS to any family member indicating our position, or much better a previous family self-protection plan with a meeting place clearly defined in advance in case of emergencies, would be much better alternatives. 
        6. In addition, if we are at home, a good option in the face of such a public alert from the authorities may be to fill the bathtub and containers with drinking water, since one of the estimated effects of an extreme Carrington-type solar storm could be the interruption of the electricity supply. water in large areas, particularly above second story heights. It could also be advisable to group all the frozen food in the same drawer so that the cold is kept longer in case of loss of electricity.
        7. Finally, it must be remembered that candles and other combustion elements in the home are inherently dangerous and that it is advisable to resort to other battery-powered lighting elements, by dynamo
        8. Already in the post-event, the first element of self-protection that should be counted on is a radio (also battery-powered or through dynamo or solar recharging systems) to be able to follow from that moment on with complete peace of mind the recommendations of the authorities and reports of the evolution of the situation that with all predictability would be by radio. The importance of the latter must be particularly stressed, and a small radio and some backup batteries is an element easily within everyone's reach.

        dts: """ + str(dts)

    for i in receptor:
        em = EmailMessage()
        em['From'] = emisor
        em['To'] = i
        em['Subject'] = asunto
        em.set_content(cuerpo)

        contexto = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
            smtp.login(emisor, password)
            smtp.sendmail(emisor, receptor, em.as_string())


# ---------------------------------
# | Call function for send emails |
# ---------------------------------
# dtsValue = 100
# from alerta import alerta
# dts = int(dtsValue)
# alerta(dts)

