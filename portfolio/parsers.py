import csv
from rest_framework.parsers import MultiPartParser
from rest_framework.exceptions import ParseError

class CSVAndImageParser(MultiPartParser):
    def parse(self, stream, media_type=None, parser_context=None):
        result = super().parse(stream, media_type, parser_context)
        csv_file = None
        image_files = []

        for file in result.files.values():
            if file.name.endswith('.csv'):
                csv_file = file
            else:
                image_files.append(file)

        if csv_file is None:
            raise ParseError("CSV file is required")

        csv_data = csv.DictReader(csv_file.read().decode('utf-8').splitlines())
        return {
            'csv_data': list(csv_data),
            'image_files': image_files
        }