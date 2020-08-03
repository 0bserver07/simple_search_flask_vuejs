
## Developing a Search and Index based web dashboard
### Using a single page app with flask and vue.js


## Want to use this project?

1. Fork/Clone

1. Run the server-side Flask app in one terminal window:

    ```sh
    $ cd server
    $ python3.7 -m venv env
    $ source env/bin/activate
    (env)$ pip install -r requirements.txt
    (env)$ python server.py
    ```

    Navigate to [http://localhost:5000](http://localhost:5000)

1. Run the client-side Vue app in a different terminal window:

    ```sh
    $ cd client
    $ npm install
    $ npm run serve
    ```

    Navigate to [http://localhost:8080](http://localhost:8080)




### Tasks:

  - [ ] Find CMS-1500, ICD Codes and Patient Data (anonymized)
  - [ ] Combine and generate a proper dataset.
  - [ ] Create Frontend interface with custom filters
  - [ ] Create Backend API to provide data and heavy filter (search)
  - [ ] Create index based lookup (elasticsearch or pickle the dictionaries)
  - [ ] Update documentation


-----

### Outcomes:

### Data:

- According to Herman et al. the following is the minimum relevant to follow a health record to be used with the CMS-1500 [Ref 2]:

> From Table-1 Below

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

- Data extracted from Big Query for CMS medicare claims, (Synthetic Data) [Ref 3]:

```

 ['provider_id', 'provider_name', 'provider_street_address',
  'provider_city', 'provider_state', 'provider_zipcode',
 'drg_definition', 'hospital_referral_region_description',
 'total_discharges', 'average_covered_charges',
 'average_total_payments', 'average_medicare_payments',
 'cpt_code', 'cpt_desc', 'icd1010_code', 'icd_desc']
```

- ICD Preocudre codes from the CDC data gov.

```
A000    Cholera due to Vibrio cholerae 01, biovar cholerae
A001    Cholera due to Vibrio cholerae 01, biovar eltor
```




-------

## references:

1. CPT 4 Codes, found on Github: https://gist.github.com/lieldulev/439793dc3c5a6613b661c33d71fdd185
2. "Measuring Price Dynamics: A Guide to Understanding Payer-Physician Claims Data" Douglas A. Herman.
3. cms synthetic patient data omop [link](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=cms_synthetic_patient_data_omop&t=care_site&page=table&project=keen-vision-285016&folder=&organizationId=)
