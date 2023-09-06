from src.repositories.parsing_menu import ParsingMenuRepository
from src.services.parsing_menu_magicinfo import ParsingService
from src.repositories.menu import MenuRepository, ContentReposytory
from src.services.menu import MenuService


def parsing_menu(server: str):
    return ParsingService(
        parsing_menu_repo=ParsingMenuRepository(server), server=server)


def update_menu_info(server: str):
    return MenuService(
        menu_repo=MenuRepository(),
        content_repo=ContentReposytory(), server=server
        )