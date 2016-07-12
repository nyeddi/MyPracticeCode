SLOT_1 = '8:00AM'
SLOT_2 = '8:30AM'
SLOT_3 = '9:00AM'
SLOT_4 = '9:30AM'
SLOT_5 = '10:00AM'
SLOT_6 = '10:30AM'
SLOT_7 = '11:00AM'
SLOT_8 = '11:30AM'
SLOT_9 = '1:00PM'
SLOT_10 = '1:30PM'
SLOT_11 = '2:00PM'
SLOT_12 = '2:30PM'
SLOT_13 = '3:00PM'
SLOT_14 = '3:30PM'
SLOT_15 = '4:00PM'
SLOT_16 = '4:30PM'

class Person(object):

    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
        self.full_name = self.f_name+" " + self.l_name
        self.calendar= Calendar()


    def get_record(self):
        return {
            'name': self.full_name,
        }

    def make_appointment(self,slot, record):
        self.calendar.add_entry(slot,record)

    def is_available(self,slot):
        return self.calendar.is_available(slot)



class Calendar(object):

    def __init__(self):
        self.entries = {
        }

    def is_available(self,slot):
        if slot not in self.entries:
            return True
        else:
            return False


    def add_entry(self, slot, record):
        if self.is_available(slot):
            self.entries[slot] = record
        else:
            return "Slot not empty"

    def __str__(self):
        return str(self.entries)

class Doctor(Person):

    def __init__(self, f_name, l_name, speciality):
        Person.__init__(self, f_name, l_name)
        self.speciality = speciality


    def get_record(self):
        record = Person.get_record(self)
        record["speciality"] = self.speciality
        return record



class Patient(Person):

    def __init__(self, f_name, l_name, ssn):
        Person.__init__(self, f_name, l_name)
        self.ssn = ssn
        self.patient_id = self.f_name[:1] + self.l_name + str(self.ssn)


    def get_record(self):
        record = Person.get_record(self)
        print record
        record['patient_id'] = self.patient_id
        return record

def schedule(patient, doctor, slot):
    if not doctor.is_available(slot):
        print "Doctor not available"
        return
    if not patient.is_available(slot):
        print "Patient not available"
        return
    doctor.make_appointment(slot, patient.get_record())
    patient.make_appointment(slot, doctor.get_record())



P1 = Patient("first", "patient", 275)
P2 = Patient("second", "patient", 276)
P3 = Patient("thrid", "patient", 277)
D1 = Doctor("first", "doctor", "head")
D2 = Doctor("second", "doctor", "body")
D3 = Doctor("thrid", "doctor", "legs")



a= P1.get_record()
b =D1.get_record()

print a
print b

schedule(P1,D1, SLOT_1)
schedule(P2,D1, SLOT_1)

print P1.calendar.__str__()
print D2.calendar.__str__()
