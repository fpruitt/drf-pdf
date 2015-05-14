# encoding: utf-8
from cStringIO import StringIO

from rest_framework import status
from rest_framework.views import APIView

from drf_pdf.renderer import PDFRenderer
from drf_pdf.response import PDFResponse

from weasyprint import HTML


class FromTemplate(APIView):
    renderer_classes = (PDFRenderer, )

    def get(self, request):
        pdf = StringIO()

        # This example may change to a new drf-pdf response
        HTML(string='<h1>Foo</h1>').write_pdf(pdf)

        return PDFResponse(
            pdf.getvalue(),
            file_name='example',
            status=status.HTTP_200_OK
        )
