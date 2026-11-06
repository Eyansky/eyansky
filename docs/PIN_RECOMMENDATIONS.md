# Recommended GitHub pins

Audited 2026-11-06. The account's public repository inventory and all non-fork default-branch trees/available READMEs were inspected. Representative source and tests were read for the leading candidates. This is an evidence-based showcase review, not a full code, dependency, or security audit. Existing application test suites were not executed; the presence of tests is not a claim that they currently pass.

## Six candidates, in order

| Repository | Engineering evidence | Recommendation and limitations |
| --- | --- | --- |
| [multi-tenant-maintenance-api](https://github.com/Eyansky/multi-tenant-maintenance-api) | Django/DRF, organization-scoped access, PostgreSQL, Redis/Celery, Docker, health/readiness checks. Tests cover tenant isolation, permissions, state transitions, background tasks, and API behavior. Representative cross-organization denial tests were inspected. | Lead pin for backend and architecture roles. Replace the README's placeholder clone URL and `django-test` directory; verify the documented setup in a fresh checkout. |
| [agriweather](https://github.com/Eyansky/agriweather) | Structured AI integration with runtime response validation, bounded retries and explicit errors. Weather/image routes, localization, consent handling, documented boundaries, unit/component tests, browser tests, and CI. | Lead pin for AI and full-stack roles. The public README explains operational limitations, including in-memory rate limiting. Recheck its test and coverage claims before using numeric coverage in a job application. |
| [StackOverflow-lite](https://github.com/Eyansky/StackOverflow-lite) | Flask question/answer API with authentication and domain tests, endpoint documentation, UI, and setup instructions. Representative authentication tests were inspected. | Shows Python API history and workflow implementation. Modernize setup instructions and dependencies; replace obsolete Travis/coverage widgets. Treat it as a legacy project. |
| [Maintenance-Tracker-App](https://github.com/Eyansky/Maintenance-Tracker-App) | Request lifecycle API, authentication, role-oriented workflows, UI, and tests for requests/users. Representative tests cover create/list/get/update behavior and missing-request responses. | Shows sustained backend experience. Refresh the documentation to explain backend setup, supported Python, and how to run tests. Replace obsolete third-party badges. |
| [portfolio](https://github.com/Eyansky/portfolio) | React/TypeScript component structure, dedicated About/Contact/Hero/Skills components, theme handling, and UI primitives. | Adds frontend presentation breadth. Its short README and lack of a visible dedicated test suite weaken the engineering story. Add a screenshot, architecture overview, build instructions, and meaningful interaction tests. Do not assume this code is the current mwangi.dev deployment. |
| [Agile-Group-Project](https://github.com/Eyansky/Agile-Group-Project) | Python API code organized into users/comments/replies, model definitions, CLI/setup entry points, and role-oriented behavior documented in the README. | Conditional sixth pin for API breadth. Documentation describes the design but not a reproducible setup; no dedicated test suite was visible in the default-branch tree. Explain personal contributions to this group project and add tests before treating it as a senior-level showcase. |

The first two are the clearest current evidence for senior backend/AI work. The remaining four are the strongest available complementary candidates, with material documentation/maintenance gaps. Pinning fewer than six is reasonable until those gaps are addressed. None of these recommendations relies on stars or popularity.

## Selection boundaries

Glow Careers, mwangi.dev, and VibeCheck remain live-product features. The audit did not establish a corresponding public source repository for those products. Their code is not represented as open source.

Large forks such as `art-backend` and `CodeGraphContext` were not promoted merely for their inherited engineering depth. The checked default-branch `art-backend` commit query for author `Eyansky` returned no results; that does not prove Ian never contributed under another identity or branch. Confirm personal contribution before using a fork as authorship evidence. Empty repositories, first-draft setups, and scaffold-only projects were deprioritized.

## Maintain the pins

The six pins were applied through GitHub's signed-in browser UI on 2026-11-06. Their saved order was verified using the read-only GraphQL `pinnedItems` field. GitHub's public API did not provide a pin-customization mutation for this workflow. To change them later:

1. Sign in and open [your GitHub profile](https://github.com/eyansky).
2. At the top of **Popular repositories** or **Pinned**, click **Customize your pins**.
3. Select the six repository names in the table above. Deselect existing choices if needed; GitHub permits up to six repositories and gists combined.
4. Click **Save pins**.
5. Drag the pins by their upper-right handles to match the recommended order.

These steps follow [GitHub's pinning documentation](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/pinning-items-to-your-profile).
