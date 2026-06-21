Create:

```txt
notes/pybaseball-analysis.md
```

and paste this in.

---

# pybaseball Analysis

## Executive Summary

`pybaseball` is the Python equivalent of baseballr, but it is closer to the ecosystem MLB-LAB will likely build around in the future.

Like baseballr, pybaseball primarily solves the problem of data acquisition.

However, because Python dominates modern analytics, machine learning, and automation workflows, pybaseball provides a more direct path from:

```txt
Data
→ Analysis
→ Modeling
→ Reports
```

For MLB-LAB, pybaseball is not a prediction engine.

It is a research and data infrastructure asset.

---

## What Problem Does It Solve?

Baseball data is scattered across:

* Statcast
* FanGraphs
* Baseball Reference
* Lahman Database
* Retrosheet
* MLB sources

pybaseball provides Python functions that simplify access to those sources.

---

## Why It Matters

MLB-LAB is attempting to build an intelligence system.

Intelligence systems require:

1. Data
2. Feature engineering
3. Analysis
4. Decision support

pybaseball helps with stages 1 and 2.

---

## Data Sources

### Tier 1

Highest value

```txt
Statcast
FanGraphs
Baseball Reference
```

---

### Tier 2

Supporting value

```txt
Lahman Database
Retrosheet
```

---

## Reusable Components

### Statcast Access

Score: 10/10

Provides access to:

* Exit velocity
* Launch angle
* Pitch movement
* xBA
* xSLG
* xwOBA

These metrics are essential for modern baseball analysis.

---

### Historical Queries

Score: 10/10

Allows historical testing.

Useful for:

```txt
Trend analysis
Backtesting
Model validation
```

---

### Python Integration

Score: 10/10

Largest advantage over baseballr.

Compatible with:

```txt
pandas
numpy
scikit-learn
xgboost
lightgbm
jupyter
```

This creates future flexibility.

---

## What MLB-LAB Should Extract

### Extract

```txt
Statcast workflows
Feature engineering ideas
Historical testing methods
Data cleaning approaches
Metric definitions
```

---

### Do Not Extract

```txt
Entire codebase
Package maintenance logic
Every available statistic
```

Focus on decision-making information.

---

## Weaknesses

### No Intelligence Layer

pybaseball retrieves data.

It does not answer:

```txt
What matters?
What creates edge?
What should I do?
```

---

### No Reporting Layer

No executive summaries.

No decision framework.

No research prioritization.

---

### Data Overload Risk

Thousands of available metrics.

Most are not actionable.

This can create analysis paralysis.

---

## Hidden Assumptions

### Assumption 1

More features create better predictions.

Often false.

Feature quality matters more than quantity.

---

### Assumption 2

Statcast metrics automatically create edge.

Many markets already account for obvious Statcast signals.

---

### Assumption 3

Users understand baseball analytics.

MLB-LAB's job is translating analytics into intelligence.

---

## What Could Break?

### External Data Sources

If:

```txt
Statcast changes
FanGraphs changes
Baseball Reference changes
```

certain functions may fail.

---

### Scraping Dependencies

Some data access depends on external website structures.

---

## Relevance Score

| Category           | Score |
| ------------------ | ----- |
| Data Collection    | 10    |
| Research Value     | 10    |
| Prediction Value   | 6     |
| Reporting Value    | 3     |
| MLB-LAB Importance | 10    |

---

## Build From Zero Assessment

baseballr and pybaseball solve the same major problem:

```txt
Access to baseball data
```

Neither solves:

```txt
Decision making
Research prioritization
Intelligence generation
Report creation
```

Those layers still need to be built.

---

## Comparison vs baseballr

| Area                | baseballr | pybaseball |
| ------------------- | --------- | ---------- |
| Language            | R         | Python     |
| Data Access         | 10        | 10         |
| Research Utility    | 10        | 10         |
| Future Automation   | 7         | 10         |
| ML Ecosystem        | 6         | 10         |
| Reporting Potential | 6         | 9          |

Winner:

```txt
pybaseball
```

for long-term MLB-LAB development.

---

## Key Insight

After analyzing both repositories:

```txt
Data Collection = Solved

Research Layer = Missing

Decision Layer = Missing

Report Layer = Missing
```

This confirms MLB-LAB should focus on:

```txt
Research Frameworks
Decision Frameworks
Intelligence Reports
```

rather than building another data library.

---

## Next Action

Research:

1. MLB-StatsAPI
2. Projection systems
3. Betting models
4. Statcast feature engineering repos

Then update:

```txt
notes/repo-comparison.md
```

with:

| Repo       | Data | Research | Prediction | Reporting | Overall |
| ---------- | ---- | -------- | ---------- | --------- | ------- |
| baseballr  | 10   | 10       | 4          | 3         | 9       |
| pybaseball | 10   | 10       | 6          | 3         | 10      |

---

### MLB-LAB Conclusion

baseballr and pybaseball are foundations.

Neither is the final system.

The real opportunity is building the layers that sit **above** the data:

```txt
Data
↓
Research
↓
Intelligence
↓
Decision Support
↓
Reports
```

That is where MLB-LAB can become differentiated.
