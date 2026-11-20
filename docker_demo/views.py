import platform
import socket

from django.http import HttpResponse


def home(request):
    html = f"""
    <html dir="rtl" lang="fa">
      <body style="font-family: sans-serif; text-align: center; margin-top: 60px;">
        <h1>سلام! این پروژه داخل Docker اجرا شد</h1>
        <p>نسخه‌ی پایتون داخل Container: <b>{platform.python_version()}</b></p>
        <p>اسم (شناسه‌ی) Container: <b>{socket.gethostname()}</b></p>
      </body>
    </html>
    """
    return HttpResponse(html)
