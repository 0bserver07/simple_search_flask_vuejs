import json
from pprint import pprint
import pandas as pd
import random


def icd10_codes_loader():
    icd10_codes_dict = {}
    with open("../data/icd10cm_codes_2021.txt") as file:
        for l in file:
            icd10_codes_dict[l.split(' ')[0]] = l
    # pprint(cdm_codes_dict)
    return icd10_codes_dict

def cpt_codes_loader():
    cpt_codes_dict = {}
    data = pd.read_csv('../data/cpt_codes.csv', index_col=1, skiprows=1).T.to_dict()
    # pprint(data)
    for key,value in data.items():
        cpt_codes_dict[list(value.values())[0]] = key
    # print(data.keys())
    # pprint(cpt_codes_dict)

    print(random.choice(list(cpt_codes_dict.keys())))
    print(random.choice(list(cpt_codes_dict.keys())))
    print(random.choice(list(cpt_codes_dict.keys())))


    return cpt_codes_dict


def bigQuery_loader():
    """[summary]
        loads a json file with bigQ data extracted via file_path
    Args:
        file_path ([str]): json file's file_path
    """
    icd10_codes_dict = icd10_codes_loader()
    cpt_codes_dict = cpt_codes_loader()

    with open('../data/inpatient_charges_2015_1500.json') as f:
        data = json.load(f)

    for row in data:
        cpt_code = random.choice(list(cpt_codes_dict.keys()))
        icd10_code = random.choice(list(icd10_codes_dict.keys()))
        # print(cpt_codes_dict[cpt_code], icd10_codes_dict[icd10_code])
        d1 = {'cpt_code': cpt_code, 'cpt_desc': cpt_codes_dict[cpt_code]}
        d2 = {'icd1010_code': icd10_code, 'icd_desc': icd10_codes_dict[icd10_code]}
        row.update(d1)
        row.update(d2)


    pprint(data)

    return data


bigQuery_loader()




#  {
#   'average_covered_charges': 14812.06,
#   'average_medicare_payments': 2873.44,
#   'average_total_payments': 4545.61,
#   'drg_definition': '392 - ESOPHAGITIS, GASTROENT & MISC DIGEST DISORDERS W/O '
#                     'MCC',
#   'hospital_referral_region_description': 'IN - Gary',
#   'provider_city': 'CROWN POINT',
#   'provider_id': '150166',
#   'provider_name': 'PINNACLE HOSPITAL',
#   'provider_state': 'IN',
#   'provider_street_address': '9301 CONNECTICUT DR',
#   'provider_zipcode': 46307,
#   'total_discharges': 18
#   'diagnosis' : '',
#   'date_of_Service' : '',
#   'place _of_service' : '',
#   'procedure' : '',
#   'days_or_units' : '',
#   'id_qualifier' : '',
#   'total_charge' : '',
#   'amount_paid' : '',
#   'insurance_plan' : '',
#
# }

# minimum data needed for cms-1500:

# 'Diagnosis'= Code identifying patient's ailment.
# 'Date of Service'= Date of service performed.
# 'Place of Service'= Type of facility where services were rendered.
# 'Procedure'= Code indicating type of service rendered;
# 'Charges'= Amount billed by provider; may not reflect price.
# 'Days or Units'= Quantity of procedure in days or units.
# 'ID Qualifier'= Identifies providers with no national ID.
# 'Provider ID'= Unique tax identifier of provider.
# 'Total Charge'= Total billed for claim; may not reflect price.
# 'Amount Paid'= Amount paid by patient; does not include insurer's payment (may not
# 'Service Location'= Address where services were rendered.
# 'Billing Provider'= Billing office address; may not be location where services rendered .
# 'Insurance Plan'= Details of insurance company and plan name.