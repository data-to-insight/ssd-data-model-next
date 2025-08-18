# HEALTH ERD

![HEALTH ERD](../assets/images/erd_health.svg)

[View full image](../assets/images/erd_health.svg)  |  [Download SVG](../assets/images/erd_health.svg)  |  [Download DOT file](../dot/erd_health.dot)

## Table Field Previews

**Tables in domain:** 9

<details>
<summary><strong>ssd_address</strong></summary>

<table>
<thead>
<tr><th>Field</th><th>Type</th><th>Notes</th></tr>
</thead>
<tbody>
<tr><td>addr_table_id</td><td>nvarchar</td><td>PK</td></tr>
<tr><td>addr_address_json</td><td>nvarchar</td><td></td></tr>
<tr><td>addr_person_id</td><td>nvarchar</td><td>FK → <a href="#ssd_person">ssd_person</a></td></tr>
<tr><td>addr_address_type</td><td>nvarchar</td><td></td></tr>
<tr><td>addr_address_start_date</td><td>datetime</td><td></td></tr>
<tr><td>addr_address_end_date</td><td>datetime</td><td></td></tr>
<tr><td>addr_address_postcode</td><td>nvarchar</td><td></td></tr>
</tbody>
</table>

</details>

<details>
<summary><strong>ssd_cla_health</strong></summary>

<table>
<thead>
<tr><th>Field</th><th>Type</th><th>Notes</th></tr>
</thead>
<tbody>
<tr><td>clah_health_check_id</td><td>nvarchar</td><td>PK</td></tr>
<tr><td>clah_person_id</td><td>nvarchar</td><td>FK → ssd_cla_episodes</td></tr>
<tr><td>clah_health_check_type</td><td>nvarchar</td><td></td></tr>
<tr><td>clah_health_check_date</td><td>datetime</td><td></td></tr>
<tr><td>clah_health_check_status</td><td>nvarchar</td><td></td></tr>
</tbody>
</table>

</details>

<details>
<summary><strong>ssd_cla_immunisations</strong></summary>

<table>
<thead>
<tr><th>Field</th><th>Type</th><th>Notes</th></tr>
</thead>
<tbody>
<tr><td>clai_person_id</td><td>nvarchar</td><td>FK → ssd_cla_episodes</td></tr>
<tr><td>clai_immunisations_status</td><td>nchar</td><td></td></tr>
<tr><td>clai_immunisations_status_date</td><td>datetime</td><td></td></tr>
</tbody>
</table>

</details>

<details>
<summary><strong>ssd_cla_substance_misuse</strong></summary>

<table>
<thead>
<tr><th>Field</th><th>Type</th><th>Notes</th></tr>
</thead>
<tbody>
<tr><td>clas_substance_misuse_id</td><td>nvarchar</td><td>PK</td></tr>
<tr><td>clas_person_id</td><td>nvarchar</td><td>FK → ssd_cla_episodes</td></tr>
<tr><td>clas_substance_misuse_date</td><td>datetime</td><td></td></tr>
<tr><td>clas_substance_misused</td><td>nchar</td><td></td></tr>
<tr><td>clas_intervention_received</td><td>nchar</td><td></td></tr>
</tbody>
</table>

</details>

<details>
<summary><strong>ssd_disability</strong></summary>

<table>
<thead>
<tr><th>Field</th><th>Type</th><th>Notes</th></tr>
</thead>
<tbody>
<tr><td>disa_person_id</td><td>nvarchar</td><td>FK → <a href="#ssd_person">ssd_person</a></td></tr>
<tr><td>disa_table_id</td><td>nvarchar</td><td>PK</td></tr>
<tr><td>disa_disability_code</td><td>nvarchar</td><td></td></tr>
</tbody>
</table>

</details>

<details>
<summary><strong>ssd_immigration_status</strong></summary>

<table>
<thead>
<tr><th>Field</th><th>Type</th><th>Notes</th></tr>
</thead>
<tbody>
<tr><td>immi_person_id</td><td>nvarchar</td><td>FK → <a href="#ssd_person">ssd_person</a></td></tr>
<tr><td>immi_immigration_status_id</td><td>nvarchar</td><td>PK</td></tr>
<tr><td>immi_immigration_status</td><td>nvarchar</td><td></td></tr>
<tr><td>immi_immigration_status_start_date</td><td>datetime</td><td></td></tr>
<tr><td>immi_immigration_status_end_date</td><td>datetime</td><td></td></tr>
</tbody>
</table>

</details>

<details>
<summary><strong>ssd_linked_identifiers</strong></summary>

<table>
<thead>
<tr><th>Field</th><th>Type</th><th>Notes</th></tr>
</thead>
<tbody>
<tr><td>link_table_id</td><td>nvarchar</td><td>PK</td></tr>
<tr><td>link_person_id</td><td>nvarchar</td><td>FK → <a href="#ssd_person">ssd_person</a></td></tr>
<tr><td>link_identifier_type</td><td>nvarchar</td><td></td></tr>
<tr><td>link_identifier_value</td><td>nvarchar</td><td></td></tr>
<tr><td>link_valid_from_date</td><td>datetime</td><td></td></tr>
<tr><td>link_valid_to_date</td><td>datetime</td><td></td></tr>
</tbody>
</table>

</details>

<details>
<summary><strong>ssd_person</strong></summary>

<table>
<thead>
<tr><th>Field</th><th>Type</th><th>Notes</th></tr>
</thead>
<tbody>
<tr><td>pers_person_id</td><td>nvarchar</td><td>PK</td></tr>
<tr><td>pers_sex</td><td>nvarchar</td><td></td></tr>
<tr><td>pers_gender</td><td>nvarchar</td><td></td></tr>
<tr><td>pers_ethnicity</td><td>nvarchar</td><td></td></tr>
<tr><td>pers_dob</td><td>datetime</td><td></td></tr>
<tr><td>pers_common_child_id</td><td>nvarchar</td><td></td></tr>
<tr><td>pers_legacy_id</td><td>nvarchar</td><td></td></tr>
<tr><td>pers_upn_unknown</td><td>nvarchar</td><td></td></tr>
<tr><td>pers_send_flag</td><td>nchar</td><td></td></tr>
<tr><td>pers_expected_dob</td><td>datetime</td><td></td></tr>
<tr><td>pers_death_date</td><td>datetime</td><td></td></tr>
<tr><td>pers_is_mother</td><td>nchar</td><td></td></tr>
<tr><td>pers_nationality</td><td>nvarchar</td><td></td></tr>
</tbody>
</table>

</details>

<details>
<summary><strong>ssd_voice_of_child</strong></summary>

<table>
<thead>
<tr><th>Field</th><th>Type</th><th>Notes</th></tr>
</thead>
<tbody>
<tr><td>voch_table_id</td><td>nvarchar</td><td>PK</td></tr>
<tr><td>voch_person_id</td><td>nvarchar</td><td>FK → <a href="#ssd_person">ssd_person</a></td></tr>
<tr><td>voch_explained_worries</td><td>nchar</td><td></td></tr>
<tr><td>voch_story_help_understand</td><td>nchar</td><td></td></tr>
<tr><td>voch_agree_worker</td><td>nchar</td><td></td></tr>
<tr><td>voch_plan_safe</td><td>nchar</td><td></td></tr>
<tr><td>voch_tablet_help_explain</td><td>nchar</td><td></td></tr>
</tbody>
</table>

</details>

