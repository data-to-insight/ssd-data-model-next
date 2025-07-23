# IDENTITY ERD

![IDENTITY ERD](../assets/images/erd_identity.svg)

[View full image](../assets/images/erd_identity.svg)  |  [Download SVG](../assets/images/erd_identity.svg)  |  [Download DOT file](../dot/erd_identity.dot)

## Table Field Previews

**Tables in domain:** 22

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
<summary><strong>ssd_cla_care_plan</strong></summary>

<table>
<thead>
<tr><th>Field</th><th>Type</th><th>Notes</th></tr>
</thead>
<tbody>
<tr><td>lacp_table_id</td><td>nvarchar</td><td>PK</td></tr>
<tr><td>lacp_person_id</td><td>nvarchar</td><td>FK → <a href="#ssd_cla_episodes">ssd_cla_episodes</a></td></tr>
<tr><td>lacp_cla_care_plan_start_date</td><td>datetime</td><td></td></tr>
<tr><td>lacp_cla_care_plan_end_date</td><td>datetime</td><td></td></tr>
<tr><td>lacp_cla_care_plan_json</td><td>nvarchar</td><td></td></tr>
</tbody>
</table>

</details>

<details>
<summary><strong>ssd_cla_convictions</strong></summary>

<table>
<thead>
<tr><th>Field</th><th>Type</th><th>Notes</th></tr>
</thead>
<tbody>
<tr><td>clac_cla_conviction_id</td><td>nvarchar</td><td>PK</td></tr>
<tr><td>clac_person_id</td><td>nvarchar</td><td>FK → <a href="#ssd_cla_episodes">ssd_cla_episodes</a></td></tr>
<tr><td>clac_cla_conviction_date</td><td>datetime</td><td></td></tr>
<tr><td>clac_cla_conviction_offence</td><td>nvarchar</td><td></td></tr>
</tbody>
</table>

</details>

<details>
<summary><strong>ssd_cla_episodes</strong></summary>

<table>
<thead>
<tr><th>Field</th><th>Type</th><th>Notes</th></tr>
</thead>
<tbody>
<tr><td>clae_cla_episode_id</td><td>nvarchar</td><td>PK</td></tr>
<tr><td>clae_person_id</td><td>nvarchar</td><td>FK → <a href="#ssd_person">ssd_person</a></td></tr>
<tr><td>clae_cla_episode_start_date</td><td>datetime</td><td></td></tr>
<tr><td>clae_cla_episode_start_reason</td><td>nvarchar</td><td></td></tr>
<tr><td>clae_cla_primary_need_code</td><td>nvarchar</td><td></td></tr>
<tr><td>clae_cla_episode_ceased_date</td><td>datetime</td><td></td></tr>
<tr><td>clae_cla_episode_ceased_reason</td><td>nvarchar</td><td></td></tr>
<tr><td>clae_cla_id</td><td>nvarchar</td><td></td></tr>
<tr><td>clae_referral_id</td><td>nvarchar</td><td></td></tr>
<tr><td>clae_cla_placement_id</td><td>nvarchar</td><td>FK → ssd_cla_placements</td></tr>
<tr><td>clae_entered_care_date</td><td>datetime</td><td></td></tr>
<tr><td>clae_cla_last_iro_contact_date</td><td>datetime</td><td></td></tr>
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
<tr><td>clah_person_id</td><td>nvarchar</td><td>FK → <a href="#ssd_cla_episodes">ssd_cla_episodes</a></td></tr>
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
<tr><td>clai_person_id</td><td>nvarchar</td><td>FK → <a href="#ssd_cla_episodes">ssd_cla_episodes</a></td></tr>
<tr><td>clai_immunisations_status</td><td>nchar</td><td></td></tr>
<tr><td>clai_immunisations_status_date</td><td>datetime</td><td></td></tr>
</tbody>
</table>

</details>

<details>
<summary><strong>ssd_cla_placement</strong></summary>

<table>
<thead>
<tr><th>Field</th><th>Type</th><th>Notes</th></tr>
</thead>
<tbody>
<tr><td>clap_cla_placement_id</td><td>nvarchar</td><td>PK</td></tr>
<tr><td>clap_cla_placement_start_date</td><td>datetime</td><td></td></tr>
<tr><td>clap_cla_placement_type</td><td>nvarchar</td><td></td></tr>
<tr><td>clap_cla_placement_urn</td><td>nvarchar</td><td></td></tr>
<tr><td>clap_cla_placement_distance</td><td>float</td><td></td></tr>
<tr><td>clap_cla_id</td><td>nvarchar</td><td>FK → <a href="#ssd_cla_episodes">ssd_cla_episodes</a></td></tr>
<tr><td>clap_cla_placement_provider</td><td>nvarchar</td><td></td></tr>
<tr><td>clap_cla_placement_postcode</td><td>nvarchar</td><td></td></tr>
<tr><td>clap_cla_placement_end_date</td><td>datetime</td><td></td></tr>
<tr><td>clap_cla_placement_change_reason</td><td>nvarchar</td><td></td></tr>
<tr><td>clap_person_id</td><td>nvarchar</td><td></td></tr>
</tbody>
</table>

</details>

<details>
<summary><strong>ssd_cla_previous_permanence</strong></summary>

<table>
<thead>
<tr><th>Field</th><th>Type</th><th>Notes</th></tr>
</thead>
<tbody>
<tr><td>lapp_table_id</td><td>nvarchar</td><td>PK</td></tr>
<tr><td>lapp_person_id</td><td>nvarchar</td><td>FK → <a href="#ssd_cla_episodes">ssd_cla_episodes</a></td></tr>
<tr><td>lapp_previous_permanence_order_date</td><td>nvarchar</td><td></td></tr>
<tr><td>lapp_previous_permanence_option</td><td>nvarchar</td><td></td></tr>
<tr><td>lapp_previous_permanence_la</td><td>nvarchar</td><td></td></tr>
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
<tr><td>clas_person_id</td><td>nvarchar</td><td>FK → <a href="#ssd_cla_episodes">ssd_cla_episodes</a></td></tr>
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
<summary><strong>ssd_ehcp_requests</strong></summary>

<table>
<thead>
<tr><th>Field</th><th>Type</th><th>Notes</th></tr>
</thead>
<tbody>
<tr><td>ehcr_ehcp_request_id</td><td>nvarchar</td><td>PK</td></tr>
<tr><td>ehcr_send_table_id</td><td>nvarchar</td><td>FK → <a href="#ssd_send">ssd_send</a></td></tr>
<tr><td>ehcr_ehcp_req_date</td><td>datetime</td><td></td></tr>
<tr><td>ehcr_ehcp_req_outcome_date</td><td>datetime</td><td></td></tr>
<tr><td>ehcr_ehcp_req_outcome</td><td>nvarchar</td><td></td></tr>
</tbody>
</table>

</details>

<details>
<summary><strong>ssd_family</strong></summary>

<table>
<thead>
<tr><th>Field</th><th>Type</th><th>Notes</th></tr>
</thead>
<tbody>
<tr><td>fami_table_id</td><td>nvarchar</td><td></td></tr>
<tr><td>fami_family_id</td><td>nvarchar</td><td>PK</td></tr>
<tr><td>fami_person_id</td><td>nvarchar</td><td>FK → <a href="#ssd_person">ssd_person</a></td></tr>
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
<summary><strong>ssd_legal_status</strong></summary>

<table>
<thead>
<tr><th>Field</th><th>Type</th><th>Notes</th></tr>
</thead>
<tbody>
<tr><td>lega_legal_status_id</td><td>nvarchar</td><td>PK</td></tr>
<tr><td>lega_person_id</td><td>nvarchar</td><td>FK → <a href="#ssd_person">ssd_person</a></td></tr>
<tr><td>lega_legal_status</td><td>nvarchar</td><td></td></tr>
<tr><td>lega_legal_status_start_date</td><td>datetime</td><td></td></tr>
<tr><td>lega_legal_status_end_date</td><td>datetime</td><td></td></tr>
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
<summary><strong>ssd_missing</strong></summary>

<table>
<thead>
<tr><th>Field</th><th>Type</th><th>Notes</th></tr>
</thead>
<tbody>
<tr><td>miss_table_id</td><td>nvarchar</td><td>PK</td></tr>
<tr><td>miss_person_id</td><td>nvarchar</td><td>FK → <a href="#ssd_person">ssd_person</a></td></tr>
<tr><td>miss_missing_episode_start_date</td><td>datetime</td><td></td></tr>
<tr><td>miss_missing_episode_type</td><td>nvarchar</td><td></td></tr>
<tr><td>miss_missing_episode_end_date</td><td>datetime</td><td></td></tr>
<tr><td>miss_missing_rhi_offered</td><td>nvarchar</td><td></td></tr>
<tr><td>miss_missing_rhi_accepted</td><td>nvarchar</td><td></td></tr>
</tbody>
</table>

</details>

<details>
<summary><strong>ssd_mother</strong></summary>

<table>
<thead>
<tr><th>Field</th><th>Type</th><th>Notes</th></tr>
</thead>
<tbody>
<tr><td>moth_table_id</td><td>nvarchar</td><td>PK</td></tr>
<tr><td>moth_person_id</td><td>nvarchar</td><td>FK → <a href="#ssd_person">ssd_person</a></td></tr>
<tr><td>moth_childs_person_id</td><td>nvarchar</td><td>PK; FK → <a href="#ssd_person">ssd_person</a></td></tr>
<tr><td>moth_childs_dob</td><td>datetime</td><td></td></tr>
</tbody>
</table>

</details>

<details>
<summary><strong>ssd_permanence</strong></summary>

<table>
<thead>
<tr><th>Field</th><th>Type</th><th>Notes</th></tr>
</thead>
<tbody>
<tr><td>perm_table_id</td><td>nvarchar</td><td>PK</td></tr>
<tr><td>perm_person_id</td><td>nvarchar</td><td>FK → <a href="#ssd_cla_episodes">ssd_cla_episodes</a></td></tr>
<tr><td>perm_cla_id</td><td>nvarchar</td><td></td></tr>
<tr><td>perm_adm_decision_date</td><td>datetime</td><td></td></tr>
<tr><td>perm_ffa_cp_decision_date</td><td>datetime</td><td></td></tr>
<tr><td>perm_placement_order_date</td><td>datetime</td><td></td></tr>
<tr><td>perm_placed_for_adoption_date</td><td>datetime</td><td></td></tr>
<tr><td>perm_matched_date</td><td>datetime</td><td></td></tr>
<tr><td>perm_adopted_by_carer_flag</td><td>nchar</td><td></td></tr>
<tr><td>perm_placed_ffa_cp_date</td><td>datetime</td><td></td></tr>
<tr><td>perm_decision_reversed_date</td><td>datetime</td><td></td></tr>
<tr><td>perm_placed_foster_carer_date</td><td>datetime</td><td></td></tr>
<tr><td>perm_part_of_sibling_group</td><td>nchar</td><td></td></tr>
<tr><td>perm_siblings_placed_together</td><td>int</td><td></td></tr>
<tr><td>perm_siblings_placed_apart</td><td>int</td><td></td></tr>
<tr><td>perm_placement_provider_urn</td><td>nvarchar</td><td></td></tr>
<tr><td>perm_decision_reversed_reason</td><td>nvarchar</td><td></td></tr>
<tr><td>perm_permanence_order_date</td><td>datetime</td><td></td></tr>
<tr><td>perm_permanence_order_type</td><td>nvarchar</td><td></td></tr>
<tr><td>perm_adoption_worker_id</td><td>nvarchar</td><td>FK → ssd_professionals</td></tr>
<tr><td>perm_adopter_sex</td><td>nvarchar</td><td></td></tr>
<tr><td>perm_adopter_legal_status</td><td>nvarchar</td><td></td></tr>
<tr><td>perm_number_of_adopters</td><td>nvarchar</td><td></td></tr>
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
<summary><strong>ssd_sdq_scores</strong></summary>

<table>
<thead>
<tr><th>Field</th><th>Type</th><th>Notes</th></tr>
</thead>
<tbody>
<tr><td>csdq_table_id</td><td>nvarchar</td><td>PK</td></tr>
<tr><td>csdq_person_id</td><td>nvarchar</td><td>FK → <a href="#ssd_cla_episodes">ssd_cla_episodes</a></td></tr>
<tr><td>csdq_sdq_completed_date</td><td>datetime</td><td></td></tr>
<tr><td>csdq_sdq_reason</td><td>nvarchar</td><td></td></tr>
<tr><td>csdq_sdq_score</td><td>nvarchar</td><td></td></tr>
</tbody>
</table>

</details>

<details>
<summary><strong>ssd_send</strong></summary>

<table>
<thead>
<tr><th>Field</th><th>Type</th><th>Notes</th></tr>
</thead>
<tbody>
<tr><td>send_table_id</td><td>nvarchar</td><td>PK</td></tr>
<tr><td>send_upn</td><td>nvarchar</td><td></td></tr>
<tr><td>send_uln</td><td>nvarchar</td><td></td></tr>
<tr><td>send_upn_unknown</td><td>nvarchar</td><td></td></tr>
<tr><td>send_person_id</td><td>nvarchar</td><td>FK → <a href="#ssd_person">ssd_person</a></td></tr>
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

