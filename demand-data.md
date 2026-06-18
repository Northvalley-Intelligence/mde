
    # Mission Driven Engineering (MDE) Project Bootstrap

    You are operating under the Mission Driven Engineering (MDE) approach.

    Your goal is not to generate code.

    Your goal is to build a successful application that accomplishes the mission while continuously improving understanding of the problem.

    Code is an artifact.

    Mission advancement is the objective.

    ---

    # Core Philosophy

    Traditional software development optimizes for tasks.

    Many AI coding systems optimize for code generation.

    MDE optimizes for mission accomplishment.

    The primary unit of work is a Generation.

    The primary measure of progress is mission advancement.

    The primary measure of quality is validated behavior.

    ---

    # Key Concepts

    ## Mission

    The Mission describes:

    * what we are building
    * why it matters
    * who benefits
    * constraints
    * assumptions
    * success criteria

    The Mission is the highest-priority artifact.

    Mission changes must be recorded in MISSION_UPDATES.md.

    ---

    ## Generation

    A Generation is a bounded implementation attempt made in pursuit of the Mission.

    A Generation consumes:

    * Mission
    * Mission Updates
    * Existing Codebase
    * Existing Agent Artifacts
    * Existing Deploy Artifacts
    * Current BDD Status

    A Generation produces:

    * Code Changes
    * Agent Artifact Updates
    * Deploy Artifact Updates
    * Validation Results
    * Progress Summary
    * New Risks
    * Lessons Learned

    Progress is measured by:

    * mission advancement
    * BDD improvement
    * risk reduction
    * knowledge gained

    Never measure success using lines of code.

    ---

    ## BDD

    BDD scenarios are derived from the Mission.

    Every significant behavior should be represented by one or more BDDs.

    Each BDD must be classified:

    * Critical
    * High
    * Medium
    * Low

    Critical and High BDDs drive implementation priority.

    Passing tests that do not validate mission-critical behavior do not constitute success.

    ---

    ## Mission Updates

    Mission Updates capture learning.

    Examples:

    * clarified requirements
    * failed assumptions
    * discovered risks
    * improved approaches
    * refined success criteria

    Mission Updates become part of project memory.

    Do not discard lessons learned.

    ---

    # Artifact Categories

    MDE recognizes three classes of artifacts.

    ---

    ## Human Artifacts

    These should be optimized for human understanding.

    Examples:

    ```text
    MISSION.md
    MISSION_UPDATES.md
    ```

    Humans should understand:

    * what is being built
    * what changed
    * what remains risky
    * what happens next

    Do not overwhelm humans with implementation details or large code dumps.

    ---

    ## Agent Artifacts

    Agent artifacts exist to help agents reason efficiently.

    Optimize them for:

    * retrieval
    * traceability
    * validation
    * planning
    * decision making

    Suggested structure:

    ```text
    .mde/
    state.json
    bdd-index.json
    failing-bdds.json
    task-graph.json
    risk-register.json
    decisions.jsonl
    progress.json
    generations/
    ```

    Agent artifacts are not required to be human-friendly.

    Use formats that are fast for agents to read and update.

    ---

    ## Deploy Artifacts

    Deploy artifacts should optimize:

    * reliability
    * reproducibility
    * simplicity
    * operational cost

    Examples:

    ```text
    deploy/
    build-manifest.json
    release-checks.json
    environment.schema.json
    ```

    Deployment should not require extensive human interpretation.

    ---

    # Generation Lifecycle

    Every Generation follows this lifecycle.

    ## Step 1: Understand

    Review:

    * Mission
    * Mission Updates
    * Existing State
    * Existing BDDs
    * Existing Risks

    Identify knowledge gaps.

    ---

    ## Step 2: Plan

    Determine:

    * highest-value behaviors
    * failing BDDs
    * dependencies
    * risks

    Update task graph.

    ---

    ## Step 3: Implement

    Implement only enough change to advance the Mission.

    Avoid speculative architecture.

    Avoid solving hypothetical future problems.

    ---

    ## Step 4: Validate

    Execute BDD validation.

    Record:

    * passing BDDs
    * failing BDDs
    * new failures
    * regressions

    ---

    ## Step 5: Learn

    Identify:

    * assumptions proven wrong
    * missing BDDs
    * mission ambiguities
    * newly discovered risks

    Update Mission Updates if appropriate.

    ---

    ## Step 6: Communicate

    Produce a concise mission-oriented summary.

    Focus on:

    * behavior improved
    * why it matters
    * validation results
    * risks
    * next focus area

    Do not dump code.

    ---

    # Generation Exit Criteria

    A Generation ends when one or more occur:

    1. Assigned scope completed
    2. Validation completed
    3. Mission refinement required
    4. No meaningful progress can be made
    5. Resource limits reached

    Do not continue indefinitely.

    ---

    # Mission Phase Exit Criteria

    A Mission Phase is complete only when:

    1. All Critical BDDs pass
    2. All High BDDs pass
    3. Two consecutive independent validation generations pass without requiring code changes between validations
    4. No unresolved Critical risks remain

    ---

    # Mission Exit Criteria

    The Mission is complete only when:

    1. Mission objectives are achieved
    2. All Critical BDDs pass
    3. All High BDDs pass
    4. Phase exit criteria have been satisfied
    5. Remaining risks are accepted or mitigated
    6. Human approval is obtained

    ---

    # Progress Reporting

    Communicate in mission language.

    Preferred format:

    Mission Progress Update

    Current Focus:
    ...

    Behavior Improved:
    ...

    Why It Matters:
    ...

    Validation Results:
    ...

    Risks:
    ...

    Next Generation Focus:
    ...

    Avoid code-centric reporting.

    ---

    # Continuous MDE Improvement

    The project should improve not only the application but also the engineering process.

    If weaknesses are discovered in:

    * mission tracking
    * BDD generation
    * validation
    * deployment
    * agent memory
    * progress reporting

    record them in MISSION_UPDATES.md and improve project MDE artifacts.

    Every project should leave the MDE approach stronger than it was before.

    ---

    # Initial Deliverables

    Before implementation begins:

    1. Create MISSION.md
    2. Create MISSION_UPDATES.md
    3. Create .mde structure
    4. Generate BDD inventory
    5. Classify BDD priorities
    6. Create task graph
    7. Create risk register
    8. Create Generation 0 readiness assessment

    Do not begin implementation until these artifacts exist.

    ---

# Current Project Mission



Feature A: Demand Intelligence Dataset

Mission:
Build a reusable, versioned dataset that represents what customers search for across local service industries.

This dataset should be independently improvable without changing the Demand Coverage Engine.

Supported v1 sectors:

* HVAC
* Roofing
* Pest Control
* Real Estate
* Closet / Wardrobe Design
* Cleaning

Demand sources:

1. Google Keyword Planner export

   * Best source for estimated monthly search volume.
   * Manually exported in v1.
   * No direct Google Ads API integration in v1.

2. Google autocomplete

   * Useful for discovering common search phrasing.
   * Good for “near me,” cost, emergency, and question-style searches.

3. People Also Ask / related questions

   * Useful for educational and research intent.
   * Helps identify article/FAQ opportunities.

4. Google Search Console

   * Future source.
   * Useful after a customer connects their own verified site.
   * Shows real queries where the site already appears.

5. Manual expert curation

   * Used for business-important topics that may not show strong volume.
   * Example: “relocating from California to Georgia” for real estate.

6. Customer/prospect discovery

   * Topics learned from business owner interviews, sales calls, and local meetings.

7. Existing website corpus

   * Terms extracted from high-quality local business websites.
   * Used for inspiration, not copied blindly.

Required dataset fields:

* id
  Unique stable identifier for the demand record.

* sector
  Primary industry category.
  Examples: roofing, hvac, pest_control, real_estate, cleaning.

* subcategory
  More specific demand group.
  Examples: roof_repair, replacement, relocation, schools, deep_cleaning.

* keyword
  The raw search term or demand phrase.
  Example: “roof replacement cost”.

* normalized_keyword
  Lowercase/cleaned version used for matching and deduplication.

* intent
  Customer intent category.
  Allowed values:
  Emergency / Urgent
  Cost / Pricing
  Service
  Local / Near Me
  Education / Research
  Comparison
  Trust / Provider Selection
  Financing
  Maintenance / Prevention

* monthly_searches
  Estimated monthly searches, if available.
  Null if unknown.

* search_volume_source
  Source of monthly search estimate.
  Examples: keyword_planner, search_console, manual_estimate, unknown.

* priority
  Business priority independent of search volume.
  Allowed values: high, medium, low.

* location_modifier
  Location phrase if present.
  Examples: Marietta, Kennesaw, near me, Georgia.

* location_relevance
  Whether the topic is local, regional, or national.
  Allowed values: local, regional, national, unknown.

* source
  Where the keyword/topic came from.
  Examples:
  keyword_planner
  autocomplete
  people_also_ask
  search_console
  manual_curation
  prospect_discovery
  website_corpus

* source_detail
  Optional note describing source context.
  Example: “Google autocomplete for roof repair”.

* confidence
  Confidence that the record is useful and correctly classified.
  Allowed values: high, medium, low.

* notes
  Human-readable notes for future improvement.

* active
  Boolean indicating whether this demand record should currently be used.

* created_at
  Date added.

* updated_at
  Date last modified.

Dataset requirements:

* Must be versionable.
* Must support CSV and JSON.
* Must allow null monthly search volume.
* Must deduplicate similar keywords.
* Must preserve source attribution.
* Must be easy to expand by sector.
* Must be testable independently from the website assessment engine.

Validation:
For Feature A, tests should cover:

* schema validation
* required fields
* allowed intent values
* allowed priority values
* duplicate detection
* source attribution
* null search volume handling
* sector/subcategory consistency
* active/inactive record handling

Output:
Create or update documentation explaining:

* dataset purpose
* sources
* field definitions
* validation rules
* example records
* how the dataset improves Demand Coverage analysis
