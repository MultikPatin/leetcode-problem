import inspect
import logging
from collections.abc import Callable, Iterable, Mapping, Sequence


def tester(
    solution: Callable,
    task_name: str,
    test_data: Sequence[Mapping[str, Iterable]],
) -> None:
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    solution = solution()

    task = getattr(solution, task_name, None)
    if task is None:
        attrs = [n for n in solution.__dict__ if not n.startswith("__")]
        msg = f"Task {task_name} not found in {attrs} class"
        raise AttributeError(msg)

    func_args = inspect.getfullargspec(task).args
    func_args.remove("self")

    for i, data in enumerate(test_data, start=1):
        result = task(*data["args"])

        logger.info(
            "Test %s. Input:  %s",
            i,
            dict(zip(func_args, data["args"], strict=True)),
        )
        logger.info("Test %s. Output: %s", i, data["expected"])
        logger.info("Test %s. Result: %s", i, result)

        if result != data["expected"]:
            logger.info("Test %s. ==== FAILED with result: %s", i, result)
        else:
            logger.info("Test %s. ==== PASSED", i)
