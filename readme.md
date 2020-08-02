### Backend API


### Goals:

### Tasks:

data sample generated:

```
 {'average_covered_charges': 14812.06,
  'average_medicare_payments': 2873.44,
  'average_total_payments': 4545.61,
  'cpt_code': '64449',
  'cpt_desc': 'N block inj, lumbar plexus',
  'drg_definition': '392 - ESOPHAGITIS, GASTROENT & MISC DIGEST DISORDERS W/O '
                    'MCC',
  'hospital_referral_region_description': 'IN - Gary',
  'icd1010_code': 'V0211XS',
  'icd_desc': 'V0211XS Pedestrian on roller-skates injured in collision with '
              'two- or three-wheeled motor vehicle in traffic accident, '
              'sequela\n',
  'provider_city': 'CROWN POINT',
  'provider_id': '150166',
  'provider_name': 'PINNACLE HOSPITAL',
  'provider_state': 'IN',
  'provider_street_address': '9301 CONNECTICUT DR',
  'provider_zipcode': 46307,
  'total_discharges': 18}
  ```



- minimum data needed for cms-1500

```

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

```


## data sources:

- https://gist.github.com/lieldulev/439793dc3c5a6613b661c33d71fdd185
-