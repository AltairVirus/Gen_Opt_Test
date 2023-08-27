import mimetypes
import os
import uuid
from urllib.parse import urlencode


class UploadTRRequest:
    def __init__(self, group):
        self.params = {
            'plan': f'{group.MODEL.PLAN.id}',
            'modelId': f'{group.MODEL.PLAN.id}',
            'RuleGroupId': '58e95ef2-7b5b-44dc-9a44-6105a63e0f6b',
            'loadAllItemsToPlan': 'false',
            'userCorrections': f'{group.MODEL.UC.id}'
        }
        delimiter = '-------------123456789'
        file = File("05_Ц1_ТР_НЕФТЯНЫХ_НА_МАЙ_2023г без пароля [N92oDN].xlsx",
                    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'Content file')
        post = BodyPost.get({'file': file}, delimiter)
        self.form_data = post


class File:
    def __init__(self, name, mime=None, content=None):
        # if content is None, then we assume that $name is a path to the file
        if content is None:
            # get the file name from the path
            info = os.path.basename(name)
            # check if the file is readable
            if info and os.access(name, os.R_OK):
                self.name = info
                # get the MIME type of the file
                self.mime = mimetypes.guess_type(name)[0]
                # get the content of the file
                content = open(name, 'rb').read()
                # check if the content was read successfully
                if content:
                    self.content = content
                else:
                    raise Exception('Don`t get content - "{}"'.format(name))
            else:
                raise Exception('Error param')
        else:
            # set the file name
            self.name = name
            # if MIME type is not specified, guess it from the file name
            if mime is None:
                mime = mimetypes.guess_type(name)[0]
            # set the MIME type
            self.mime = mime
            # set the content of the file
            self.content = content


class BodyPost:
    # Метод формирования части составного запроса
    @staticmethod
    def create_part_of_post(name, val):
        body = 'Content-Disposition: form-data; name="' + name + '"'
        # Проверяем передан ли класс File
        if isinstance(val, File):
            # Извлекаем имя файла
            fil = val.name
            # Извлекаем MIME тип файла
            mime = val.mime
            # Извлекаем содержимое файла
            cont = val.content

            body += '; filename="' + fil + '"' + "\r\n"
            body += 'Content-Type: ' + mime + "\r\n\r\n\r\n"
            # body += cont + "\r\n"
        else:
            body += "\r\n\r\n" + urlencode(val) + "\r\n"
        return body

    # Метод формирующий тело POST запроса из переданного массива
    @classmethod
    def get(cls, post_list: dict, delimit='-------------0123456789'):
        if isinstance(post_list, dict) and post_list:
            bool = False
            # Проверяем есть ли среди элементов массива файл
            for val in post_list.values():
                if isinstance(val, File):
                    bool = True
                    break
            if bool:
                ret = ''
                # Формируем из каждого элемента массива, составное тело POST запроса
                for name, val in post_list.items():
                    ret += '--' + delimit + "\r\n" + cls.create_part_of_post(name, val)
                ret += "--" + delimit + "--\r\n"
            else:
                ret = post_list
        else:
            raise Exception('Error input param!')
        return ret

#
# # ?????????? ?????????? ?????? ??? ?????????? ?????? POST ???????

#
# # ????????? ?????? oFile ?????????? ????

#
# # ????????? ???? POST ???????


#
# # ??????????????  CURL
# ch = curl_init()
#
# # ????????? ?? ????? ?????? ???????? ????
# curl_setopt(ch, CURLOPT_URL, 'http://server/upload/')
# # ?????????, ??? ????? ?????????????? POST ??????
# curl_setopt(ch, CURLOPT_POST, 1)
# # ???????? ???? POST ???????
# curl_setopt(ch, CURLOPT_POSTFIELDS, post)
#
# / * ????????? ?????????????? ?????? ??? ?????????:
# Content - Type - ??? ???????????,
# boundary - ??????????? ?
# Content - Length - ????? ???? ????????? * /
# curl_setopt(ch, CURLOPT_HTTPHEADER, ['Content-Type: multipart/form-data; boundary=' + delimiter,
#                                      'Content-Length: ' + str(len(post))])
#
# # ?????????? POST ?????? ?? ????????? Web ??????
# curl_exec(ch)
