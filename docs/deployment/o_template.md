# SSD Deployment — [cms type]

This is a holding page for resources that support deployment of the **SSD Standard Safeguarding Dataset (SSD)** within local authority case management systems (CMS).

> Linked resources/scripts/repo are specifically for authorities using **[cms type]**  

## Accessing the [cms type] Release

The current version of deployment script(s) available at the following GitHub link:

[View [cms type] SSD Release](https://github.com/data-to-insight/ssd-data-model/tree/main/deployment_extracts/[cms type]/live)

Please note:
- This is a **private repository link**.  
- Local authorities or sector colleagues interested in accessing are encouraged to **request access** via [datatoinsight.enquiries@gmail.com](mailto:datatoinsight.enquiries@gmail.com)

---

## Development Partners

This release has been developed with assistance and collaboration from:
- Local Authorities enabling testing: 
- ~90+ CSC Sector colleagues via focus groups centred on defining the scope of the SSD
- Data to Insight (Dev Lead)

---

## Deployment Requirements

| Requirement         | Details                                   |
|---------------------|--------------------------------------------|
| **Database Type**   | SQL Server / Oracle / PostgreSQL (varies by CMS) |
| **Minimum DB Version** | 2016+ (SQL Server), 12c+ (Oracle), 12+ (PostgreSQL) |
| **DB Permissions**  | `CREATE TABLE`, `DROP TABLE`, `CREATE INDEX`, `DROP INDEX` |
| **Environment**     | Access to CMS reporting layer or replica db |
| **Automation**      | Optional: Local ETL scripting or scheduled job setup |

---

## Release Status

| Version | Status     | Notes                               |
|---------|------------|-------------------------------------|
| `v1.0`  | Live (Initial) | Deployed and tested with live local authority data |
| `v1.x+` | Planned    | Updates to follow sector feedback and SSD standard refinements |


## Release Status

| label | Status Label   | Description                                                 |
| ----- | -------------- | ----------------------------------------------------------- |
| ⭕     | In Development | Active dev phase            |
| 🟡    | Beta Testing   | Released to limited LAs/users for feedback|testing          |
| 🟢    | Released       | Stable, public release — actively supported                 |
| 🟠    | On Hold        | Pending resource or decision     |
| ⚫     | Not Available  | Not currently planned |

---


For more information about the SSD data standard and its integration into operational reporting tools, please refer to the main project repository or contact the team directly.
