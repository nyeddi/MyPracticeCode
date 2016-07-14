#User define exceptions:
class Error(Exception):
    """Base class for exceptions raised from Patient-Doctor Scheduler."""
    pass

class SlotNotEmptyError(Error):
    """Exception raised for errors in the SlotNotEmptyError.

    Attributes:
        slot -- slot information
        record  -- explanation of the record
        msg -- slot not available
    """

    def __init__(self, slot, record, msg):
        self.slot = slot
        self.record = record
        self.msg = msg

class DctNotAvblError(Error):
    """Raised when an operation attempts a book a doctor schedule when doctor
     schedule is not empty.

    Attributes:
        slot -- slot information
        doctor -- doctor insformation
        msg  -- explanation of why the specific error
    """

    def __init__(self, slot, doctor, msg):
        self.slot = slot
        self.doctor = doctor
        self.msg = msg

class PtntNotAvblError(Error):
    """Raised when an operation attempts a book a doctor schedule when doctor
     schedule is not empty.

    Attributes:
        slot -- slot information
        doctor -- Patient insformation
        msg  -- explanation of why the specific error
    """

    def __init__(self, slot, Patient, msg):
        self.slot = slot
        self.Patient = Patient
        self.msg = msg    
