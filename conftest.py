#Указываем путь до файла с фикстурами, чтобы использовать их глобально
pytest_plugins =(
    "fixtures.pages",
    "fixtures.browsers"
)
