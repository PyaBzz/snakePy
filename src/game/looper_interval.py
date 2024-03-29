import asyncio


class LooperInterval:
    _iterations: int
    counter: int
    _interval: float
    _func: object
    _should_continue: bool
    _end_callback: object
    _args: tuple

    def __init__(
        self,
        func: object,
        interval: float,
        iterations: int = 0,
        end_callback: object = lambda: None,
        args: tuple = (),
    ) -> None:
        self.counter = 0
        self._interval = interval
        self._func = func
        self._iterations = iterations
        self._args = args
        self._end_callback = end_callback

    async def start(self) -> int:
        self._should_continue = True
        if self._iterations:
            while self._should_continue and self._iterations > 0:
                await self._cycle()
                self._iterations -= 1
        else:
            while self._should_continue:
                await self._cycle()
        self._end_callback()
        return self.counter

    def stop(self) -> int:
        self._should_continue = False
        return self.counter

    async def _cycle(self) -> None:
        await asyncio.sleep(self._interval)
        self._func(*self._args)
        self.counter += 1
