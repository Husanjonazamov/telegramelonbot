
CHAT = \
"""
👋 Assalomu alaykum! 

Ishonchli va arzon taksi xizmati!
Taksi chaqirish uchun pastdagi tugmani bosing!
"""



START_MESSAGE = \
"""
<b>
Assalomu alaykum {}!
</b>
"""


COUNT_MESSAGE = \
"""
<b>
Hurmatli Mijoz Yo'lovchilar sonini kiriting!
</b>
"""


PASSENGER_PHONE_MESSAGE = \
"""
Iltimos telefon raqamingizni yozib yuboring yoki pastdagi <b>📲 Telefon raqamni yuborish</b> tugmasini bosing
"""


MAIL_SEND_MESSAGE = \
"""
Assalomu alaykum {}!
Sizning buyurtmangiz qabul qilndi✅
Lichkada sizni shofirlarimiz kutmoqda...
"""



SUCCES_PESSERGER = \
"""
<b>
✅ Sizning murojatingiz adminga yuborildi. Tez orada siz bilan bog'lanadi!
</b>
"""    


SUCCESS_RIDE = \
"""
✅ Tabriklaymiz! Siz yo'lovchini qabul qildingiz
"""

SUCCESS_MAIL = \
"""
✅ Tabriklaymiz! Siz pochtani qabul qildingiz
"""


# ACCEPTANCE_MESSAGE = \
# """
# <b>
# Sizning arizangizni @{} qabul qilishdi siz bilan bog'lanadi
# </b>
# """


# ACCEPTANCE_PASSENGER = \
# """
# <b>
# Bu yo'lovchi allaqachon @{} tomonidan qabul qilngan
# </b>
# """



DRIVER_NAME = \
"""
<b>
Ismingizni kiriting
</b>
"""


SEND_DRIVER = \
""" 
<b>
✅ Sizning arizangiz adminga yuborildi. Tez orada siz bilan bog'lanadi!
</b>
"""


PASSENGER_LOCATION_MESSAGE = \
"""
<b>
Qayerga bormoqchisiz !
</b>
"""



NOT_PESSERGER = \
"""
❌ Bu yo'lo'vchini faqat qabul qilgan taksi haydovchisi bekor qilishi mumkin.
"""

NOT_MAIL = \
"""
❌ Bu pochtani faqat qabul qilgan taksi haydovchisi bekor qilishi mumkin.
"""



MAIL_LOCATION = \
"""
<b>
Pochtangizni qayerga yubormoqchisiz?
</b>
"""



MAIL_SUCCESS = \
"""
<b>
✅ Sizning pochtangiz qabul qilindi. Tez orada siz bilan shofirlarimiz bog'lanishadi!
</b>
"""


def confirmation_user(**kwargs):
    confirmation = ''

    confirmation += f'<b>Malumot:</b>\n\n'
    confirmation += f"<b>Yo'lovchi soni: {kwargs['count']}</b>\n"
    confirmation += f"<b>Manzil: {kwargs['location']}</b>\n"
    confirmation += f'<b>Telefon: {kwargs['phone_number']}</b>\n\n'
    
    
    return confirmation


def confirmation_admin(**kwargs):
    confirmation = ''

    confirmation += f"<b>Yo'lovchi:</b>\n\n"
    confirmation += f"<b>Username: @{kwargs['username']}</b>\n"
    confirmation += f"<b>Yo'lovchi soni: {kwargs['count']}</b>\n"
    confirmation += f"<b>Manzil: {kwargs['location']}</b>\n"
    confirmation += f'<b>Telefon: {kwargs['phone_number']}</b>\n\n'
    
    
    return confirmation
    
    

def send_driver_admin(**kwargs):
    driver_admin = ''
    
    driver_admin += f"<b>Yangi ariza:</b>\n\n"
    driver_admin += f"<b>ism: {kwargs['name']}</b>\n"
    driver_admin += f"<b>Username: @{kwargs['username']}</b>\n"
    driver_admin += f'<b>Telefon: {kwargs['phone']}</b>\n'
    
    
    return driver_admin


def cancel_pesserger_admin(**kwargs):
    confirmation = ''

    confirmation += f"<b>Yo'lovchi:</b>\n\n"
    confirmation += f"<b>Username: {kwargs['username']}</b>\n"
    confirmation += f"<b>Yo'lovchi soni: {kwargs['count']}</b>\n"
    confirmation += f"<b>Manzil: {kwargs['location']}</b>\n"
    confirmation += f'<b>Telefon: {kwargs['phone_number']}</b>\n\n'
    
    
    return confirmation



def mail_send_channel(**kwargs):
    mail_send = ''
    
    mail_send += f"<b>Po'chta:</b>\n\n"
    mail_send += f"<b>Username: @{kwargs['username']}</b>\n" 
    mail_send += f"<b>Manzil: {kwargs['location']}</b>\n" 
    mail_send += f"<b>Telefon: {kwargs['phone']}</b>\n" 
    
    return mail_send



def cancel_mail_send_channel(**kwargs):
    mail_send = ''
    
    mail_send += f"<b>Po'chta:</b>\n\n"
    mail_send += f"<b>Username: {kwargs['username']}</b>\n" 
    mail_send += f"<b>Manzil: {kwargs['location']}</b>\n" 
    mail_send += f"<b>Telefon: {kwargs['phone']}</b>\n" 
    
    
    return mail_send



def text_to_send(**kwargs):
    group_mail_send = ''
    group_mail_send += f"<b>Po'chta:</b>\n\n"
    group_mail_send += f"<b>Username: @{kwargs['username']}</b>\n" 
    group_mail_send += f"<b>Ariza: {kwargs['mail']}</b>\n" 
    
    
    return group_mail_send


def text_to_send_cancel(**kwargs):
    group_mail_send = ''
    group_mail_send += f"<b>Po'chta:</b>\n\n"
    group_mail_send += f"<b>Username: {kwargs['username']}</b>\n" 
    group_mail_send += f"<b>Ariza: {kwargs['application']}</b>\n" 
    
    
    return group_mail_send





DID_ACCEPT = \
"""
Shofir bilan kelisha oldingizmi?\n
Kelisha olmagan bo'lsangiz <b>❌ Yoq</b> tugmasini bosing.
Arizangiz qaytadan tashlab beriladi
"""


DID_SUCCESS = \
"""
Safaringiz bexatar bo'lsin!
"""