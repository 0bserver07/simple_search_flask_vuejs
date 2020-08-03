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
        # icd10_code = random.choice(list(icd10_codes_dict.keys()))

        # little gimmick to have repeated icd codes:
        icd10_code = random.choice(list(icd10_codes_dict.keys())[:30])
        # print(cpt_codes_dict[cpt_code], icd10_codes_dict[icd10_code])
        d1 = {'cpt_code': cpt_code, 'cpt_desc': cpt_codes_dict[cpt_code]}
        d2 = {'icd1010_code': icd10_code, 'icd_desc': icd10_codes_dict[icd10_code]}
        row.update(d1)
        row.update(d2)

    return data




dataset = bigQuery_loader()


with open('../data/data_combined.json', 'w') as json_file:
  json.dump(dataset, json_file)


# ['provider_id', 'provider_name', 'provider_street_address',
#  'provider_city', 'provider_state', 'provider_zipcode',
# 'drg_definition', 'hospital_referral_region_description',
# 'total_discharges', 'average_covered_charges',
# 'average_total_payments', 'average_medicare_payments',
# 'cpt_code', 'cpt_desc', 'icd1010_code', 'icd_desc']

# Usable:
# provider_name
# provider_street_address
# provider_city
# drg_definition
# hospital_referral_region_description
# total_discharges
# average_covered_charges
# average_total_payments
# average_medicare_payments
# cpt_code
# cpt_desc
# icd1010_code
# icd_desc
