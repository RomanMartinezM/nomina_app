from django.urls import path
from .views import payrolls_register, get_payrolls, download_payroll, detail_payroll, payrolls_register_on_render

urlpatterns = [
    # Payroll views
    path('payroll-register/', payrolls_register),
    path('payroll-register-render/', payrolls_register_on_render),
    path('get-payrolls/', get_payrolls),
    # path('download_payroll/', download_payroll, name='download_payroll'),
    path('download_payroll/<str:payroll_file_name>/', download_payroll, name='download_payroll'),
    # path('detail_payroll/', detail_payroll, name='detail_payroll'),
    path('detail_payroll/<str:payroll_file_name>/', detail_payroll, name='detail_pdf'),
] 