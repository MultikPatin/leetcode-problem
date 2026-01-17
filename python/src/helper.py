import inspect
import logging
from collections.abc import Callable, Iterable, Mapping, Sequence
from enum import StrEnum, auto


class Fields(StrEnum):
    args = auto()
    expd = auto()


def tester(
    solution: Callable,
    task_name: str,
    test_data: Sequence[Mapping[str, Iterable]],
) -> None:
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    task = getattr(solution(), task_name, None)
    if task is None:
        attrs = [n for n in solution.__dict__ if not n.startswith("__")]
        msg = f"Task '{task_name}' not found in class methods: {attrs}"
        raise AttributeError(msg)

    func_args = inspect.getfullargspec(task).args
    func_args.remove("self")

    for i, data in enumerate(test_data, start=1):
        result = task(*data[Fields.args])
        title = f"Test {i} |"

        logger.info(
            "%s Input:  %s",
            title,
            dict(zip(func_args, data[Fields.args], strict=True)),
        )
        logger.info("%s Output: %s", title, data[Fields.expd])
        logger.info("%s Result: %s", title, result)

        if result != data[Fields.expd]:
            logger.info("======== FAILED")
        else:
            logger.info("======== PASSED")
