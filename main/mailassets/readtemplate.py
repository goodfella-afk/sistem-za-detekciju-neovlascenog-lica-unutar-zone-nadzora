from string import Template

def read_template(filename):

    #return template obj
    with open('/opt/frtsys/main/mailassets/message.txt', 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


