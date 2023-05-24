menu = [
    {'title': "Турниры", 'url_name': 'index'},
    {'title': "Команды", 'url_name': 'teams'},
    {'title': "Игроки", 'url_name': 'players'},
]


class ContextMixin:
    @staticmethod
    def get_user_context(**kwargs):
        context = kwargs
        user_menu = menu.copy()
        context['menu'] = user_menu
        return context

