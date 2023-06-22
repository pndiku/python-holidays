#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date
from datetime import timedelta as td

from holidays.calendars import _CustomIslamicCalendar
from holidays.constants import JAN, FEB, MAY, JUN, JUL, AUG, SEP, OCT
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays, IslamicHolidays


class Uganda(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Uganda

    Holidays based on the Islamic Calendar are estimated (and so denoted),
    as are announced each year and based on moon sightings:
    - Eid al-Fitr
    - Eid al-Adha
    """

    country = "UG"
    special_holidays = {}

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self, calendar=UgandaIslamicCalendar())
        super().__init__(*args, **kwargs)

    def _add_observed(self, dt: date, days: int = +1) -> None:
        if self.observed and self._is_sunday(dt):
            self._add_holiday("%s (Observed)" % self[dt], dt + td(days=days))

    def _populate(self, year):
        if year <= 1962:
            return None

        super()._populate(year)

        # New Year's Day
        self._add_observed(self._add_new_years_day("New Year's Day"))

        # Good Friday
        self._add_good_friday("Good Friday")

        # Easter Monday
        self._add_easter_monday("Easter Monday")

        # Labour Day
        self._add_observed(self._add_labor_day("Labour Day"))

        if year >= 1986:
            # Liberation Day
            self._add_observed(self._add_holiday("Liberation Day", JAN, 26))

        if year >= 2015:
            # Archbishop Janani Luwum Day
            self._add_observed(self._add_holiday("Archbishop Janani Luwum Day", FEB, 16))

        # Uganda Martyrs' Day
        self._add_observed(self._add_holiday("Uganda Martyrs' Day"), JUN, 3)

        # National Heroes' Day
        self._add_observed(self._add_holiday("National Heroes' Day"), JUN, 9)
        # Independence Day
        self._add_observed(self._add_holiday("Independence Day", OCT, 9))

        # Christmas Day
        self._add_observed(self._add_christmas_day("Christmas Day"), days=+2)

        # Boxing Day
        self._add_observed(self._add_christmas_day_two("Boxing Day"))


class UG(Uganda):
    pass


class UGN(Uganda):
    pass


class UgandaIslamicCalendar(_CustomIslamicCalendar):
    EID_AL_ADHA_DATES = {
        2017: (SEP, 1),
        2018: (AUG, 21),
        2019: (AUG, 11),
        2020: (JUL, 31),
    }

    EID_AL_FITR_DATES = {
        2017: (JUN, 25),
        2018: (JUN, 14),
        2019: (JUN, 3),
        2020: (MAY, 24),
    }
