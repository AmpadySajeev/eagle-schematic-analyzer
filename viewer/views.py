from django.shortcuts import render
import xml.etree.ElementTree as ET
from parser import parse_schematic

def upload_schematic(request):
    context = {}

    if request.method == 'POST':
        uploaded_file = request.FILES.get('schematic_file')

        if not uploaded_file:
            context["error"] = "Please select a schematic file."

        elif not uploaded_file.name.lower().endswith(".sch"):
            context["error"] = "Please select an .sch file"

        elif uploaded_file.size > 5 * 1024 * 1024:
            context["error"] = "File size must be 5 MB or less"

        else:
            try:
                result = parse_schematic(uploaded_file)
                context["parts"] = result["parts"]
                context["nets"] = result["nets"]
            except(ET.ParseError, ValueError, OSError):
                context["error"] = (
                    "Unable to parse this file. "
                    "Please upload a valid EAGLE schematic file."
                )
    return render(request, "viewer/upload.html", context)
