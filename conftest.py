import logging
import pytest

# задаем глобальные настройки для логирования
logging.basicConfig(level=logging.ERROR,
                    format='\n %(levelname)s (%(asctime)s) : %(message)s  (Line: %(lineno)d [%(filename)s])',
                    datefmt='%I:%M:%S %p')

# сохраняем историю падений в разрезе имен классов и индексов в параметризации (если она используется)
_test_failed_incremental: dict[str, dict[tuple[int, ...], str]] = {}


def pytest_runtest_makereport(item, call):
    if "incremental" in item.keywords:
        # используется маркер incremental
        if call.excinfo is not None:
            # тест упал
            # извлекаем из теста имя класса
            cls_name = str(item.cls)
            # извлекаем индексы теста (если вместе с  incremental используется параметризация)
            parametrize_index = (
                tuple(item.callspec.indices.values())
                if hasattr(item, "callspec")
                else ()
            )
            # извлекаем имя тестовой функции
            test_name = item.originalname or item.name
            # сохраняем в _test_failed_incremental оригинальное имя упавшего теста
            _test_failed_incremental.setdefault(cls_name, {}).setdefault(
                parametrize_index, test_name
            )


def pytest_runtest_setup(item):
    if "incremental" in item.keywords:
        # извлекаем из теста имя класса
        cls_name = str(item.cls)
        # проверяем, падал ли предыдущий тест на этом классе
        if cls_name in _test_failed_incremental:
            # извлекаем индексы теста (если вместе с  incremental используется параметризация)
            parametrize_index = (
                tuple(item.callspec.indices.values())
                if hasattr(item, "callspec")
                else ()
            )
            # извлекаем имя первой тестовой функции, которая должна упасть для этого имени класса и индекса
            test_name = _test_failed_incremental[cls_name].get(parametrize_index, None)
            # если нашли такое имя, значит, тест падал для такой комбинации класса & фукнкции
            if test_name is not None:
                pytest.xfail(f"Tests is stopped because test -- {test_name} -- is failed")
