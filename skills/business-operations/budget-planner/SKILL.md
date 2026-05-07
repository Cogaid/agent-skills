---
name: budget-planner
description: Create, manage, and analyze budgets with variance tracking and forecasting. Use when the user mentions "budget," "budget planning," "budget template," "spending plan," "cost allocation," "budget variance," "forecasting," "zero-based budgeting," "department budget," "annual budget," or "budget review."
metadata:
  version: 1.0.0
  category: finance-operations
---

# Budget Planner

Create and manage budgets with structured categories, variance tracking, and data-driven forecasting.

## Purpose

This skill helps you build budgets from scratch, track spending against plan, analyze variances, and forecast future periods. It supports both zero-based and incremental approaches and provides frameworks for reallocation decisions when actuals diverge from plan.

## Quick Start

1. **Choose approach**: Zero-based (justify every dollar) or incremental (adjust last period)
2. **Define categories**: Use the category template below
3. **Set allocations**: Assign amounts by category and period
4. **Track actuals**: Compare spending to plan monthly
5. **Analyze variances**: Investigate anything over threshold
6. **Forecast and adjust**: Update projections quarterly

## Budget Categories Template

```
ANNUAL BUDGET: [Department / Company]
Fiscal Year: [YYYY]
Prepared by: [Name] | Approved by: [Name]
Last Updated: [Date]

CATEGORY                          Q1         Q2         Q3         Q4        ANNUAL
═══════════════════════════════  ═════════  ═════════  ═════════  ═════════  ═════════
REVENUE
  Product / Service Revenue      $XXX,XXX   $XXX,XXX   $XXX,XXX   $XXX,XXX   $X,XXX,XXX
  Other Income                    $XX,XXX    $XX,XXX    $XX,XXX    $XX,XXX     $XXX,XXX
  TOTAL REVENUE                  $XXX,XXX   $XXX,XXX   $XXX,XXX   $XXX,XXX   $X,XXX,XXX

PEOPLE (typically 60-70% of OpEx)
  Salaries & Wages               $XXX,XXX   $XXX,XXX   $XXX,XXX   $XXX,XXX   $X,XXX,XXX
  Benefits & Insurance            $XX,XXX    $XX,XXX    $XX,XXX    $XX,XXX     $XXX,XXX
  Contractors & Freelancers       $XX,XXX    $XX,XXX    $XX,XXX    $XX,XXX     $XXX,XXX
  Recruiting & Onboarding         $X,XXX     $X,XXX     $X,XXX     $X,XXX      $XX,XXX
  Training & Development          $X,XXX     $X,XXX     $X,XXX     $X,XXX      $XX,XXX

TECHNOLOGY
  SaaS & Subscriptions            $XX,XXX    $XX,XXX    $XX,XXX    $XX,XXX     $XXX,XXX
  Infrastructure / Cloud          $XX,XXX    $XX,XXX    $XX,XXX    $XX,XXX     $XXX,XXX
  Hardware & Equipment            $XX,XXX     $X,XXX     $X,XXX     $X,XXX      $XX,XXX
  Licenses                        $X,XXX     $X,XXX     $X,XXX     $X,XXX      $XX,XXX

SALES & MARKETING
  Advertising & Paid Media        $XX,XXX    $XX,XXX    $XX,XXX    $XX,XXX     $XXX,XXX
  Content & Creative              $XX,XXX    $XX,XXX    $XX,XXX    $XX,XXX     $XXX,XXX
  Events & Conferences            $XX,XXX    $XX,XXX     $X,XXX    $XX,XXX      $XX,XXX
  Sales Tools & Commissions       $XX,XXX    $XX,XXX    $XX,XXX    $XX,XXX     $XXX,XXX

GENERAL & ADMIN
  Office / Rent                   $XX,XXX    $XX,XXX    $XX,XXX    $XX,XXX     $XXX,XXX
  Legal & Accounting              $XX,XXX    $XX,XXX     $X,XXX     $X,XXX      $XX,XXX
  Insurance (D&O, E&O, GL)        $X,XXX     $X,XXX     $X,XXX     $X,XXX      $XX,XXX
  Travel & Meals                  $X,XXX     $X,XXX     $X,XXX     $X,XXX      $XX,XXX
  Miscellaneous                   $X,XXX     $X,XXX     $X,XXX     $X,XXX      $XX,XXX

CONTINGENCY (5-10% of total)     $XX,XXX    $XX,XXX    $XX,XXX    $XX,XXX     $XXX,XXX

═══════════════════════════════  ═════════  ═════════  ═════════  ═════════  ═════════
TOTAL EXPENSES                   $XXX,XXX   $XXX,XXX   $XXX,XXX   $XXX,XXX   $X,XXX,XXX
NET (Revenue - Expenses)          $XX,XXX    $XX,XXX    $XX,XXX    $XX,XXX     $XXX,XXX
```

## Zero-Based vs. Incremental Budgeting

| Dimension | Zero-Based (ZBB) | Incremental |
|-----------|------------------|-------------|
| **Starting point** | $0 -- justify every line | Last period + adjustment % |
| **Effort** | High (full rebuild each cycle) | Low (modify existing) |
| **Best for** | Cost reduction, new orgs, turnarounds | Stable businesses, minor changes |
| **Advantage** | Eliminates legacy bloat | Fast, easy, predictable |
| **Risk** | Time-consuming, may cut muscle | Perpetuates waste, less scrutiny |
| **When to use** | Every 2-3 years, or during cost pressure | Default annual cycle |
| **Approval** | Every item requires justification | Only changes need justification |

**Hybrid approach**: Use incremental for stable categories (rent, insurance) and zero-based for discretionary categories (marketing, travel, tools).

## Variance Analysis Framework

```
BUDGET VARIANCE REPORT
Period: [Month/Quarter YYYY]

Category              Budget      Actual      Variance    Var %    Status
────────────────────  ────────    ────────    ────────    ─────    ──────
Salaries              $120,000    $118,500     $1,500     1.3%    ✓ On track
Marketing              $45,000     $52,300    ($7,300)   -16.2%   ⚠ Over
Cloud Infrastructure   $25,000     $31,200    ($6,200)   -24.8%   ✗ Alert
Travel                  $8,000      $4,200     $3,800    47.5%    ✓ Under
────────────────────  ────────    ────────    ────────    ─────
TOTAL                 $198,000    $206,200    ($8,200)    -4.1%   ⚠ Review

Status Thresholds:
  ✓ On track:  within ±5%
  ⚠ Over:      5-15% over budget
  ✗ Alert:     >15% over budget
```

### Variance Investigation Questions

For each flagged variance, answer:
1. **What caused it?** One-time event or structural change?
2. **Was it foreseeable?** Should the budget have accounted for this?
3. **Is it recurring?** Will this variance continue in future periods?
4. **What's the impact?** Does it affect other categories or overall targets?
5. **What's the action?** Reallocate, cut elsewhere, or revise forecast?

## Forecasting Methodology

| Method | How It Works | Best For | Accuracy |
|--------|-------------|----------|----------|
| **Straight-line** | Last period x remaining periods | Stable costs | Low |
| **Moving average** | Average of last 3-6 months projected forward | Smoothing volatility | Medium |
| **Growth rate** | Apply historical growth % to base | Revenue forecasting | Medium |
| **Driver-based** | Forecast inputs (headcount, deals) then calculate cost | Operational planning | High |
| **Scenario-based** | Best / base / worst case models | Strategic planning | High |
| **Rolling forecast** | Continuously update next 12-18 months | Dynamic businesses | High |

### Driver-Based Forecast Example

```
DRIVER-BASED FORECAST: Engineering Department

Driver                Current    Forecast     Assumption
──────────────────    ───────    ────────     ──────────────────
Headcount (FTE)          12         15        3 hires in Q2-Q3
Avg Salary/FTE       $130K      $135K        3.8% market adjustment
Benefits Rate          28%        28%         No change
Contractor Hours      200/mo     300/mo       New project scope
Contractor Rate       $150/hr    $150/hr      Locked rate

Derived Costs:
  Salaries:          $130K x 15 = $1,950K (annualized at full ramp)
  Benefits:          $1,950K x 28% = $546K
  Contractors:       300 x $150 x 12 = $540K
  Ramp adjustment:   -$195K (staggered start dates)
  ────────────────────────────────────────────
  Total Forecast:    $2,841K
```

## Budget Review Cadence

| Review Type | Frequency | Participants | Focus |
|-------------|-----------|-------------|-------|
| **Actuals check** | Weekly | Finance lead | Flag early variances |
| **Monthly review** | Monthly | Dept heads + Finance | Variance analysis, reforecast |
| **Quarterly deep dive** | Quarterly | Exec team + Finance | Strategic reallocation |
| **Mid-year reset** | Semi-annual | Full leadership | Revise annual targets if needed |
| **Annual planning** | Annual (Q4) | All departments | Build next year's budget |

## Reallocation Decision Matrix

When actuals diverge from plan, use this framework to decide:

| Situation | Variance | Action | Approval |
|-----------|----------|--------|----------|
| Under budget, temporary | >10% under | Hold funds, do not reallocate yet | Dept head |
| Under budget, structural | >10% under for 2+ months | Release funds to contingency pool | Finance lead |
| Over budget, one-time | <15% over | Absorb from contingency | Dept head |
| Over budget, recurring | >10% over for 2+ months | Formal reallocation request | CFO / Exec |
| Over budget, critical | >25% over | Emergency review, freeze discretionary | CFO + CEO |
| Revenue shortfall | >10% miss | Trigger cost reduction playbook | Exec team |

## Department Budget Template

```
DEPARTMENT BUDGET REQUEST
──────────────────────────────────────────
Department:       [Name]
Manager:          [Name]
Fiscal Year:      [YYYY]
Submission Date:  [Date]

1. DEPARTMENT MISSION
   [One sentence describing the department's role]

2. KEY OBJECTIVES FOR THE YEAR
   a. [Objective 1 -- tied to company goal]
   b. [Objective 2 -- tied to company goal]
   c. [Objective 3 -- tied to company goal]

3. HEADCOUNT PLAN
   Current FTEs:     [##]
   Planned hires:    [##] (roles: ________________)
   Planned exits:    [##]
   Year-end FTEs:    [##]

4. BUDGET SUMMARY
   Category              Request       Last Year     Change
   ──────────────────    ──────────    ──────────    ──────
   People                $XXX,XXX      $XXX,XXX      +XX%
   Technology             $XX,XXX       $XX,XXX      +XX%
   Marketing              $XX,XXX       $XX,XXX      -XX%
   Travel & Events         $X,XXX        $X,XXX      +XX%
   Other                   $X,XXX        $X,XXX       0%
   ──────────────────    ──────────    ──────────    ──────
   TOTAL                 $XXX,XXX      $XXX,XXX      +XX%

5. KEY ASSUMPTIONS
   • [Assumption 1]
   • [Assumption 2]

6. RISKS TO BUDGET
   • [Risk 1 -- potential impact $XX,XXX]
   • [Risk 2 -- potential impact $XX,XXX]

7. TRADE-OFF OPTIONS (if budget is reduced 10-20%)
   • Cut option A: [What would be deferred, impact]
   • Cut option B: [What would be deferred, impact]
```

## Scripts & Tools

**create_budget.py**: Initialize a new budget from template
```bash
python scripts/create_budget.py --department engineering --year 2026 --approach zero-based
# Output: Budget template with pre-populated categories
```

**track_variance.py**: Monthly variance tracking
```bash
python scripts/track_variance.py --period 2026-03 --threshold 10
# Output: Variance report with flagged items
```

**forecast.py**: Generate rolling forecast
```bash
python scripts/forecast.py --method driver-based --horizon 12
# Output: 12-month forecast with confidence intervals
```

## Best Practices

1. **Start with objectives**: Budget should fund strategy, not just repeat last year
2. **Build in contingency**: 5-10% buffer for unplanned but inevitable costs
3. **Use drivers, not guesses**: Base projections on measurable inputs (headcount, deals, volume)
4. **Review monthly, adjust quarterly**: Budgets are living documents, not annual rituals
5. **Require trade-offs**: Every budget increase should identify what gets cut or deferred
6. **Separate capital from operating**: CapEx and OpEx have different approval and tax treatment
7. **Document assumptions**: When assumptions change, you know which numbers to update
8. **Involve budget owners**: People who manage spending should own their budget line items
9. **Track commitment, not just spend**: Purchase orders and contracts are future obligations
10. **Keep it simple**: A budget nobody reads is a budget nobody follows
