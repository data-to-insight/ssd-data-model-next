# SSD Deployment — Mosaic

This is a holding page for resources that support deployment of the **SSD Standard Safeguarding Dataset (SSD)** within local authority case management systems (CMS).

> Linked resources/scripts/repo are specifically for authorities using **Mosaic**  

## Accessing the Mosaic Release

The current version of deployment script(s) available at the following GitHub link:

[View Mosaic SSD Release](https://github.com/data-to-insight/ssd-data-model/tree/main/deployment_extracts/mosaic/live)

Please note:
- This is a **private repository link**.  
- Local authorities or sector colleagues interested in accessing are encouraged to **request access** via [datatoinsight.enquiries@gmail.com](mailto:datatoinsight.enquiries@gmail.com)

---

## Development Partners

This release has been developed with assistance and collaboration from:

 - Local Authorities enabling testing: Essex, +2  
 - ~90+ CSC Sector colleagues via focus groups defining the scope of the SSD  
 - Sam Ferguson, Keith Thomas (Dev Leads)  

---

## Deployment Requirements

| Requirement         | Details                                   |
|---------------------|--------------------------------------------|
| **Database Type**   | SQL Server (We have no Oracle version atm) |
| **Minimum DB Version** | 2016+ (SQL Server) |
| **DB Permissions**  | `CREATE TABLE`, `DROP TABLE`, `CREATE INDEX`, `DROP INDEX` |
| **Environment**     | Access to CMS reporting layer or replica db |
| **Automation**      | Optional: Local ETL scripting or scheduled job setup |

---

## Release Status

| label | Status Label   | Description                                                 |
| ----- | -------------- | ----------------------------------------------------------- |
| 🟢    | Released       | Stable, public release                  |


---


For more information about the SSD data standard and its integration into operational reporting tools, please refer to the main project repository or contact the team directly.
