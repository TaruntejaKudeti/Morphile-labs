from django.shortcuts import render


from django.http import HttpResponse
import os
from datetime import datetime
import subprocess
import pytz

def htop(request):
    name = "Kudeti Tarun Teja"  # Replace with your actual full name
    username = os.getlogin()
    ist_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S')
    top_output = subprocess.check_output("top -bn1 | head -10", shell=True).decode()

    return HttpResponse(f"""
    <html>
    <body>
        <h1>/htop</h1>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time in IST:</strong> {ist_time}</p>
        <pre><strong>Top Output:</strong>\n{top_output}</pre>
    </body>
    </html>
    """)
