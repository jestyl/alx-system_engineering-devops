Client management service (CMS)crashed
![pixlr-image-generator-54d2d33e-5dd8-4ce2-b7cf-dfbb812e58b7](https://github.com/jestyl/alx-system_engineering-devops/assets/40529386/9857d01b-3f64-491b-94f1-e510477d3c09)

Date of Incident: 10 April 2024

Issue Summary:
On 10 April 2024, from 7:30 AM to 10:00 AM PT, our Content Management System (CMS) experienced a critical outage. The incident began with a noticeable lag at 7:30 AM PT, escalating to a complete system crash by 8:00 AM PT. The outage impacted over 12,000 remote Travel Agents, preventing them from logging in or continuing their work. The root cause was identified as conflicts from recently updated plugins/extensions, resulting in a memory leak, CPU overload, and API failures.

Timeline:
- 7:30 AM: Initial lag detected by automated monitoring systems.
- 7:35 AM: First alert triggered, indicating a potential issue with CMS performance.
- 7:40 AM: Engineers began preliminary investigations focusing on server load.
- 7:55 AM: Users reported difficulties logging in, prompting escalation to senior engineers.
- 8:00 AM: CMS crashed completely, triggering a critical alert.
- 8:05 AM: Senior engineers ruled out server hardware issues and shifted focus to recent software updates.
- 8:20 AM: Misleading path: Engineers spent time checking network configurations.
- 8:35 AM: Identified unusual memory usage patterns linked to recent plugin updates.
- 8:50 AM: Decision made to disable the newly updated plugins.
- 9:00 AM: Disabled plugins, but CMS still unstable; further investigation needed.
- 9:15 AM: Discovered that memory leak persisted due to residual processes from faulty plugins.
- 9:30 AM: Cleaned up residual processes and reconfigured system resources.
- 9:45 AM: Restarted CMS to assess stability.
- 10:00 AM: CMS fully restored to normal operation after thorough system checks and patches.

Root Cause and Resolution:
Root Cause:
The outage was caused by bugs in recent updates to several CMS plugins, specifically the softphone, mail app, and terminal plugins. These bugs created a memory leak, leading to excessive CPU usage and API failures. This combination overwhelmed the server, resulting in the system becoming unresponsive.

Resolution:
The resolution process involved disabling the problematic plugins and cleaning up any residual processes causing the memory leak. Senior engineers then reconfigured system resources and applied necessary patches. The CMS was restarted and rigorously tested to ensure stability before being fully restored.



Corrective and Preventative Measures:
Improvements:
1. Enhanced Testing Protocols: Implement comprehensive testing for all plugins/extensions in a staging environment before deploying to production.
2. Advanced Automated Monitoring: Integrate additional monitoring tools focused on detecting memory leaks, CPU spikes, and API failures.
3. Rigorous Plugin Management: Establish strict guidelines for managing and updating plugins/extensions, including regular audits and controlled deployment procedures.

Specific Tasks:
- Task 1: Conduct a thorough review and patching of all existing plugins to eliminate potential bugs.
- Task 2: Deploy advanced monitoring tools capable of identifying and alerting unusual resource usage in real time.
- Task 3: Develop and enforce a robust plugin/extension management policy, ensuring regular updates and audits.
- Task 4: Train helpdesk and engineering teams on updated protocols for rapid detection and resolution of similar issues.

Conclusion:

The CMS outage on 10 April 2024 resulted in significant disruptions, affecting over 12,000 Travel Agents and causing a loss of over 35% in daily revenue typically generated between 7:30 AM and 10:00 AM PT. This incident highlighted the importance of rigorous testing, advanced monitoring, and stringent management of plugins/extensions. The swift actions taken by our engineering team to identify and resolve the root cause were critical in restoring service. Going forward, the corrective and preventative measures implemented will help ensure the stability and reliability of our CMS, minimizing the risk of future incidents.

Reported By: Jestyl Arku

Date of Report: 17 April 2024
