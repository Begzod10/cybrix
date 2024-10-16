class CustomResponseMixin:
    def get_custom_message(self, method):
        messages = {
            'POST': "muvaffaqiyatli yaratildi.",
            'PUT': "maʼlumotlari muvaffaqiyatli yangilandi.",
            'PATCH': "maʼlumotlari muvaffaqiyatli yangilandi.",
            'DELETE': "maʼlumotlari muvaffaqiyatli o'chirildi.",
        }
        return messages.get(method, "amal muvaffaqiyatli yakunlandi.")

    def finalize_response(self, request, response, *args, **kwargs):
        response = super().finalize_response(request, response, *args, **kwargs)

        if not (200 <= response.status_code < 300 and isinstance(response.data, (dict, list))):
            return response
        custom_message = self.get_custom_message(request.method)
        if isinstance(response.data, dict):
            response.data['msg'] = custom_message
        elif isinstance(response.data, list):
            response.data = {
                'msg': custom_message,
            }
        return response
