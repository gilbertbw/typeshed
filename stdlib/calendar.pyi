import datetime
import sys
from _typeshed import Unused
from collections.abc import Iterable, Sequence
from time import struct_time
from typing import ClassVar
from typing_extensions import Literal, TypeAlias

__all__ = [
    "IllegalMonthError",
    "IllegalWeekdayError",
    "setfirstweekday",
    "firstweekday",
    "isleap",
    "leapdays",
    "weekday",
    "monthrange",
    "monthcalendar",
    "prmonth",
    "month",
    "prcal",
    "calendar",
    "timegm",
    "month_name",
    "month_abbr",
    "day_name",
    "day_abbr",
    "Calendar",
    "TextCalendar",
    "HTMLCalendar",
    "LocaleTextCalendar",
    "LocaleHTMLCalendar",
    "weekheader",
]

if sys.version_info >= (3, 10):
    __all__ += ["FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"]

_LocaleType: TypeAlias = tuple[str | None, str | None]

class IllegalMonthError(ValueError):
    def __init__(self, month: int) -> None: ...

class IllegalWeekdayError(ValueError):
    def __init__(self, weekday: int) -> None: ...

def isleap(year: int) -> bool: ...
def leapdays(y1: int, y2: int) -> int: ...
def weekday(year: int, month: int, day: int) -> int: ...
def monthrange(year: int, month: int) -> tuple[int, int]: ...

class Calendar:
    firstweekday: int
    def __init__(self, firstweekday: int = ...) -> None: ...
    def getfirstweekday(self) -> int: ...
    def setfirstweekday(self, firstweekday: int) -> None: ...
    def iterweekdays(self) -> Iterable[int]: ...
    def itermonthdates(self, year: int, month: int) -> Iterable[datetime.date]: ...
    def itermonthdays2(self, year: int, month: int) -> Iterable[tuple[int, int]]: ...
    def itermonthdays(self, year: int, month: int) -> Iterable[int]: ...
    def monthdatescalendar(self, year: int, month: int) -> list[list[datetime.date]]: ...
    def monthdays2calendar(self, year: int, month: int) -> list[list[tuple[int, int]]]: ...
    def monthdayscalendar(self, year: int, month: int) -> list[list[int]]: ...
    def yeardatescalendar(self, year: int, width: int = ...) -> list[list[int]]: ...
    def yeardays2calendar(self, year: int, width: int = ...) -> list[list[tuple[int, int]]]: ...
    def yeardayscalendar(self, year: int, width: int = ...) -> list[list[int]]: ...
    def itermonthdays3(self, year: int, month: int) -> Iterable[tuple[int, int, int]]: ...
    def itermonthdays4(self, year: int, month: int) -> Iterable[tuple[int, int, int, int]]: ...

class TextCalendar(Calendar):
    def prweek(self, theweek: int, width: int) -> None: ...
    def formatday(self, day: int, weekday: int, width: int) -> str: ...
    def formatweek(self, theweek: int, width: int) -> str: ...
    def formatweekday(self, day: int, width: int) -> str: ...
    def formatweekheader(self, width: int) -> str: ...
    def formatmonthname(self, theyear: int, themonth: int, width: int, withyear: bool = ...) -> str: ...
    def prmonth(self, theyear: int, themonth: int, w: int = ..., l: int = ...) -> None: ...
    def formatmonth(self, theyear: int, themonth: int, w: int = ..., l: int = ...) -> str: ...
    def formatyear(self, theyear: int, w: int = ..., l: int = ..., c: int = ..., m: int = ...) -> str: ...
    def pryear(self, theyear: int, w: int = ..., l: int = ..., c: int = ..., m: int = ...) -> None: ...

def firstweekday() -> int: ...
def monthcalendar(year: int, month: int) -> list[list[int]]: ...
def prweek(theweek: int, width: int) -> None: ...
def week(theweek: int, width: int) -> str: ...
def weekheader(width: int) -> str: ...
def prmonth(theyear: int, themonth: int, w: int = ..., l: int = ...) -> None: ...
def month(theyear: int, themonth: int, w: int = ..., l: int = ...) -> str: ...
def calendar(theyear: int, w: int = ..., l: int = ..., c: int = ..., m: int = ...) -> str: ...
def prcal(theyear: int, w: int = ..., l: int = ..., c: int = ..., m: int = ...) -> None: ...

class HTMLCalendar(Calendar):
    cssclasses: ClassVar[list[str]]
    cssclass_noday: ClassVar[str]
    cssclasses_weekday_head: ClassVar[list[str]]
    cssclass_month_head: ClassVar[str]
    cssclass_month: ClassVar[str]
    cssclass_year: ClassVar[str]
    cssclass_year_head: ClassVar[str]
    def formatday(self, day: int, weekday: int) -> str: ...
    def formatweek(self, theweek: int) -> str: ...
    def formatweekday(self, day: int) -> str: ...
    def formatweekheader(self) -> str: ...
    def formatmonthname(self, theyear: int, themonth: int, withyear: bool = ...) -> str: ...
    def formatmonth(self, theyear: int, themonth: int, withyear: bool = ...) -> str: ...
    def formatyear(self, theyear: int, width: int = ...) -> str: ...
    def formatyearpage(self, theyear: int, width: int = ..., css: str | None = ..., encoding: str | None = ...) -> str: ...

class different_locale:
    def __init__(self, locale: _LocaleType) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *args: Unused) -> None: ...

class LocaleTextCalendar(TextCalendar):
    def __init__(self, firstweekday: int = ..., locale: _LocaleType | None = ...) -> None: ...

class LocaleHTMLCalendar(HTMLCalendar):
    def __init__(self, firstweekday: int = ..., locale: _LocaleType | None = ...) -> None: ...
    def formatweekday(self, day: int) -> str: ...
    def formatmonthname(self, theyear: int, themonth: int, withyear: bool = ...) -> str: ...

c: TextCalendar

def setfirstweekday(firstweekday: int) -> None: ...
def format(cols: int, colwidth: int = ..., spacing: int = ...) -> str: ...
def formatstring(cols: int, colwidth: int = ..., spacing: int = ...) -> str: ...
def timegm(tuple: tuple[int, ...] | struct_time) -> int: ...

# Data attributes
day_name: Sequence[str]
day_abbr: Sequence[str]
month_name: Sequence[str]
month_abbr: Sequence[str]

MONDAY: Literal[0]
TUESDAY: Literal[1]
WEDNESDAY: Literal[2]
THURSDAY: Literal[3]
FRIDAY: Literal[4]
SATURDAY: Literal[5]
SUNDAY: Literal[6]

EPOCH: Literal[1970]
