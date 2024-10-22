from datetime import date

from django.db.models import Q


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


class QueryParamFilterMixin:
    filter_mappings = {}
    filter_conditions = Q()

    def filter_queryset(self, queryset):
        query_params = self.request.query_params

        for param, field in self.filter_mappings.items():
            value = query_params.get(param)
            if not value or value == 'null':
                if param == 'branch':
                    user = get_user(self.request)
                    self.filter_conditions &= Q(**{field: user.branch_id})
                continue

            if param == 'age' and '-' in value:
                try:
                    age_from, age_to = map(int, value.split('-'))
                    today = date.today()
                    birth_date_from = date(today.year - age_to, today.month, today.day)
                    birth_date_to = date(today.year - age_from, today.month, today.day)
                    self.filter_conditions &= Q(**{f'{field}__range': (birth_date_from, birth_date_to)})
                except ValueError:
                    continue
            elif value.startswith('[') and value.endswith(']'):
                value_list = value.strip('[]').split(',')
                self.filter_conditions &= Q(**{f'{field}__in': [v.strip() for v in value_list]})
            elif value.isdigit():
                self.filter_conditions &= Q(**{field: value})
            elif value in ['True', 'False']:
                self.filter_conditions &= Q(**{field: value == 'True'})

        if self.filter_conditions:
            queryset = queryset.filter(self.filter_conditions)

        return queryset
