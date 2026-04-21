# Calendar Summary Template

## Usage

Visual time-block view of the day's calendar. Use `generate_briefing.py --format calendar` to produce this view from calendar API data.

---

```
CALENDAR DETAIL: {{date}}

TIME BLOCKS:
+----------+--------------------------------------------------+
| 08:00 AM | ........ FOCUS TIME ........                      |
| 08:30 AM | ........ FOCUS TIME ........                      |
| 09:00 AM | #### {{meeting_1}} ({{duration_1}})               |
| 09:30 AM | #### {{meeting_1}} continued                      |
| 10:00 AM | ........ FOCUS TIME ........                      |
| 10:30 AM | ........ FOCUS TIME ........                      |
| 11:00 AM | #### {{meeting_2}} ({{duration_2}})               |
| 11:30 AM | #### {{meeting_2}} continued                      |
| 12:00 PM | ~~~~~~~~ LUNCH ~~~~~~~~                           |
| 12:30 PM | ~~~~~~~~ LUNCH ~~~~~~~~                           |
| 01:00 PM | #### {{meeting_3}} ({{duration_3}})               |
| 01:30 PM | ........ FOCUS TIME ........                      |
| 02:00 PM | ........ FOCUS TIME ........                      |
| 02:30 PM | ........ FOCUS TIME ........                      |
| 03:00 PM | #### {{meeting_4}} ({{duration_4}})               |
| 03:30 PM | ........ FOCUS TIME ........                      |
| 04:00 PM | ........ FOCUS TIME ........                      |
| 04:30 PM | ........ FOCUS TIME ........                      |
| 05:00 PM | END OF DAY                                        |
+----------+--------------------------------------------------+

MEETING PREP NEEDED:
- {{meeting_1}}: Review {{document_1}}, prepare {{deliverable_1}}
- {{meeting_3}}: Send agenda to {{attendees_3}}

CONFLICTS: {{conflict_description}} or "None detected"

SUMMARY:
  Total meetings: {{meeting_count}}
  Total meeting time: {{meeting_hours}}h
  Focus blocks: {{focus_block_count}} ({{focus_hours}}h total)
  Longest focus block: {{longest_focus}} ({{longest_focus_start}} - {{longest_focus_end}})
```

## Legend

- `####` = Scheduled meeting
- `........` = Available focus time
- `~~~~~~~~` = Break / lunch

## Notes

- Working hours default to 8:00 AM - 5:00 PM; configurable via `--work-start` and `--work-end`
- Lunch is auto-detected or defaults to 12:00 - 1:00 PM
- Conflicts are flagged when two events overlap
- Prep notes are pulled from event descriptions or linked documents
