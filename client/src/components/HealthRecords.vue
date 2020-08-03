<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-12">
        <h1>Health Records</h1>

      <div class="col-sm-6">
        <p>Select CPT Code:</p>

        <multiselect
        v-model="selectValue"
        :options="selectOptions"
        :multiple="true"
        :taggable="true"
        :custom-label="nameWithDetail"
        track-by="name"
        @select="selectedTagFilter"
        @remove="removedTagFilter"
        >
        </multiselect>


      </div>
        <br><br>
        <vue-good-table
        :lineNumbers="true"
        :columns="columns"
        :rows="health_records"
        :pagination-options="{ enabled: true, perPage: 5}"
        :search-options="{
            enabled: true,
            trigger: 'enter',
            skipDiacritics: true,
            placeholder: 'Search this table',
        }"
        theme="black-rhino"
        :paginate="true"

        >

        </vue-good-table>

      </div>
    </div>



  </div>
</template>

<script>
import axios from 'axios';

import 'vue-good-table/dist/vue-good-table.css'
import { VueGoodTable } from 'vue-good-table';

import Multiselect from "vue-multiselect";

export default {
  data() {
    return {
    selecedtValues: [],
    selectValue: [
      ],
    selectOptions:  [
      ],
    columns: [
        {
            label: "Provider",
            field: "provider_name",
        },
        {
            label: 'CPT Code',
            field: 'cpt_code',
        },
        {
            label: 'CPT Description',
            field: 'cpt_desc',
         filterOptions: {
            enabled: true,
            placeholder: "Describe CPT",
            filterFn: this.myColumnFilter
          }
        },

        {
            label: 'ICD Code',
            field: 'icd1010_code',
        },

        {
            label: 'ICD Description',
            field: 'icd_desc',
        },
        {
            label: 'Provider Address',
            field: 'provider_street_address',
        },
        {
            label: 'Drug',
            field: 'drg_definition',
            filterOptions: {
            enabled: true,
            placeholder: "Name",
          }
        },
        {
            label: 'Hospital',
            field: 'hospital_referral_region_description',
        },
        {
            label: 'Provider Address',
            field: 'provider_street_address',
        },
        {
            label: 'Provider Address',
            field: 'provider_street_address',
        },
        {
            label: 'Total Charge',
            field: 'total_discharges',
            type: 'number',
        },
      ],
      health_records: [],
    };
  },
  components: {
    VueGoodTable,
    Multiselect,

},
  methods: {

    //   multi-select style
    nameWithDetail ({ name, detail }) {
      return `${name} — [${detail}]`
    },

    // multi-select select tag call
    selectedTagFilter: function(selectedOption, id) {

        const selectedTags = JSON.parse(JSON.stringify(this.selectValue));
        selectedTags.push({name: selectedOption['name']})
        const payload = {
            tags: selectedTags,
        }
        this.updateHealthRecord(payload);
    },

    // multi-select remove tag call
    removedTagFilter: function(removedOption, id) {

       var selectedTags = JSON.parse(JSON.stringify(this.selectValue));
       selectedTags = selectedTags.filter(function( obj ) {
            return obj['name'] !== removedOption['name'];
        });

        const payload = {
          tags: selectedTags,
         }
         this.updateHealthRecord(payload);

    },

    updateHealthRecord(payload) {
    const path = 'http://localhost:5000/health_records';
    axios.post(path, payload)
        .then((res) => {
          this.health_records = res.data.health_records;
          this.selectOptions = res.data.cpt_categories;
        })
        .catch((error) => {
        // eslint-disable-next-line
            console.error(error);
            this.getHealthRecords();
        });
    },

    getHealthRecords() {
      const path = 'http://localhost:5000/health_records';
      axios.get(path)
        .then((res) => {
          this.health_records = res.data.health_records;
          this.selectOptions = res.data.cpt_categories;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },

    searchQuery(row, col, cellValue, searchTerm) {
        console.log(searchTerm)
        const path = 'http://localhost:5000/health_records';
        // get the table's search query from API
    },

  },
  created() {
    this.getHealthRecords();
  },

};
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>