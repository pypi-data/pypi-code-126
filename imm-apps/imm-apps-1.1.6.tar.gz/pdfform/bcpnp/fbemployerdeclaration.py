from model.common.advertisement import Advertisements, InterviewRecords
from pdfform.jsonmaker import JsonMaker
from model.common.address import Addresses
from model.bcpnp.jobofferform import JobOfferFormModel
from model.common.contact import Contacts
from assess.policy.bcpnp.data import bc_tech_pilot
from datetime import date


class FormBuilderEmployerDeclaration:
    """Form builder"""

    def __init__(self, jof: JobOfferFormModel):
        self.jof = jof
        self.form = JsonMaker()

    def start(self):
        self.form.add_skip(1)

    def employee(self):
        self.form.add_text(self.jof.personal.last_name)
        self.form.add_text(self.jof.personal.first_name)

    def employer(self):
        self.form.add_text(self.jof.general.legal_name)
        self.form.add_text(self.jof.general.operating_name or "")

        mailing_address = Addresses(self.jof.eraddress).mailing
        business_address = Addresses(self.jof.eraddress).business

        self.form.add_text(mailing_address.line1)
        self.form.add_text(mailing_address.city)
        self.form.add_text(mailing_address.province)
        self.form.add_text(mailing_address.country)
        self.form.add_text(mailing_address.post_code)

        if mailing_address == business_address:
            self.form.add_skip(5)
        else:
            self.form.add_text(business_address.line1)
            self.form.add_text(business_address.city)
            self.form.add_text(business_address.province)
            self.form.add_text(business_address.country)
            self.form.add_text(business_address.post_code)
        # contact
        contact = Contacts(self.jof.contact).primary
        self.form.add_text(contact.last_name)
        self.form.add_text(contact.first_name)
        self.form.add_text(contact.position)
        self.form.add_text(contact.phone)
        self.form.add_text(contact.email)

        # other
        self.form.add_text(self.jof.general.website)
        self.form.add_text(self.jof.general.ft_employee_number)
        self.form.add_text(self.jof.general.establish_date.year)
        self.form.add_text(self.jof.general.industry)

        if self.jof.general.corporate_structure == "Incorporated":
            self.form.add_checkbox(True)
        elif self.jof.general.corporate_structure == "Limited Liability Partnership":
            self.form.add_skip(1)
            self.form.add_checkbox(True)
        elif self.jof.general.corporate_structure == "Extra-provincially-registered":
            self.form.add_skip(2)
            self.form.add_checkbox(True)
        self.form.add_text(self.jof.general.registration_number)
        # other corporate structure
        if (
            self.jof.general.corporate_structure == "federally-incorporated"
            or self.jof.general.corporate_structure == "Other"
        ):
            self.form.add_checkbox(True)
            self.form.add_text(self.jof.general.corporate_structure)

    def joboffer(self):
        self.form.add_text(self.jof.joboffer.job_title)
        self.form.add_text(self.jof.joboffer.hourly_rate)
        self.form.add_text(self.jof.joboffer.annual_rate)
        self.form.add_text(self.jof.joboffer.weekly_hours)

        work_locations = Addresses(self.jof.eraddress).workings
        # first work location
        if len(work_locations) < 1:
            raise ValueError("Work location missed")
        self.form.add_text(work_locations[0].line1)
        self.form.add_text(work_locations[0].city)
        self.form.add_text(work_locations[0].post_code)
        self.form.add_text(work_locations[0].phone)
        if len(work_locations) >= 2:
            self.form.add_text(work_locations[1].line1)
            self.form.add_text(work_locations[1].city)
            self.form.add_text(work_locations[1].post_code)
            self.form.add_text(work_locations[1].phone)
        else:
            self.form.add_skip(4)

    def tech(self):
        if self.jof.joboffer.noc in bc_tech_pilot:
            if self.jof.joboffer.permanent:
                self.form.add_radio(True)
                self.form.add_skip(5)  # messy skip :(
            else:
                self.form.add_radio(False)
                self.form.add_text(self.jof.joboffer.work_end_date.strftime("%d-%b-%Y"))
                self.form.add_skip(3)
                self.form.add_text(self.jof.joboffer.why_not_permanent)
        else:
            self.form.add_skip(5)

    def position(self):
        # new position
        self.form.add_radio(self.jof.position.is_new)
        self.form.add_radio(self.jof.position.under_cba)
        if self.jof.position.under_cba:
            self.form.add_text(self.jof.position.which_union)
        else:
            self.form.add_skip(1)

        # employee number in same position
        self.form.add_text(self.jof.position.has_same_number)
        self.form.add_text(self.jof.position.vacancies_number)
        self.form.add_text(self.jof.position.laidoff_with12)
        self.form.add_text(self.jof.position.laidoff_current)
        # language requirement
        self.form.add_radio(self.jof.joboffer.other_language_required)
        if self.jof.joboffer.other_language_required:
            self.form.add_text(self.jof.joboffer.reason_for_other)
        else:
            self.form.add_skip(1)

        # lmia status
        self.form.add_radio(self.jof.position.lmia_refused)
        if self.jof.position.lmia_refused:
            self.form.add_text(self.jof.position.lmia_refused_reason)
        else:
            self.form.add_skip(1)

        # license issue
        if self.jof.joboffer.license_request:
            if self.jof.joboffer.license_met:
                self.form.add_radio(True)
                self.form.add_text(self.jof.joboffer.license_met_reason)
            else:
                self.form.add_radio(False)
                self.form.add_text(self.jof.joboffer.license_met_reason)
        else:
            # not applicable
            #  TODO: 需要增加对N/A的处理。 form control，application form和json maker需要修改
            self.form.add_radio(False)
            self.form.add_skip(1)

    def recruit(self):
        ads = Advertisements(self.jof.advertisement)
        interviews = InterviewRecords(self.jof.interviewrecord)
        recruited = True if ads.amount > 0 else False
        if recruited:
            self.form.add_radio(True)
            self.form.add_text(interviews.resume_num)
            self.form.add_text(ads.min_days)
            self.form.add_text(interviews.summary)
            self.form.add_text(self.jof.personalassess.why_qualified_say)
            self.form.add_text(self.jof.recruitmentsummary.reasons_not_hire_canadians)
            self.form.add_skip(1)
        else:
            self.form.add_radio(False)
            self.form.add_skip(6)

    def sign(self):
        contact = Contacts(self.jof.contact).primary
        # messy skip in pdf
        self.form.add_text(contact.last_name)
        self.form.add_text(contact.position)
        self.form.add_skip(21)
        self.form.add_text(contact.first_name)
        self.form.add_text(date.today().strftime("%d-%b-%Y"))

    def get_form(self):
        self.start()
        self.employee()
        self.employer()
        self.joboffer()
        self.tech()
        self.position()
        self.recruit()
        self.sign()
        return self.form
