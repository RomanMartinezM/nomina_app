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

    # link_files = {

    # "NOM1222_2021-01-01.pdf": "https://drive.google.com/file/d/16fqMX4hjQgJfIgENSJx8RD0j6TYkagH1/view?usp=drivesdk",

    # "NOM1221_2021-12-10.pdf": "https://drive.google.com/file/d/18L87LrguUdxoi8UacKEn7EJDYx5bt_jP/view?usp=drivesdk",

    # "NOM1221_2021-10-22.pdf": "https://drive.google.com/file/d/1IfCF4S761QJnjx4b3aEIFnvE-qrDoLjY/view?usp=drivesdk",


    # "NOM1222_2021-06-11.pdf": "https://drive.google.com/file/d/1Kl83pycg0gSUT4Qmqvspg1Ve5fFKdk7T/view?usp=drivesdk",



    # "NOM1222_2021-10-08.pdf": "https://drive.google.com/file/d/13OZDvvG4B_AN-UeBhZIfkPo3rARxfqqy/view?usp=drivesdk",



    # "NOM1222_2021-01-29.pdf": "https://drive.google.com/file/d/1JiTedIS9g-ErN7fOHJBqbSwQm7GDIWqe/view?usp=drivesdk",



    # "NOM1221_2021-03-19.pdf": "https://drive.google.com/file/d/1nw1RH05eXUJVDox2I9--Y_F2L8pMhm15/view?usp=drivesdk",



    # "NOM1221_2021-05-14.pdf": "https://drive.google.com/file/d/1CVNrCs3N2kWbpNZzTkYdJUs38OI8kbnt/view?usp=drivesdk",



    # "NOM1221_2021-01-15.pdf": "https://drive.google.com/file/d/1UUAVdhtsa-5XGBofS1IJvGjtPWPxwavM/view?usp=drivesdk",


    # "NOM1221_2021-12-17.pdf": "https://drive.google.com/file/d/1-3ALdtlMddm1fGh4M9hVS1AzziKs-WEl/view?usp=drivesdk",



    # "NOM1221_2021-08-20.pdf": "https://drive.google.com/file/d/1iw7KjJ3Lsf2FIuFTqz6cSzOzPF483Ckj/view?usp=drivesdk",



    # "NOM1222_2021-01-08.pdf": "https://drive.google.com/file/d/1LOAbwwVTBh9GfLycZWtZjWyrIq3S86w0/view?usp=drivesdk",



    # "NOM1221_2021-09-17.pdf": "https://drive.google.com/file/d/1O4BAS6k19jj3tGsFO28_IRhQ8Wn4gsGC/view?usp=drivesdk",



    # "NOM1221_2021-03-12.pdf": "https://drive.google.com/file/d/18oXCXTZq-Dv32e534qz80-zqqPPb81tr/view?usp=drivesdk",



    # "NOM1222_2021-07-16.pdf": "https://drive.google.com/file/d/1Tm29LIUshXmWMNy1YQRCK7KhA-1A11sX/view?usp=drivesdk",



    # "NOM1222_2021-10-29.pdf": "https://drive.google.com/file/d/1w6M62xExOZt3Oau23EzMsNZdBJ_tCtnl/view?usp=drivesdk",



    # "NOM1222_2021-11-05.pdf": "https://drive.google.com/file/d/1OcL37ECm98z7cQibaucAA5w5YukmpCe8/view?usp=drivesdk",



    # "NOM1222_2021-01-22.pdf": "https://drive.google.com/file/d/1EpSLstuj0hs63Bu3BTzj9wgB1JvnNWA6/view?usp=drivesdk",


    # "NOM1222_2021-04-30.pdf": "https://drive.google.com/file/d/1DMe3Vg36vL6CBBrHIAp0j1NvZsXufq3H/view?usp=drivesdk",



    # "NOM1221_2021-07-09.pdf": "https://drive.google.com/file/d/1k0dt0djforQMiStubE5faIDnh3k41Y4a/view?usp=drivesdk",



    # "NOM1222_2021-05-21.pdf": "https://drive.google.com/file/d/1p5nD1v3MpT8DwY9_-UBKsi_UjIPATjtO/view?usp=drivesdk",



    # "NOM1221_2021-06-18.pdf": "https://drive.google.com/file/d/1IMZdPfHvUqZIjsAANQUz5XVqdyQbAgfm/view?usp=drivesdk",



    # "NOM1221_2021-04-16.pdf": "https://drive.google.com/file/d/1no6t4c-DVtTbM2x1OXzdEhbTy1i4DSFc/view?usp=drivesdk",



    # "NOM1222_2021-11-26.pdf": "https://drive.google.com/file/d/1QCzU98ZLeHKWP6AnelRpW2Nti6hHtYzm/view?usp=drivesdk",



    # "NOM1222_2021-03-19.pdf": "https://drive.google.com/file/d/15tfKGmJyMRTSb50lShE7iCmQArou_NRc/view?usp=drivesdk",



    # "NOM1221_2021-11-19.pdf": "https://drive.google.com/file/d/1JiYtns2ckd9CpvkrMzNsNz063dPBUtNa/view?usp=drivesdk",



    # "NOM1221_2021-10-08.pdf": "https://drive.google.com/file/d/1iyb1RZEvTxtwv12zRqNZi2oQStoxLset/view?usp=drivesdk",



    # "NOM1221_2021-06-04.pdf": "https://drive.google.com/file/d/1Sa7m5Jop30lIa-egrIx4ADsnz0qLbpcV/view?usp=drivesdk",



    # "NOM1222_2021-03-05.pdf": "https://drive.google.com/file/d/10FsXY8BAu9uzdLyrnF3y_HHMUWP0WQe_/view?usp=drivesdk",



    # "NOM1222_2021-10-22.pdf": "https://drive.google.com/file/d/1P8D2NwFyvr2sq0wG8poOUY0mSYtOcKEO/view?usp=drivesdk",



    # "NOM1222_2021-06-18.pdf": "https://drive.google.com/file/d/1y6wx9aVvY0V35BcxuD50lW0D2i4MgFBD/view?usp=drivesdk",



    # "NOM1222_2021-05-14.pdf": "https://drive.google.com/file/d/1JGKhTCI_6RviGvUAfHerTekqXKsLKF5v/view?usp=drivesdk",



    # "NOM1221_2021-05-21.pdf": "https://drive.google.com/file/d/1auZCt-wF34Kjj0YvJ2PRJLfFCnr8RckG/view?usp=drivesdk",



    # "NOM1222_2021-02-12.pdf": "https://drive.google.com/file/d/1k_O1_RQ7SOevARgJzSNZ1Pt4DeIfZl1-/view?usp=drivesdk",



    # "NOM1222_2021-12-17.pdf": "https://drive.google.com/file/d/1pEaCcZLBlJ2uQbTgnbHoha-uR1omYtS8/view?usp=drivesdk",



    # "NOM1222_2021-01-15.pdf": "https://drive.google.com/file/d/1vDX-8yNChDxubkO9mvMRWGx_21lJWPkL/view?usp=drivesdk",



    # "NOM1221_2021-04-09.pdf": "https://drive.google.com/file/d/1CSqVJ1P3cz4LNBE4Lnw9igZQNhV6zFU9/view?usp=drivesdk",



    # "NOM1222_2021-09-10.pdf": "https://drive.google.com/file/d/13yA1XFf4nI-oOyCdpyki98oND1ljyE6r/view?usp=drivesdk",



    # "NOM1221_2021-04-23.pdf": "https://drive.google.com/file/d/19HqmP5D7Kog9VkJ68tVvSolhdAptqoSi/view?usp=drivesdk",



    # "NOM1222_2021-04-23.pdf": "https://drive.google.com/file/d/162t-8V7pLoWhuJUQfD-T1nIvg6USd_WY/view?usp=drivesdk",



    # "NOM1221_2021-11-26.pdf": "https://drive.google.com/file/d/1Qr2Z8t260HWglaTvQ8yEs_-GI8Bvi47a/view?usp=drivesdk",



    # "NOM1221_2021-09-24.pdf": "https://drive.google.com/file/d/1G6-pG6lwPlOmjlCdz1Xk3l8i7yF7vURZ/view?usp=drivesdk",



    # "NOM1222_2021-04-09.pdf": "https://drive.google.com/file/d/1K4jHXJt02YPWZP6r3hsUVL8AEec0Vj5B/view?usp=drivesdk",



    # "NOM1222_2021-02-05.pdf": "https://drive.google.com/file/d/1w-OzNON4Vrl40hfz14O9zAHE_TSLqVbq/view?usp=drivesdk",



    # "NOM1221_2021-10-29.pdf": "https://drive.google.com/file/d/14nTkGFjWFsW52Yb9KZKgonsemcfpDE4n/view?usp=drivesdk",



    # "NOM1221_2021-08-06.pdf": "https://drive.google.com/file/d/12ck3P6SMMyy7oV-bu0bl7ZILhtSbKfJ7/view?usp=drivesdk",



    # "NOM1221_2021-03-05.pdf": "https://drive.google.com/file/d/1LUCYmJKwR3iErMCW6goyLRCXX98oBbRv/view?usp=drivesdk",



    # "NOM1221_2021-09-03.pdf": "https://drive.google.com/file/d/1qx3OFNV0izlnPmyxsj8kSSGBa41Xxhak/view?usp=drivesdk",



    # "NOM1221_2021-02-05.pdf": "https://drive.google.com/file/d/17m6uIU6mBloT1I8cZ5lrojX19f39hX5l/view?usp=drivesdk",



    # "NOM1221_2021-12-03.pdf": "https://drive.google.com/file/d/1rxnSFu2xNy5_R_c1260CJRCB33IhryhR/view?usp=drivesdk",



    # "NOM1221_2021-11-05.pdf": "https://drive.google.com/file/d/1unOWtiOZh2hUqUiL1TIQnH4KeKElDCRi/view?usp=drivesdk",



    # "NOM1221_2021-04-02.pdf": "https://drive.google.com/file/d/1EKmyYpWMpx0s4pEwS05GB7GsiVEzAA_Y/view?usp=drivesdk",



    # "NOM1221_2021-07-30.pdf": "https://drive.google.com/file/d/1p-WkgElvaJwdKxgh0KjbUmCAbkhTSrlM/view?usp=drivesdk",



    # "NOM1222_2021-08-13.pdf": "https://drive.google.com/file/d/1JA3m8WpqNOz8mspdkyU2Nzfo6u5SHGPV/view?usp=drivesdk",



    # "NOM1222_2021-12-10.pdf": "https://drive.google.com/file/d/1LI3dLqM_fH2tXAWxp6HfU-9n9wf1ds2M/view?usp=drivesdk",



    # "NOM1221_2021-10-01.pdf": "https://drive.google.com/file/d/1Vj8lCo4wARJ0l1na6Amoz2_U4yZjlYBR/view?usp=drivesdk",



    # "NOM1221_2021-06-25.pdf": "https://drive.google.com/file/d/15SqkXkjCBZWvuOyWYRbzdckegk2XZn7f/view?usp=drivesdk",



    # "NOM1222_2021-08-20.pdf": "https://drive.google.com/file/d/1BGGx8pN92IG0NskXAFA57nR1FLq59Z_h/view?usp=drivesdk",



    # "NOM1222_2021-09-17.pdf": "https://drive.google.com/file/d/1n-s4cGhCFyACkf5KlCxybPDlboZD_Bf4/view?usp=drivesdk",



    # "NOM1221_2021-03-26.pdf": "https://drive.google.com/file/d/1r9wmf8Gg2jSUNenorRckDMgS7JpNFK9D/view?usp=drivesdk",



    # "NOM1221_2021-05-28.pdf": "https://drive.google.com/file/d/1bY4r2lNLv7NnIf0pzOwpPgu_CvDxMhck/view?usp=drivesdk",



    # "NOM1222_2021-10-01.pdf": "https://drive.google.com/file/d/1zlqZkfZvvdlWoXjT82VINP4u8ojv9ViI/view?usp=drivesdk",



    # "NOM1221_2021-09-10.pdf": "https://drive.google.com/file/d/1Q4X4ggNXM6x1SyzhPZLXg5_ByFxYO6MP/view?usp=drivesdk",



    # "NOM1222_2021-08-27.pdf": "https://drive.google.com/file/d/1wCyO6Zn90qmd_AEZwBA4EVfZKZwoSQ9l/view?usp=drivesdk",



    # "NOM1221_2021-01-22.pdf": "https://drive.google.com/file/d/1P7Q7YNEVPNs0IC_csUUmmMVcLWN9RBBi/view?usp=drivesdk",



    # "NOM1222_2021-07-02.pdf": "https://drive.google.com/file/d/1dY8Dizji3UD-FUNKw7iaDmCz3d2ENZOb/view?usp=drivesdk",



    # "NOM1222_2021-02-26.pdf": "https://drive.google.com/file/d/10S6DRjiOUYeFnpGa6DoNuOxg1TwmVAiL/view?usp=drivesdk",



    # "NOM1221_2021-02-12.pdf": "https://drive.google.com/file/d/1kmJNJtcFC0ncz2o_hmD8KP-9QDASuwtV/view?usp=drivesdk",



    # "NOM1222_2021-10-15.pdf": "https://drive.google.com/file/d/1vV6AlLmP2b2jn6T9xkF1yDdLRUVK8ADa/view?usp=drivesdk",



    # "NOM1222_2021-03-12.pdf": "https://drive.google.com/file/d/1HZGn-gLTul5dTte725zJUvvii3z-y2Ea/view?usp=drivesdk",



    # "NOM1222_2021-12-03.pdf": "https://drive.google.com/file/d/1kUZhnX6VE2-TKj8opoI2rvhIEKvfKQOp/view?usp=drivesdk",



    # "NOM1221_2021-11-12.pdf": "https://drive.google.com/file/d/1ubCHCUSCYhZ9cwaTd34JoGHqhofunmuB/view?usp=drivesdk",



    # "NOM1222_2021-04-16.pdf": "https://drive.google.com/file/d/17dXEPv_S8lu3__OAHYAbfeRRupAR__r2/view?usp=drivesdk",



    # "NOM1222_2021-12-24.pdf": "https://drive.google.com/file/d/1mnRHScckCu-rsW5Ei1ykpsyOrMRjmSuT/view?usp=drivesdk",



    # "NOM1222_2021-09-03.pdf": "https://drive.google.com/file/d/1hQ-VhLA7groq-Krn2yadBCZrqJkJPlCG/view?usp=drivesdk",



    # "NOM1222_2021-05-07.pdf": "https://drive.google.com/file/d/1iVD_oekzB0q6LAxfw7GOLfuoMq6R9k0B/view?usp=drivesdk",



    # "NOM1222_2021-03-26.pdf": "https://drive.google.com/file/d/1e-LYDOv0lNV5OhjOqL_DwM27wsscJK5_/view?usp=drivesdk",



    # "NOM1221_2021-08-27.pdf": "https://drive.google.com/file/d/10A2pzQCj_IcK7pZJl5DCPppnsPR1FvMt/view?usp=drivesdk",



    # "NOM1221_2021-05-07.pdf": "https://drive.google.com/file/d/10Nz10Mt99qnpSr6EDxhIg86Ssl6YyVTF/view?usp=drivesdk",



    # "NOM1222_2021-06-25.pdf": "https://drive.google.com/file/d/1GumtBdywSxg0de48hMo7MJCg6NgMJy_z/view?usp=drivesdk",



    # "NOM1222_2021-09-24.pdf": "https://drive.google.com/file/d/1KiHs3rnBDA7P40yLu2A2DpQWPreyg5C_/view?usp=drivesdk",



    # "NOM1221_2021-07-02.pdf": "https://drive.google.com/file/d/1N7H7TaI-N-pKDo5UvsNCbDt7QQcS9ydN/view?usp=drivesdk",



    # "NOM1222_2021-04-02.pdf": "https://drive.google.com/file/d/1i8KGOPBq5BYxD4Ta3_IKnatQDI9Hlmvi/view?usp=drivesdk",



    # "NOM1222_2021-06-04.pdf": "https://drive.google.com/file/d/122PtVWaNaans1CEHmlGeQaZODrPrakkz/view?usp=drivesdk",



    # "NOM1221_2021-07-16.pdf": "https://drive.google.com/file/d/1yACe7_6ORZ8agwMeNYU3k__BqMiksdBy/view?usp=drivesdk",



    # "NOM1221_2021-01-08.pdf": "https://drive.google.com/file/d/1VR7HFkSbwr_RQo3TxnHrxMq8Q1lTeMbc/view?usp=drivesdk",



    # "NOM1221_2021-12-24.pdf": "https://drive.google.com/file/d/1MHePsOlspmB-vHF5v3ISP6z0zmVD7jsb/view?usp=drivesdk",



    # "NOM1221_2021-01-01.pdf": "https://drive.google.com/file/d/1MsRkEC66DSwr7aZRUriRQDWRqfvlsyx4/view?usp=drivesdk",



    # "NOM1221_2021-10-15.pdf": "https://drive.google.com/file/d/1dk2Z0Wt7WxM2PmtaCWmQyMoyR_t4PUne/view?usp=drivesdk",



    # "NOM1222_2021-07-23.pdf": "https://drive.google.com/file/d/1LRy2vk-6Z_4aK4jAJflOtcQbVHHQd4qy/view?usp=drivesdk",



    # "NOM1221_2021-02-19.pdf": "https://drive.google.com/file/d/1kA825Ua9cELNg7D0ZD7bs_9Nt-inJYVu/view?usp=drivesdk",



    # "NOM1222_2021-02-19.pdf": "https://drive.google.com/file/d/15P_YuOarPAJYiaumXi__uhhmBGtxTVVQ/view?usp=drivesdk",



    # "NOM1221_2021-01-29.pdf": "https://drive.google.com/file/d/14HQZHtWDSHWn80NNqK2txPlf6wErW5OL/view?usp=drivesdk",



    # "NOM1222_2021-05-28.pdf": "https://drive.google.com/file/d/12lWiCHrF6cQi3BL0PGxrtijHi576R2Hk/view?usp=drivesdk",



    # "NOM1222_2021-11-19.pdf": "https://drive.google.com/file/d/1sVVnZ7WJLSOW_vp_aG70af76kUHhq698/view?usp=drivesdk",



    # "NOM1222_2021-07-30.pdf": "https://drive.google.com/file/d/1adgaWb8FJjYU87aB9h-DMZ8c-E4lQYe2/view?usp=drivesdk",



    # "NOM1221_2021-06-11.pdf": "https://drive.google.com/file/d/1KZIElsyIMYNoKBjYwHx0Sajca8NMoV06/view?usp=drivesdk",



    # "NOM1222_2021-08-06.pdf": "https://drive.google.com/file/d/13dAWaSRfhLbxtA9IEusk5IcNjw1_JPAz/view?usp=drivesdk",



    # "NOM1221_2021-04-30.pdf": "https://drive.google.com/file/d/1Yuqbwf43qsxgIS-Ws5pU9VXRb5v4jrRn/view?usp=drivesdk",



    # "NOM1222_2021-11-12.pdf": "https://drive.google.com/file/d/1fi2_27nVQpuc0rycPWgm0zTK3zLNxmDE/view?usp=drivesdk",



    # "NOM1221_2021-07-23.pdf": "https://drive.google.com/file/d/1-aPW8yBaX0U3oKIOPNGTP-QwKN5G2Yvj/view?usp=drivesdk",



    # "NOM1221_2021-02-26.pdf": "https://drive.google.com/file/d/18gbyTvh7LjvMGsVE1_g6qN1cFMekWt8d/view?usp=drivesdk",



    # "NOM1221_2021-08-13.pdf": "https://drive.google.com/file/d/1DV3z1JTSWHYihDYs7tq3Mcfq4vnRQ2mS/view?usp=drivesdk",



    # "NOM1222_2021-07-09.pdf": "https://drive.google.com/file/d/1gSOC-g-op48lvoAViLt5SVxvhoKQ7Zd7/view?usp=drivesdk",

    # }

    link_files = {
    "NOM1221_2022-01-01.pdf": 
    "https://drive.google.com/file/d/1FtJRiMeKCjbNnJBqfkD2tP3dH0G0G1cx/view?usp=share_link",   

    "NOM1221_2022-01-08.pdf":
    "https://drive.google.com/file/d/1cFd0qrguSKoVnZY3TnHgRGT0zTskh-k7/view?usp=share_link",


    "NOM1221_2022-01-15.pdf":
    "https://drive.google.com/file/d/15oC5jZqZHv70fnME31-6yi3EDl99Kyzz/view?usp=share_link",


    "NOM1221_2022-01-22.pdf":
    "https://drive.google.com/file/d/1dY2z-aPCms_5Wt5gRsHn1_8PtqMaqarU/view?usp=share_link",


    "NOM1221_2022-01-29.pdf":
    "https://drive.google.com/file/d/1boiVvpyLCMHBZfNI28Slgtp5hKVQb-Iw/view?usp=share_link",


    "NOM1221_2022-02-05.pdf":
    "https://drive.google.com/file/d/1J-N-c8GSEpXjCr5CXA227EdO6P7lQk61/view?usp=share_link",

    "NOM1221_2022-02-12.pdf":
    "https://drive.google.com/file/d/1i2J_4F9YBwB2DChHJCDZscyghQX6iZ_n/view?usp=share_link",

    "NOM1221_2022-02-19.pdf":
    "https://drive.google.com/file/d/1ILs08Z-ZEqB6TCiPTIU84vbePjOz-og2/view?usp=share_link",

    "NOM1221_2022-02-26.pdf":
    "https://drive.google.com/file/d/1p1a2QHgBPVjYu8i5zu9bRfxB2MRjDTsY/view?usp=share_link",

    "NOM1221_2022-03-05.pdf":
    "https://drive.google.com/file/d/12BuFHOd3AHBs22QZpBSOy-KLN7o5v_03/view?usp=share_link",

    "NOM1221_2022-03-12.pdf":
    "https://drive.google.com/file/d/1MtLTZC5iSD5D26MZta4ggi_TeWqYu4zi/view?usp=share_link",

    "NOM1221_2022-03-19.pdf":
    "https://drive.google.com/file/d/110vVyLhmAb7NW4Ch52gjOnjul4-cNDS_/view?usp=share_link",

    "NOM1221_2022-03-26.pdf":
    "https://drive.google.com/file/d/1EIK__M1v7atBLV8nm9y-Weh1BbzomOck/view?usp=share_link",

    "NOM1221_2022-04-02.pdf":
    "https://drive.google.com/file/d/1gtKOLn2vwxhFilKodJJ6hRvzEA6SKUHK/view?usp=share_link",

    "NOM1221_2022-04-09.pdf":
    "https://drive.google.com/file/d/1eKbQ4QanhzZNEZkasgnHpvFxUc_BrOK9/view?usp=share_link",

    "NOM1221_2022-04-16.pdf":
    "https://drive.google.com/file/d/19wZ5bYCxlfXW5AdNeDNEEyvZcaYMTNiH/view?usp=share_link",

    "NOM1221_2022-04-23.pdf":
    "https://drive.google.com/file/d/1yPTOzyDi1Kcjlclf4E5n6w6MTmXntTk7/view?usp=share_link",

    "NOM1221_2022-04-30.pdf":
    "https://drive.google.com/file/d/1FUPFrc_gOX2skfx5Dw6UcHMP5-cAp0j0/view?usp=share_link",

    "NOM1221_2022-05-07.pdf":
    "https://drive.google.com/file/d/1wVpl5PXH1nUlkVs7SctwW9x2Z3JpeNi5/view?usp=share_link",

    "NOM1221_2022-05-14.pdf":
    "https://drive.google.com/file/d/1HRdPOmTn1bGnFzxsq-ni98DYgwLmPMee/view?usp=share_link",

    "NOM1221_2022-05-21.pdf":
    "https://drive.google.com/file/d/12PYlQ79PRqLm_QDF8EJp7CwAIOgDljdu/view?usp=share_link",

    "NOM1221_2022-05-28.pdf":
    "https://drive.google.com/file/d/1FaJ8NlTwIrEawC2_OpnUIY9SvY17zgx8/view?usp=share_link",

    "NOM1221_2022-06-04.pdf":
    "https://drive.google.com/file/d/1IidA2WsCUdg11BpZMlJlNady0HsNyrha/view?usp=share_link",

    "NOM1221_2022-06-11.pdf":
    "https://drive.google.com/file/d/1FbXZ7y1Ihuf65pnFc5IHt7ct0l_OYlU8/view?usp=share_link",

    "NOM1221_2022-06-18.pdf":
    "https://drive.google.com/file/d/1JLOUflZB0xVdw_VhSl5duWiE8chbxSL3/view?usp=share_link",

    "NOM1221_2022-06-25.pdf":
    "https://drive.google.com/file/d/1Bjl58pijzJlVrxh2hQiHDDyjfzZfLtcg/view?usp=share_link",

    "NOM1221_2022-07-02.pdf":
    "https://drive.google.com/file/d/1q1ljCWO0TtO4eF0WJYaYMwjViyJbKS6K/view?usp=share_link",

    "NOM1221_2022-07-09.pdf":
    "https://drive.google.com/file/d/1X1cvHu7zv6DutpOXTjhtDaPJ5fkwZpaO/view?usp=share_link",

    "NOM1221_2022-07-16.pdf":
    "https://drive.google.com/file/d/1HPaj-6xTvUQvQHZ4r5i6__HmUX4O-wFV/view?usp=share_link",

    "NOM1221_2022-07-23.pdf":
    "https://drive.google.com/file/d/1IM3IDWAEoclWMiXUYzbtyypneyAKPcW_/view?usp=share_link",

    "NOM1221_2022-07-30.pdf":
    "https://drive.google.com/file/d/1FicjG1MCb9XqsDN0A2wM5NE6uhotiqFq/view?usp=share_link",

    "NOM1221_2022-08-06.pdf":
    "https://drive.google.com/file/d/1alXrlWhq4bBKN_br_j33Bm5_LenKF74y/view?usp=share_link",

    "NOM1221_2022-08-13.pdf":
    "https://drive.google.com/file/d/14kqOBZTskKg_C4L0HiTgoyOxKDsJ9vWJ/view?usp=share_link",

    "NOM1221_2022-08-20.pdf":
    "https://drive.google.com/file/d/1xtxXN35O1vei1NKdUJb4IPs3xvxUL_PY/view?usp=share_link",

    "NOM1221_2022-08-27.pdf":
    "https://drive.google.com/file/d/1CdfTAeiy7LIH74LpIL4kyDBHIoWZc4G9/view?usp=share_link",

    "NOM1221_2022-09-03.pdf":
    "https://drive.google.com/file/d/1XLlvIuXmUKvLCLRf1A4DWAzbxxWuiDpK/view?usp=share_link",

    "NOM1221_2022-09-10.pdf":
    "https://drive.google.com/file/d/1n35iMGIppTvTczr9BGaPYwJIdv2qQ_H0/view?usp=share_link",

    "NOM1221_2022-09-17.pdf":
    "https://drive.google.com/file/d/1Jt133fskjqcAp2Pw9x9kxoivpLBzsOr1/view?usp=share_link",

    "NOM1221_2022-09-24.pdf":
    "https://drive.google.com/file/d/1y2w7ugQvWnZDDog7g-dioFBvoQ1xoEG7/view?usp=share_link",

    "NOM1221_2022-10-01.pdf":
    "https://drive.google.com/file/d/11CbEP59ak9EOBicUhMj4QBKgDbJdD_wY/view?usp=share_link",

    "NOM1221_2022-10-08.pdf":
    "https://drive.google.com/file/d/1sx_v1shbnkubZxoMX4O3Mqxi_DP-UHkd/view?usp=share_link",

    "NOM1221_2022-10-15.pdf":
    "https://drive.google.com/file/d/1PCg30Ri2eHyB99rszarITkaKztju-Js9/view?usp=share_link",

    "NOM1221_2022-10-22.pdf":
    "https://drive.google.com/file/d/16QwSQmQp-xQmd60oN-fUAeZkjL1Bbyku/view?usp=share_link",

    "NOM1221_2022-10-29.pdf":
    "https://drive.google.com/file/d/1De6NyG4NqFm-2uYREP2e1cMa2Gh049to/view?usp=share_link",

    "NOM1221_2022-11-05.pdf":
    "https://drive.google.com/file/d/1FwG0I8MY56yHMx9yKEkgV6jH-LRfb49c/view?usp=share_link",

    "NOM1221_2022-11-12.pdf":
    "https://drive.google.com/file/d/1Claw1wve_lVtobKoMN_Nuw5j3U4jJbkd/view?usp=share_link",

    "NOM1221_2022-11-19.pdf":
    "https://drive.google.com/file/d/1zEOnoS2Oukw4ch0oXhhC0-nD9wgJE-2r/view?usp=share_link",

    "NOM1221_2022-11-26.pdf":
    "https://drive.google.com/file/d/1YOsBJBkQRMdnOW2bacnM9mu6oRjYZKsx/view?usp=share_link",

    "NOM1221_2022-12-03.pdf":
    "https://drive.google.com/file/d/1qJSMXDOHQge9KfW_njpYHy-d2gi0Ggpi/view?usp=share_link",

    "NOM1221_2022-12-10.pdf":
    "https://drive.google.com/file/d/1K6ZgK3wRkTJZtR1rU3uj3NV9y_ZJDsv6/view?usp=share_link",

    "NOM1221_2022-12-17.pdf":
    "https://drive.google.com/file/d/1fVeCehRixukIjJST62hGVd-uxZhOSupN/view?usp=share_link",

    "NOM1221_2022-12-24.pdf":
    "https://drive.google.com/file/d/18u8W9fWUYkPeVFHinqZ-3O1Od2vetMx3/view?usp=share_link",

    "NOM1222_2022-01-01.pdf":
    "https://drive.google.com/file/d/1kk0ovzQ_ElYBK_U2VaymrxzwrZDqHXiw/view?usp=share_link",

    "NOM1222_2022-01-08.pdf":
    "https://drive.google.com/file/d/1r7fTh_QgNr3-g4tAIqkGx2cV-opvru_5/view?usp=share_link",

    "NOM1222_2022-01-15.pdf":
    "https://drive.google.com/file/d/1t8k6_dDyGdlUlhLpbXt-G5XX68ehQNol/view?usp=share_link",

    "NOM1222_2022-01-22.pdf":
    "https://drive.google.com/file/d/1qJe0Ba_NvXXpzyaWBwzhtQoqJ-VnQauo/view?usp=share_link",

    "NOM1222_2022-01-29.pdf":
    "https://drive.google.com/file/d/1aNOaxCn6N9VMEMhDFOYrw33CUT_HCKBu/view?usp=share_link",

    "NOM1222_2022-02-05.pdf":
    "https://drive.google.com/file/d/1seU4S1ks4RqBylKx2WYBaIeYVko8Oyh-/view?usp=share_link",

    "NOM1222_2022-02-12.pdf":
    "https://drive.google.com/file/d/16O7776M-2701Kc25OhT3oRGv4_WJtNBd/view?usp=share_link",

    "NOM1222_2022-02-19.pdf":
    "https://drive.google.com/file/d/1qC7xQwy7H0vb4Aqj1Rhlc4pNqffM6ME_/view?usp=share_link",

    "NOM1222_2022-02-26.pdf":
    "https://drive.google.com/file/d/1RzWHNCArfI5fgVHTz2Eo5_OxsRMHizDB/view?usp=share_link",

    "NOM1222_2022-03-05.pdf":
    "https://drive.google.com/file/d/19hL9h7Dzz0AbTHaHnzXdGXzwpFXjx6j0/view?usp=share_link",

    "NOM1222_2022-03-12.pdf":
    "https://drive.google.com/file/d/1uI4KB_4nsY_nt5-_aoeqWrUOas0Ehe0-/view?usp=share_link",

    "NOM1222_2022-03-19.pdf":
    "https://drive.google.com/file/d/1N2KB6Ec7M-ZmUqGLMDvXYURJQfPCDoak/view?usp=share_link",

    "NOM1222_2022-03-26.pdf":
    "https://drive.google.com/file/d/1yFHkACbnR1s_5o0T0qZ9Rt8sMIafO3BW/view?usp=share_link",

    "NOM1222_2022-04-02.pdf":
    "https://drive.google.com/file/d/1ifhrg9pFSTV1v9nlD0rg4jksPzBwWB8b/view?usp=share_link",

    "NOM1222_2022-04-09.pdf":
    "https://drive.google.com/file/d/11T6i7wTRYew6ggxiGIYJ8kY1NannGX5X/view?usp=share_link",

    "NOM1222_2022-04-16.pdf":
    "https://drive.google.com/file/d/1HrwhNBass7RArO98mIXppgPXHXDBDWxx/view?usp=share_link",

    "NOM1222_2022-04-23.pdf":
    "https://drive.google.com/file/d/1rxCJ5UzAeqct1C4cYel4UgWpmXNxS3Uk/view?usp=share_link",

    "NOM1222_2022-04-30.pdf":
    "https://drive.google.com/file/d/1EKsbkK7_aiu0mvK7Cmky9CeRvef5e9bR/view?usp=share_link",

    "NOM1222_2022-05-07.pdf":
    "https://drive.google.com/file/d/1j1E9QAR_YEMcha1AyN0EXLpaMcJ7LfwT/view?usp=share_link",

    "NOM1222_2022-05-14.pdf":
    "https://drive.google.com/file/d/1V3RkUO26NR5BJkIxDHaqFC8E2cNAJLIc/view?usp=share_link",

    "NOM1222_2022-05-21.pdf":
    "https://drive.google.com/file/d/1MgHFTvPe8BTgv_g69280ClafDgOg6jkQ/view?usp=share_link",

    "NOM1222_2022-05-28.pdf":
    "https://drive.google.com/file/d/1mJ7tD2KpqP5OuvoatardIf4jHbnw14cB/view?usp=share_link",

    "NOM1222_2022-06-04.pdf":
    "https://drive.google.com/file/d/1Ovb3Y3P-_3TgtoXwvJs_tK54rWLISHB7/view?usp=share_link",

    "NOM1222_2022-06-11.pdf":
    "https://drive.google.com/file/d/1JYsJnxsXRHh8pZRlXexEGUSo8RJCS9wn/view?usp=share_link",

    "NOM1222_2022-06-18.pdf":
    "https://drive.google.com/file/d/1ra-qYv91QxqqLglRdMY9nSwcOArjhpwB/view?usp=share_link",

    "NOM1222_2022-06-25.pdf":
    "https://drive.google.com/file/d/19mJcPdN-JYiRKGglJovgbKbtnnj04a2G/view?usp=share_link",

    "NOM1222_2022-07-02.pdf":
    "https://drive.google.com/file/d/1WO2VTkTS8WHnmsgEeQrbYHxp-HGsV7Yl/view?usp=share_link",

    "NOM1222_2022-07-09.pdf":
    "https://drive.google.com/file/d/1-tOeofggxZK41LgTcHPyxx28tOOkVcSx/view?usp=share_link",

    "NOM1222_2022-07-16.pdf":
    "https://drive.google.com/file/d/1DbLZaJqcY2rfVomApZkWBNZ5B587Bnq8/view?usp=share_link",

    "NOM1222_2022-07-23.pdf":
    "https://drive.google.com/file/d/1I-twsAAbMYTzY-RcpCfdak321MarzSY_/view?usp=share_link",

    "NOM1222_2022-07-30.pdf":
    "https://drive.google.com/file/d/1JD16xl2VkrSU3OpToNce--I4AuWL5q6W/view?usp=share_link",

    "NOM1222_2022-08-06.pdf":
    "https://drive.google.com/file/d/1hTIK-5y2Czgogrx9Dt9o6noLWBLqkr4n/view?usp=share_link",

    "NOM1222_2022-08-13.pdf":
    "https://drive.google.com/file/d/1InkSPntuIRHczak7N_0_qWx-SNuXHAe2/view?usp=share_link",

    "NOM1222_2022-08-20.pdf":
    "https://drive.google.com/file/d/1EH6y3FjCaX-pnpI_FTfcUE83WYlcnvMw/view?usp=share_link",

    "NOM1222_2022-08-27.pdf":
    "https://drive.google.com/file/d/15mBZA_mRo6TN4mDmRl2hEhZtVYE_CxwE/view?usp=share_link",

    "NOM1222_2022-09-03.pdf":
    "https://drive.google.com/file/d/1NZg6oGuP6V29zquCHMpCgFQ6bV8EEwt_/view?usp=share_link",

    "NOM1222_2022-09-10.pdf":
    "https://drive.google.com/file/d/1xMT_M4JeqLSpO_MGhPbQIm_9LXtWpppn/view?usp=share_link",

    "NOM1222_2022-09-17.pdf":
    "https://drive.google.com/file/d/1KvulhGAe1tJmtlJgPaEWsMkMI5N2_HHT/view?usp=share_link",

    "NOM1222_2022-09-24.pdf":
    "https://drive.google.com/file/d/1X0x8OdygmuS6DJx0k9SoIrmDGHU5RSdQ/view?usp=share_link",

    "NOM1222_2022-10-01.pdf":
    "https://drive.google.com/file/d/16T7Q5ZWifXQJon-yZxK1XQWFR0TQ8bp9/view?usp=share_link",

    "NOM1222_2022-10-08.pdf":
    "https://drive.google.com/file/d/1UB4JJT_p2vhIgWKeX1Hp7kJk4NgvFwCa/view?usp=share_link",

    "NOM1222_2022-10-15.pdf":
    "https://drive.google.com/file/d/1VBIfFltfQup9zRJInNsQioNj5s5DWPI6/view?usp=share_link",

    "NOM1222_2022-10-22.pdf":
    "https://drive.google.com/file/d/1oHLsyNz9tFakByAEA0fTzP8lxItL8W7h/view?usp=share_link",

    "NOM1222_2022-10-29.pdf":
    "https://drive.google.com/file/d/1ciU-V2V9hsa2fqTRs8XdeI-hC8u-l58i/view?usp=share_link",

    "NOM1222_2022-11-05.pdf":
    "https://drive.google.com/file/d/1FZvjHkj6I6M1edzyhzQMmGnMgca3dhTU/view?usp=share_link",

    "NOM1222_2022-11-12.pdf":
    "https://drive.google.com/file/d/111JMcS-K6OXqTHAxqBx3h6Dzp-ppTO1b/view?usp=share_link",

    "NOM1222_2022-11-19.pdf":
    "https://drive.google.com/file/d/1-GStkLDYMdvNUNPzhrV_l_DpvOHbw0Rb/view?usp=share_link",

    "NOM1222_2022-11-26.pdf":
    "https://drive.google.com/file/d/1KzwpnsjS1BQ5hFsyH6MSclAwtA_H5hyc/view?usp=share_link",

    "NOM1222_2022-12-03.pdf":
    "https://drive.google.com/file/d/1gtiB4HCnN4jcM13I1gtmV6pKKc_wiGtJ/view?usp=share_link",

    "NOM1222_2022-12-10.pdf":
    "https://drive.google.com/file/d/1J2DYPCodJUgo9ds9re9s69IuiBi2a9gG/view?usp=share_link",

    "NOM1222_2022-12-17.pdf":
    "https://drive.google.com/file/d/1yhciCyEEJEwvICzIXtEDxK_nfeiyanns/view?usp=share_link",

    "NOM1222_2022-12-24.pdf":
    "https://drive.google.com/file/d/1t9pahHmN5Avz_UUz1xOtbe8d91L06K5J/view?usp=share_link"
    }

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
def download_payroll(request, year_folder, payroll_file_name):
    # payroll_file_name = request.data.get('payroll_filename', None)
    # payroll = Payroll.objects.filter(payroll_filename=payroll_file_name).first()
    # return Response({"file_link": payroll.file_link})

    ######
    file_path = os.path.join(settings.STATIC_ROOT, 'pdf_files', str(year_folder), payroll_file_name)
    with open(file_path, 'rb') as f:
            file_content = f.read()
    # file_content = payroll.file_link
    response = HttpResponse(file_content, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{payroll_file_name}"'
    return response
    #####




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
def detail_payroll(request, year_folder, payroll_file_name):
    # payroll_file_name = request.data.get('payroll_filename', None)
    # payroll = Payroll.objects.filter(payroll_filename=payroll_file_name).first()
    # return Response({"file_link": payroll.file_link})

    # payroll = Payroll.objects.filter(payroll_filename=payroll_file_name).first()
    # file_path = payroll.file_link
    file_path = os.path.join(settings.STATIC_ROOT, 'pdf_files', str(year_folder), payroll_file_name)
    with open(file_path, 'rb') as f:
            file_content = f.read()
    # file_content = payroll.file_link
    response = HttpResponse(file_content, content_type='application/pdf')
    #response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    return response    
    
    
    
    
    
    
    # date_pdf = file_name.split('_')[1].split('.pdf')[0]
    # year_folder = date_pdf.split('-')[0]
    
    # path = os.path.join(settings.STATIC_ROOT, 'pdf_files')
    # for directory_name, directory, files in os.walk(path):
    #     # directory_name = directory_name.replace(str('C:\\Users\\HP\\Documents\\My_files\\LoopGK\\Syncronik_Internship\\projects\\nomina_app_resetpassword_updated\\nomina_app\\core\\staticfiles\\pdf_files' + '\\' + year_folder), str('fa.syncronik.com'+'/'+year_folder))
    #     for file_ in files:
    #         if file_ == file_name:
    #             return Response({"file": str(directory_name + '/' + file_)}, status=200)
    # return Response({"msg": "Archivo no encontrado"}, status=400)
    
 