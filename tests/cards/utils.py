import io

from django.core.files.uploadedfile import InMemoryUploadedFile


def generate_file(qt_lines='14'):
    content = f'''{qt_lines}
4253625879615786
4424424424442444
5122-2368-7954-3214
4123456789123456
5123-4567-8912-3456
4123356789123456
42536258796157867
4424444424442444
5122-2368-7954 - 3214
44244x4424442444
0525362587961578
61234-567-8912-3456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456
'''

    # Create buffer
    buff = io.StringIO(content)

    # Set the cursor to write
    buff.seek(0, 2)

    # Create the InMemoryUploadedFile
    file = InMemoryUploadedFile(
        buff,
        'file',
        'card_numbers.txt',
        None,
        buff.tell(),
        None,
    )

    # Set the cursor to begin of file
    file.seek(0)

    return file
