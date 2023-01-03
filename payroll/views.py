from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from django.contrib.staticfiles.utils import get_files
from django.contrib.staticfiles.storage import StaticFilesStorage
import os
from .models import Payroll, CustomUser
from authentication.serializers import CustomUserSerializer, UserSerializer
from .serializers import PayrollSerializer
from rest_framework.authtoken.models import Token
from django.http import HttpResponse


# Create your views here.
@api_view(['POST']) 
# @permission_classes([IsAuthenticated])
def payrolls_register(request):
    year = request.data.get('year', None)
    s = StaticFilesStorage()
    # files = list(get_files(s, location='pdf_files/2021'))
    files = list(get_files(s, location=str('pdf_files/'+year)))
    for file in files:
        pdf_filename = file.split('\\')[1] # "NOM1221_2022-01-01.pdf"
        pdf_dataname = pdf_filename.split('_')
        employee_data = pdf_dataname[0]
        code_employee = employee_data.split('NOM')[1]
        data_pdf = pdf_dataname[1]
        date_pdf = data_pdf.split('.pdf')[0]
            
        user = CustomUser.objects.get(code_employee=code_employee)
        Payroll.objects.create(
            user = user,
            payment_date = date_pdf,
            payroll_filename = pdf_filename
        )

    return Response({
        # "code_employee": code_employee,
        # "user": serializer.data,
        # "user_id": user.id,
        # "date": date_pdf,
        # "pdf_filename": pdf_filename
        "msg": "Registros realizados"
    })


# Create your views here.
@api_view(['POST']) 
# @permission_classes([IsAuthenticated])
def payrolls_register_on_render(request):
    year = request.data.get('year', None)
    s = StaticFilesStorage()

    link_files = {

    "NOM1222_2021-01-01.pdf": "https://drive.google.com/file/d/16fqMX4hjQgJfIgENSJx8RD0j6TYkagH1/view?usp=drivesdk",

    "NOM1221_2021-12-10.pdf": "https://drive.google.com/file/d/18L87LrguUdxoi8UacKEn7EJDYx5bt_jP/view?usp=drivesdk",

    "NOM1221_2021-10-22.pdf": "https://drive.google.com/file/d/1IfCF4S761QJnjx4b3aEIFnvE-qrDoLjY/view?usp=drivesdk",


    "NOM1222_2021-06-11.pdf": "https://drive.google.com/file/d/1Kl83pycg0gSUT4Qmqvspg1Ve5fFKdk7T/view?usp=drivesdk",



    "NOM1222_2021-10-08.pdf": "https://drive.google.com/file/d/13OZDvvG4B_AN-UeBhZIfkPo3rARxfqqy/view?usp=drivesdk",



    "NOM1222_2021-01-29.pdf": "https://drive.google.com/file/d/1JiTedIS9g-ErN7fOHJBqbSwQm7GDIWqe/view?usp=drivesdk",



    "NOM1221_2021-03-19.pdf": "https://drive.google.com/file/d/1nw1RH05eXUJVDox2I9--Y_F2L8pMhm15/view?usp=drivesdk",



    "NOM1221_2021-05-14.pdf": "https://drive.google.com/file/d/1CVNrCs3N2kWbpNZzTkYdJUs38OI8kbnt/view?usp=drivesdk",



    "NOM1221_2021-01-15.pdf": "https://drive.google.com/file/d/1UUAVdhtsa-5XGBofS1IJvGjtPWPxwavM/view?usp=drivesdk",


    "NOM1221_2021-12-17.pdf": "https://drive.google.com/file/d/1-3ALdtlMddm1fGh4M9hVS1AzziKs-WEl/view?usp=drivesdk",



    "NOM1221_2021-08-20.pdf": "https://drive.google.com/file/d/1iw7KjJ3Lsf2FIuFTqz6cSzOzPF483Ckj/view?usp=drivesdk",



    "NOM1222_2021-01-08.pdf": "https://drive.google.com/file/d/1LOAbwwVTBh9GfLycZWtZjWyrIq3S86w0/view?usp=drivesdk",



    "NOM1221_2021-09-17.pdf": "https://drive.google.com/file/d/1O4BAS6k19jj3tGsFO28_IRhQ8Wn4gsGC/view?usp=drivesdk",



    "NOM1221_2021-03-12.pdf": "https://drive.google.com/file/d/18oXCXTZq-Dv32e534qz80-zqqPPb81tr/view?usp=drivesdk",



    "NOM1222_2021-07-16.pdf": "https://drive.google.com/file/d/1Tm29LIUshXmWMNy1YQRCK7KhA-1A11sX/view?usp=drivesdk",



    "NOM1222_2021-10-29.pdf": "https://drive.google.com/file/d/1w6M62xExOZt3Oau23EzMsNZdBJ_tCtnl/view?usp=drivesdk",



    "NOM1222_2021-11-05.pdf": "https://drive.google.com/file/d/1OcL37ECm98z7cQibaucAA5w5YukmpCe8/view?usp=drivesdk",



    "NOM1222_2021-01-22.pdf": "https://drive.google.com/file/d/1EpSLstuj0hs63Bu3BTzj9wgB1JvnNWA6/view?usp=drivesdk",


    "NOM1222_2021-04-30.pdf": "https://drive.google.com/file/d/1DMe3Vg36vL6CBBrHIAp0j1NvZsXufq3H/view?usp=drivesdk",



    "NOM1221_2021-07-09.pdf": "https://drive.google.com/file/d/1k0dt0djforQMiStubE5faIDnh3k41Y4a/view?usp=drivesdk",



    "NOM1222_2021-05-21.pdf": "https://drive.google.com/file/d/1p5nD1v3MpT8DwY9_-UBKsi_UjIPATjtO/view?usp=drivesdk",



    "NOM1221_2021-06-18.pdf": "https://drive.google.com/file/d/1IMZdPfHvUqZIjsAANQUz5XVqdyQbAgfm/view?usp=drivesdk",



    "NOM1221_2021-04-16.pdf": "https://drive.google.com/file/d/1no6t4c-DVtTbM2x1OXzdEhbTy1i4DSFc/view?usp=drivesdk",



    "NOM1222_2021-11-26.pdf": "https://drive.google.com/file/d/1QCzU98ZLeHKWP6AnelRpW2Nti6hHtYzm/view?usp=drivesdk",



    "NOM1222_2021-03-19.pdf": "https://drive.google.com/file/d/15tfKGmJyMRTSb50lShE7iCmQArou_NRc/view?usp=drivesdk",



    "NOM1221_2021-11-19.pdf": "https://drive.google.com/file/d/1JiYtns2ckd9CpvkrMzNsNz063dPBUtNa/view?usp=drivesdk",



    "NOM1221_2021-10-08.pdf": "https://drive.google.com/file/d/1iyb1RZEvTxtwv12zRqNZi2oQStoxLset/view?usp=drivesdk",



    "NOM1221_2021-06-04.pdf": "https://drive.google.com/file/d/1Sa7m5Jop30lIa-egrIx4ADsnz0qLbpcV/view?usp=drivesdk",



    "NOM1222_2021-03-05.pdf": "https://drive.google.com/file/d/10FsXY8BAu9uzdLyrnF3y_HHMUWP0WQe_/view?usp=drivesdk",



    "NOM1222_2021-10-22.pdf": "https://drive.google.com/file/d/1P8D2NwFyvr2sq0wG8poOUY0mSYtOcKEO/view?usp=drivesdk",



    "NOM1222_2021-06-18.pdf": "https://drive.google.com/file/d/1y6wx9aVvY0V35BcxuD50lW0D2i4MgFBD/view?usp=drivesdk",



    "NOM1222_2021-05-14.pdf": "https://drive.google.com/file/d/1JGKhTCI_6RviGvUAfHerTekqXKsLKF5v/view?usp=drivesdk",



    "NOM1221_2021-05-21.pdf": "https://drive.google.com/file/d/1auZCt-wF34Kjj0YvJ2PRJLfFCnr8RckG/view?usp=drivesdk",



    "NOM1222_2021-02-12.pdf": "https://drive.google.com/file/d/1k_O1_RQ7SOevARgJzSNZ1Pt4DeIfZl1-/view?usp=drivesdk",



    "NOM1222_2021-12-17.pdf": "https://drive.google.com/file/d/1pEaCcZLBlJ2uQbTgnbHoha-uR1omYtS8/view?usp=drivesdk",



    "NOM1222_2021-01-15.pdf": "https://drive.google.com/file/d/1vDX-8yNChDxubkO9mvMRWGx_21lJWPkL/view?usp=drivesdk",



    "NOM1221_2021-04-09.pdf": "https://drive.google.com/file/d/1CSqVJ1P3cz4LNBE4Lnw9igZQNhV6zFU9/view?usp=drivesdk",



    "NOM1222_2021-09-10.pdf": "https://drive.google.com/file/d/13yA1XFf4nI-oOyCdpyki98oND1ljyE6r/view?usp=drivesdk",



    "NOM1221_2021-04-23.pdf": "https://drive.google.com/file/d/19HqmP5D7Kog9VkJ68tVvSolhdAptqoSi/view?usp=drivesdk",



    "NOM1222_2021-04-23.pdf": "https://drive.google.com/file/d/162t-8V7pLoWhuJUQfD-T1nIvg6USd_WY/view?usp=drivesdk",



    "NOM1221_2021-11-26.pdf": "https://drive.google.com/file/d/1Qr2Z8t260HWglaTvQ8yEs_-GI8Bvi47a/view?usp=drivesdk",



    "NOM1221_2021-09-24.pdf": "https://drive.google.com/file/d/1G6-pG6lwPlOmjlCdz1Xk3l8i7yF7vURZ/view?usp=drivesdk",



    "NOM1222_2021-04-09.pdf": "https://drive.google.com/file/d/1K4jHXJt02YPWZP6r3hsUVL8AEec0Vj5B/view?usp=drivesdk",



    "NOM1222_2021-02-05.pdf": "https://drive.google.com/file/d/1w-OzNON4Vrl40hfz14O9zAHE_TSLqVbq/view?usp=drivesdk",



    "NOM1221_2021-10-29.pdf": "https://drive.google.com/file/d/14nTkGFjWFsW52Yb9KZKgonsemcfpDE4n/view?usp=drivesdk",



    "NOM1221_2021-08-06.pdf": "https://drive.google.com/file/d/12ck3P6SMMyy7oV-bu0bl7ZILhtSbKfJ7/view?usp=drivesdk",



    "NOM1221_2021-03-05.pdf": "https://drive.google.com/file/d/1LUCYmJKwR3iErMCW6goyLRCXX98oBbRv/view?usp=drivesdk",



    "NOM1221_2021-09-03.pdf": "https://drive.google.com/file/d/1qx3OFNV0izlnPmyxsj8kSSGBa41Xxhak/view?usp=drivesdk",



    "NOM1221_2021-02-05.pdf": "https://drive.google.com/file/d/17m6uIU6mBloT1I8cZ5lrojX19f39hX5l/view?usp=drivesdk",



    "NOM1221_2021-12-03.pdf": "https://drive.google.com/file/d/1rxnSFu2xNy5_R_c1260CJRCB33IhryhR/view?usp=drivesdk",



    "NOM1221_2021-11-05.pdf": "https://drive.google.com/file/d/1unOWtiOZh2hUqUiL1TIQnH4KeKElDCRi/view?usp=drivesdk",



    "NOM1221_2021-04-02.pdf": "https://drive.google.com/file/d/1EKmyYpWMpx0s4pEwS05GB7GsiVEzAA_Y/view?usp=drivesdk",



    "NOM1221_2021-07-30.pdf": "https://drive.google.com/file/d/1p-WkgElvaJwdKxgh0KjbUmCAbkhTSrlM/view?usp=drivesdk",



    "NOM1222_2021-08-13.pdf": "https://drive.google.com/file/d/1JA3m8WpqNOz8mspdkyU2Nzfo6u5SHGPV/view?usp=drivesdk",



    "NOM1222_2021-12-10.pdf": "https://drive.google.com/file/d/1LI3dLqM_fH2tXAWxp6HfU-9n9wf1ds2M/view?usp=drivesdk",



    "NOM1221_2021-10-01.pdf": "https://drive.google.com/file/d/1Vj8lCo4wARJ0l1na6Amoz2_U4yZjlYBR/view?usp=drivesdk",



    "NOM1221_2021-06-25.pdf": "https://drive.google.com/file/d/15SqkXkjCBZWvuOyWYRbzdckegk2XZn7f/view?usp=drivesdk",



    "NOM1222_2021-08-20.pdf": "https://drive.google.com/file/d/1BGGx8pN92IG0NskXAFA57nR1FLq59Z_h/view?usp=drivesdk",



    "NOM1222_2021-09-17.pdf": "https://drive.google.com/file/d/1n-s4cGhCFyACkf5KlCxybPDlboZD_Bf4/view?usp=drivesdk",



    "NOM1221_2021-03-26.pdf": "https://drive.google.com/file/d/1r9wmf8Gg2jSUNenorRckDMgS7JpNFK9D/view?usp=drivesdk",



    "NOM1221_2021-05-28.pdf": "https://drive.google.com/file/d/1bY4r2lNLv7NnIf0pzOwpPgu_CvDxMhck/view?usp=drivesdk",



    "NOM1222_2021-10-01.pdf": "https://drive.google.com/file/d/1zlqZkfZvvdlWoXjT82VINP4u8ojv9ViI/view?usp=drivesdk",



    "NOM1221_2021-09-10.pdf": "https://drive.google.com/file/d/1Q4X4ggNXM6x1SyzhPZLXg5_ByFxYO6MP/view?usp=drivesdk",



    "NOM1222_2021-08-27.pdf": "https://drive.google.com/file/d/1wCyO6Zn90qmd_AEZwBA4EVfZKZwoSQ9l/view?usp=drivesdk",



    "NOM1221_2021-01-22.pdf": "https://drive.google.com/file/d/1P7Q7YNEVPNs0IC_csUUmmMVcLWN9RBBi/view?usp=drivesdk",



    "NOM1222_2021-07-02.pdf": "https://drive.google.com/file/d/1dY8Dizji3UD-FUNKw7iaDmCz3d2ENZOb/view?usp=drivesdk",



    "NOM1222_2021-02-26.pdf": "https://drive.google.com/file/d/10S6DRjiOUYeFnpGa6DoNuOxg1TwmVAiL/view?usp=drivesdk",



    "NOM1221_2021-02-12.pdf": "https://drive.google.com/file/d/1kmJNJtcFC0ncz2o_hmD8KP-9QDASuwtV/view?usp=drivesdk",



    "NOM1222_2021-10-15.pdf": "https://drive.google.com/file/d/1vV6AlLmP2b2jn6T9xkF1yDdLRUVK8ADa/view?usp=drivesdk",



    "NOM1222_2021-03-12.pdf": "https://drive.google.com/file/d/1HZGn-gLTul5dTte725zJUvvii3z-y2Ea/view?usp=drivesdk",



    "NOM1222_2021-12-03.pdf": "https://drive.google.com/file/d/1kUZhnX6VE2-TKj8opoI2rvhIEKvfKQOp/view?usp=drivesdk",



    "NOM1221_2021-11-12.pdf": "https://drive.google.com/file/d/1ubCHCUSCYhZ9cwaTd34JoGHqhofunmuB/view?usp=drivesdk",



    "NOM1222_2021-04-16.pdf": "https://drive.google.com/file/d/17dXEPv_S8lu3__OAHYAbfeRRupAR__r2/view?usp=drivesdk",



    "NOM1222_2021-12-24.pdf": "https://drive.google.com/file/d/1mnRHScckCu-rsW5Ei1ykpsyOrMRjmSuT/view?usp=drivesdk",



    "NOM1222_2021-09-03.pdf": "https://drive.google.com/file/d/1hQ-VhLA7groq-Krn2yadBCZrqJkJPlCG/view?usp=drivesdk",



    "NOM1222_2021-05-07.pdf": "https://drive.google.com/file/d/1iVD_oekzB0q6LAxfw7GOLfuoMq6R9k0B/view?usp=drivesdk",



    "NOM1222_2021-03-26.pdf": "https://drive.google.com/file/d/1e-LYDOv0lNV5OhjOqL_DwM27wsscJK5_/view?usp=drivesdk",



    "NOM1221_2021-08-27.pdf": "https://drive.google.com/file/d/10A2pzQCj_IcK7pZJl5DCPppnsPR1FvMt/view?usp=drivesdk",



    "NOM1221_2021-05-07.pdf": "https://drive.google.com/file/d/10Nz10Mt99qnpSr6EDxhIg86Ssl6YyVTF/view?usp=drivesdk",



    "NOM1222_2021-06-25.pdf": "https://drive.google.com/file/d/1GumtBdywSxg0de48hMo7MJCg6NgMJy_z/view?usp=drivesdk",



    "NOM1222_2021-09-24.pdf": "https://drive.google.com/file/d/1KiHs3rnBDA7P40yLu2A2DpQWPreyg5C_/view?usp=drivesdk",



    "NOM1221_2021-07-02.pdf": "https://drive.google.com/file/d/1N7H7TaI-N-pKDo5UvsNCbDt7QQcS9ydN/view?usp=drivesdk",



    "NOM1222_2021-04-02.pdf": "https://drive.google.com/file/d/1i8KGOPBq5BYxD4Ta3_IKnatQDI9Hlmvi/view?usp=drivesdk",



    "NOM1222_2021-06-04.pdf": "https://drive.google.com/file/d/122PtVWaNaans1CEHmlGeQaZODrPrakkz/view?usp=drivesdk",



    "NOM1221_2021-07-16.pdf": "https://drive.google.com/file/d/1yACe7_6ORZ8agwMeNYU3k__BqMiksdBy/view?usp=drivesdk",



    "NOM1221_2021-01-08.pdf": "https://drive.google.com/file/d/1VR7HFkSbwr_RQo3TxnHrxMq8Q1lTeMbc/view?usp=drivesdk",



    "NOM1221_2021-12-24.pdf": "https://drive.google.com/file/d/1MHePsOlspmB-vHF5v3ISP6z0zmVD7jsb/view?usp=drivesdk",



    "NOM1221_2021-01-01.pdf": "https://drive.google.com/file/d/1MsRkEC66DSwr7aZRUriRQDWRqfvlsyx4/view?usp=drivesdk",



    "NOM1221_2021-10-15.pdf": "https://drive.google.com/file/d/1dk2Z0Wt7WxM2PmtaCWmQyMoyR_t4PUne/view?usp=drivesdk",



    "NOM1222_2021-07-23.pdf": "https://drive.google.com/file/d/1LRy2vk-6Z_4aK4jAJflOtcQbVHHQd4qy/view?usp=drivesdk",



    "NOM1221_2021-02-19.pdf": "https://drive.google.com/file/d/1kA825Ua9cELNg7D0ZD7bs_9Nt-inJYVu/view?usp=drivesdk",



    "NOM1222_2021-02-19.pdf": "https://drive.google.com/file/d/15P_YuOarPAJYiaumXi__uhhmBGtxTVVQ/view?usp=drivesdk",



    "NOM1221_2021-01-29.pdf": "https://drive.google.com/file/d/14HQZHtWDSHWn80NNqK2txPlf6wErW5OL/view?usp=drivesdk",



    "NOM1222_2021-05-28.pdf": "https://drive.google.com/file/d/12lWiCHrF6cQi3BL0PGxrtijHi576R2Hk/view?usp=drivesdk",



    "NOM1222_2021-11-19.pdf": "https://drive.google.com/file/d/1sVVnZ7WJLSOW_vp_aG70af76kUHhq698/view?usp=drivesdk",



    "NOM1222_2021-07-30.pdf": "https://drive.google.com/file/d/1adgaWb8FJjYU87aB9h-DMZ8c-E4lQYe2/view?usp=drivesdk",



    "NOM1221_2021-06-11.pdf": "https://drive.google.com/file/d/1KZIElsyIMYNoKBjYwHx0Sajca8NMoV06/view?usp=drivesdk",



    "NOM1222_2021-08-06.pdf": "https://drive.google.com/file/d/13dAWaSRfhLbxtA9IEusk5IcNjw1_JPAz/view?usp=drivesdk",



    "NOM1221_2021-04-30.pdf": "https://drive.google.com/file/d/1Yuqbwf43qsxgIS-Ws5pU9VXRb5v4jrRn/view?usp=drivesdk",



    "NOM1222_2021-11-12.pdf": "https://drive.google.com/file/d/1fi2_27nVQpuc0rycPWgm0zTK3zLNxmDE/view?usp=drivesdk",



    "NOM1221_2021-07-23.pdf": "https://drive.google.com/file/d/1-aPW8yBaX0U3oKIOPNGTP-QwKN5G2Yvj/view?usp=drivesdk",



    "NOM1221_2021-02-26.pdf": "https://drive.google.com/file/d/18gbyTvh7LjvMGsVE1_g6qN1cFMekWt8d/view?usp=drivesdk",



    "NOM1221_2021-08-13.pdf": "https://drive.google.com/file/d/1DV3z1JTSWHYihDYs7tq3Mcfq4vnRQ2mS/view?usp=drivesdk",



    "NOM1222_2021-07-09.pdf": "https://drive.google.com/file/d/1gSOC-g-op48lvoAViLt5SVxvhoKQ7Zd7/view?usp=drivesdk",

    }


    # files = list(get_files(s, location='pdf_files/2021'))
    files = list(get_files(s, location=str('pdf_files/'+year)))
    for file in files:
        pdf_filename = file.split('/')[2] # pdf_files/2021/NOM1221_2021-07-23.pdf
        # return Response({"pdf_file": pdf_filename})
        pdf_dataname = pdf_filename.split('_')
        employee_data = pdf_dataname[0]
        code_employee = employee_data.split('NOM')[1]
        data_pdf = pdf_dataname[1]
        date_pdf = data_pdf.split('.pdf')[0]
            
        user = CustomUser.objects.get(code_employee=code_employee)
        Payroll.objects.create(
            user = user,
            payment_date = date_pdf,
            payroll_filename = pdf_filename,
            file_link = link_files[pdf_filename]
        )

    return Response({
        # "code_employee": code_employee,
        # "user": serializer.data,
        # "user_id": user.id,
        # "date": date_pdf,
        # "pdf_filename": pdf_filename
        "msg": "Registros realizados"
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_payrolls(request):
    token_request = request.headers.get("token", None)
    if token_request is not None:
        # token = Token.objects.get(key=token_request)
        token = Token.objects.filter(key=token_request).first()
        if token:
            log_user = CustomUser.objects.filter(auth_token=token).first()
            year = request.data.get("year", None)
            month = request.data.get("month", None)

            if year is None and month is None:
                return Response({"error":"Se requiere mes y/o año"}, status=400)
            
            if year is not None and month is not None:
                    payrolls = Payroll.objects.filter(payment_date__year=year, payment_date__month=month, user=log_user.id)
                    serializer = PayrollSerializer(payrolls, many=True)
                    return Response({"payroll": serializer.data, "year": year, "month": month})
            
            if year is not None and month is None:
                payrolls = Payroll.objects.filter(payment_date__year=year, user=log_user.id)
                serializer = PayrollSerializer(payrolls, many=True)
                return Response({"payroll": serializer.data, "year": year})

            if year is None and month is not None:
                    payrolls = Payroll.objects.filter(payment_date__month=month, user=log_user.id)
                    serializer = PayrollSerializer(payrolls, many=True)
                    return Response({"payroll": serializer.data, "month": month})

        return Response({"error":"Token inexistente"}, status=400)   
    return Response({"error":"Token no encontrado"}, status=400)   
             

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def download_payroll(request):
    file_name = request.data.get('payroll_filename', None)
    payroll = Payroll.objects.filter(payroll_filename=file_name)
    return Response({"file_link": payroll.file_link})

    # date_pdf = file_name.split('_')[1].split('.pdf')[0]
    # year_folder = date_pdf.split('-')[0]
    
    # path = os.path.join(settings.STATIC_ROOT, 'pdf_files')
    # for directory_name, directory, files in os.walk(path):
    #     # directory_name = directory_name.replace(str('C:\\Users\\HP\\Documents\\My_files\\LoopGK\\Syncronik_Internship\\projects\\nomina_app_resetpassword_updated\\nomina_app\\core\\staticfiles\\pdf_files' + '\\' + year_folder), str('fa.syncronik.com'+'/'+year_folder))
    #     for file_ in files:
    #         if file_ == file_name:
    #             return Response({"file": str(directory_name + '/' + file_)}, status=200)
    # return Response({"msg": "Archivo no encontrado"}, status=400)
    

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def detail_payroll(request):
    file_name = request.data.get('payroll_filename', None)
    payroll = Payroll.objects.filter(payroll_filename=file_name)
    return Response({"file_link": payroll.file_link})
    # date_pdf = file_name.split('_')[1].split('.pdf')[0]
    # year_folder = date_pdf.split('-')[0]
    
    # path = os.path.join(settings.STATIC_ROOT, 'pdf_files')
    # for directory_name, directory, files in os.walk(path):
    #     # directory_name = directory_name.replace(str('C:\\Users\\HP\\Documents\\My_files\\LoopGK\\Syncronik_Internship\\projects\\nomina_app_resetpassword_updated\\nomina_app\\core\\staticfiles\\pdf_files' + '\\' + year_folder), str('fa.syncronik.com'+'/'+year_folder))
    #     for file_ in files:
    #         if file_ == file_name:
    #             return Response({"file": str(directory_name + '/' + file_)}, status=200)
    # return Response({"msg": "Archivo no encontrado"}, status=400)
    
