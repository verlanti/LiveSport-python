from django.shortcuts import render_to_response


def main_page():
    return render_to_response('index.html')
