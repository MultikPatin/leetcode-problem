import inspect
import logging
from collections.abc import Callable, Iterable, Mapping, Sequence
from enum import StrEnum, auto
from typing import Any

PLACEHOLDER1 = "=========="
PLACEHOLDER2 = "----------"


class Fields(StrEnum):
    args = auto()
    expd = auto()


def tester(
    func: Callable, test_data: Sequence[Mapping[Fields, Iterable]]
) -> None:
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(" | " + func.__name__ + " | ")

    fails = []
    for i, data in enumerate(test_data, start=1):
        args = data[Fields.args]
        expected = data[Fields.expd]
        result = func(*args)

        logger.info("%s Test %s", PLACEHOLDER1, i)
        logger.info("Arguments: %s", _arguments(func, args))
        logger.info("Expected:  %s", expected)
        logger.info("Result:    %s", result)

        if result != data[Fields.expd]:
            fails.append(i)
            logger.info("%s FAILED", PLACEHOLDER2)
        else:
            logger.info("%s PASSED", PLACEHOLDER2)

    if not fails:
        logger.info(" ALL TESTS PASSED")
    else:
        logger.info("%s %s tests FAILS", PLACEHOLDER1, len(fails))


def _arguments(func: Callable, data: Iterable) -> dict[Any, Any]:
    args = inspect.getfullargspec(func).args
    args.remove("self")
    return dict(zip(args, data, strict=True))
