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

    fails = []
    for i, data in enumerate(test_data, start=1):
        result = task(*data[Fields.args])
        title = f"Test {i} |"
        in_data = dict(zip(func_args, data[Fields.args], strict=True))
        out_data = data[Fields.expd]

        logger.info("%s Input:  %s", title, in_data)
        logger.info("%s Output: %s", title, out_data)
        logger.info("%s Result: %s", title, result)

        if result != data[Fields.expd]:
            logger.info("======== FAILED")
            fails.append(
                {"title": title, "in": in_data, "out": out_data, "res": result}
            )
        else:
            logger.info("======== PASSED")

    if not fails:
        logger.info("All tests PASSED! ")
        return

    logger.error("==========================================================")
    logger.error("Some tests FAILED!")
    for fail in fails:
        logger.error(fail["title"])
        logger.error("Input:  %s", fail["in"])
        logger.error("Output: %s", fail["out"])
        logger.error("Result: %s", fail["res"])
