from pathlib import Path
from bin.config import Config

current_path = Path(__file__)
DATADIR = current_path.parents[1] / "data"

title = ["Argument", "Value", "Remark"]
make = [
    "-m",
    "excel_name",
    "Make excel based on the model and this excel name, with or without '.xlsx'",
]
check = [
    "-c",
    "excel_name",
    "Check this excel data based on the model, with or without '.xlsx'",
]

excel = [
    "-e",
    "excel_name",
    "Data source excel name, with or without '.xlsx'",
]
document_lmia = [
    "-d",
    "rs, et,sl",
    "Document type. rs: Recruitment Summary, et:Employer Training,sl:Submission Letter",
]
document_exp = [
    "-d",
    "rs, ec",
    "Document type. rs: Resume, ec:Employment Certificate",
]
document_exp_rs = [
    "-d",
    "rs,",
    "Document type. rs: Resume",
]
word = [
    "-w",
    "word_filename",
    "Output word file name with either ext or not",
]
webform = [
    "-wf",
    "filename",
    "Make json file for filling web form",
]

upload = [
    "-u",
    "upload_dir_name",
    "Upload dir name for uploading files in web form",
]
template_number = [
    "-tn",
    "template_number",
    "Template number for docx templates. Default is 1",
]

helps = {
    "5593": [
        title,
        make,
        check,
        excel,
        document_lmia,
        word,
        webform,
        upload,
    ],
    "5626": [
        title,
        make,
        check,
        excel,
        document_lmia,
        word,
        webform,
        upload,
    ],
    "5627": [
        title,
        make,
        check,
        excel,
        document_lmia,
        word,
        webform,
        upload,
    ],
    "exp": [title, make, check, excel, document_exp, template_number, word],
    "exp-rs":[title,make,check,excel,document_exp_rs,template_number,word]
}


def get_models(
    rcic_company_id_name: str = Config.rcic_company_id_name,
    temp_num: int = Config.default_template_number,
):
    models = {
        # Experience for resume and employment certificate
        "exp": {
            "path": "model.experience.experience",
            "class_list": ["ExperienceModel"],
            "remark": "Experience module for Employment Certificate model",
            "docx_template": {
                "ec": DATADIR / "word" / "employment_certificate.docx",
                "rs": DATADIR / "word" / f"resume-regular{temp_num}.docx",
            },
            "help": {
                "description": "This model can make and check excel model, and generate resume and employment certificate docx ",
                "helps": helps["exp"],
            },
        },
        "exp-rs": {
            "path": "model.experience.resume",
            "class_list": ["ResumeModel"],
            "remark": "Experience module for Resume model",
            "docx_template": {
                "rs": DATADIR / "word" / f"resume-regular{temp_num}.docx",
            },
            "help": {
                "description": "This model can make and check excel model, and generate resume and employment certificate docx ",
                "helps": helps["exp-rs"],
            },
        },
        # Recruitment
        "recruit-ja": {
            "path": "model.recruit.jobad",
            "class_list": ["JobadModel"],
            "remark": "Recruit module for Job Advertisement model",
        },
        "recruit-jo": {
            "path": "model.recruit.joboffer",
            "class_list": ["JobofferModel"],
            "remark": "Recruitment module for Job Offer model",
        },
        "recruit-rs": {
            "path": "model.recruit.recruitmentsummary",
            "class_list": ["RecruitmnetSummaryModel"],
            "remark": "Recruitment module for Recruitment Summary model",
        },
        # LMIA
        "lmia-st1": {
            "path": "model.lmia.stage1",
            "class_list": ["LmiaAssess"],
            "remark": "LMIA module for stage 1 model (assessment)",
        },
        "lmia-st2": {
            "path": "model.lmia.stage2",
            "class_list": ["LmiaRecruitment"],
            "remark": "LMIA module for stage 2 model (recruitment)",
        },
        "lmia-st3": {
            "path": "model.lmia.stage3",
            "class_list": ["LmiaApplication"],
            "remark": "LMIA module for for stage 3 model (application)",
        },
        "lmia-rcic": {
            "path": "model.lmia.rcic",
            "class_list": ["LmiaRcic"],
            "remark": "LMIA module for RCIC model (Plannning)",
        },
        "lmia-5593": {
            "path": "model.lmia.m5593",
            "class_list": ["M5593Model"],
            "docx_template": {
                "rs": DATADIR / "word" / "lmia-rs.docx",
                "et": DATADIR / "word" / "5593-et.docx",
                "sl": DATADIR / "word" / f"5593-sl-{rcic_company_id_name}.docx",
            },
            "remark": "LMIA module for EE doc generation application",
            "help": {
                "description": "This model can automatically make docx, and make json file for filling web form ",
                "helps": helps["5593"],
            },
        },
        "lmia-5626": {
            "path": "model.lmia.m5626",
            "class_list": ["M5626Model"],
            "docx_template": {
                "rs": DATADIR / "word" / "lmia-rs.docx",
                "et": DATADIR / "word" / "5626-et.docx",
                "sl": DATADIR / "word" / f"5626-sl-{rcic_company_id_name}.docx",
            },
            "remark": "LMIA module for HWS application",
            "help": {
                "description": "This model can automatically make docx, and make json file for filling web form ",
                "helps": helps["5626"],
            },
        },
        "lmia-5627": {
            "path": "model.lmia.m5627",
            "class_list": ["M5627Model"],
            "docx_template": {
                "rs": DATADIR / "word" / "lmia-rs.docx",
                "et": DATADIR / "word" / "5627-et.docx",
                "sl": DATADIR / "word" / f"5627-sl-{rcic_company_id_name}.docx",
            },
            "remark": "LMIA module for LWS application",
            "help": {
                "description": "This model can automatically make docx, and make json file for filling web form ",
                "helps": helps["5627"],
            },
        },
        # BCPNP
        "bcpnp-ert": {
            "path": "model.bcpnp.employertraining",
            "class_list": ["EmployerTrainingModel"],
            "remark": "BCPNP module for Employer Training model",
        },
        "bcpnp-eet": {
            "path": "model.bcpnp.employeetraining",
            "class_list": ["EmployeeTrainingModel"],
            "remark": "BCPNP module for Employee Training model",
        },
        "bcpnp-jd": {
            "path": "model.bcpnp.jobdescription",
            "class_list": ["JobDescriptionModel"],
            "remark": "BCPNP module for Job Description model",
        },
        "bcpnp-jof": {
            "path": "model.bcpnp.jobofferform",
            "class_list": ["JobOfferFormModel"],
            "remark": "BCPNP module for Job Offer Form model",
        },
        "bcpnp-rl": {
            "path": "model.bcpnp.recommendationletter",
            "class_list": ["RecommendationLetterModel"],
            "remark": "BCPNP module for Recommendation Letter model",
        },
        "bcpnp-rpf": {
            "path": "model.bcpnp.repform",
            "class_list": ["RepFormModel"],
            "remark": "BCPNP module for Representative Form model",
        },
        "bcpnp-reg": {
            "path": "webform.bcpnp.bcpnpmodel_reg",
            "class_list": ["BcpnpModelReg"],
            "remark": "BCPNP module for BCPNP Registration model",
        },
        "bcpnp-reg-ee": {
            "path": "webform.bcpnp.bcpnpmodel_reg",
            "class_list": ["BcpnpEEModelReg"],
            "remark": "BCPNP module for BCPNP Registration model(EE)",
        },
        "bcpnp-app": {
            "path": "webform.bcpnp.bcpnpmodel_app",
            "class_list": ["BcpnpModelApp"],
            "remark": "BCPNP module for BCPNP Application model",
        },
        "bcpnp-app-ee": {
            "path": "webform.bcpnp.bcpnpmodel_app",
            "class_list": ["BcpnpEEModelApp"],
            "remark": "BCPNP module for BCPNP application (EE) model",
        },
        # PR
        "0008": {
            "path": "model.pr.m0008",
            "class_list": ["M0008Model"],
            "remark": "PR module for form 0008 model",
        },
        "5406": {
            "path": "model.pr.m5406",
            "class_list": ["M5406Model"],
            "remark": "PR module for form 5406 model",
        },
        "5562": {
            "path": "model.pr.m5562",
            "class_list": ["M5562Model"],
            "remark": "PR module for form 5562 model",
        },
        "5669": {
            "path": "model.pr.m5669",
            "class_list": ["M5669Model"],
            "remark": "PR module for form 5669 model",
        },
        "pr": {
            "path": "webform.prportal.prmodel",
            "class_list": ["PrModel"],
            "remark": "PR module for all PR model",
        },
        # TR
        "0104": {
            "path": "model.tr.m0104",
            "class_list": ["M0104Model"],
            "remark": "TR module for form 0104 model",
        },
        "1294": {
            "path": "model.tr.m1294",
            "class_list": ["M1294Model"],
            "remark": "TR module for form 1294 model",
        },
        "1295": {
            "path": "model.tr.m1295",
            "class_list": ["M1295Model"],
            "remark": "TR module for form 1295 model",
        },
        "5257": {
            "path": "model.tr.m5257",
            "class_list": ["M5257Model"],
            "remark": "TR module for form 5257 model",
        },
        "5708": {
            "path": "model.tr.m5708",
            "class_list": ["M5708Model"],
            "docx_template": {
                "sl": DATADIR / "word" / f"{rcic_company_id_name}-5708-sl.docx"
            },
            "remark": "TR module for form 5708 model",
        },
        "5709": {
            "path": "model.tr.m5709",
            "class_list": ["M5709Model"],
            "remark": "TR module for form 5709 model",
        },
        "5710": {
            "path": "model.tr.m5710",
            "class_list": ["M5710Model"],
            "remark": "TR module for form 5710 model",
        },
        "5476": {
            "path": "model.common.m5476",
            "class_list": ["M5476Model"],
            "remark": "Rep form",
        },
    }

    return models
