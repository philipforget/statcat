# Order matters here, Stat has a foreignkey to Instrument, so Instrument
# must be imported first
from .instrument import Instrument

from .stat import Stat
