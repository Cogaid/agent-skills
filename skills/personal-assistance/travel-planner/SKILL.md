---
name: travel-planner
description: Plans and organizes travel, trips, and itineraries. Use when the user mentions "plan trip," "travel itinerary," "book travel," "flight options," "hotel recommendations," "business trip," "vacation planning," "packing list," or "conference travel."
metadata:
  version: 1.1.0
  category: personal-assistance
---

# Travel Planner

Plan and organize travel efficiently, from quick business trips to complex multi-city itineraries.

## Quick Start

1. **Gather requirements**: Run `python scripts/trip_planner.py --interactive`
2. **Build itinerary**: Use [templates/itinerary.md](templates/itinerary.md)
3. **Create packing list**: Run `python scripts/packing_list.py --type business --days 3`
4. **Pre-travel checklist**: Use [templates/checklist.md](templates/checklist.md)
5. **Document everything**: Keep confirmations accessible

## Travel Planning Workflow

```
Progress:
- [ ] Step 1: Define trip purpose and requirements
- [ ] Step 2: Book flights (earliest to get best prices)
- [ ] Step 3: Book accommodation
- [ ] Step 4: Arrange ground transportation
- [ ] Step 5: Plan activities/meetings
- [ ] Step 6: Create packing list
- [ ] Step 7: Complete pre-travel checklist
- [ ] Step 8: Share itinerary with emergency contact
```

## Booking Order

Book in this order for best prices/availability:
1. **Flights** - Book early, prices increase
2. **Accommodation** - After flights confirmed
3. **Ground transport** - Car rental, trains
4. **Activities/Reservations** - Popular ones book up
5. **Restaurant reservations** - Fine dining books early

## Utility Scripts

**trip_planner.py**: Generate trip plan from requirements
```bash
python scripts/trip_planner.py --destination "London" --dates "Mar 15-18" --purpose business
# Output: Trip planning checklist and template
```

**packing_list.py**: Generate packing list by trip type
```bash
python scripts/packing_list.py --type business --days 3 --international
# Output: Customized packing checklist
```

**timezone_helper.py**: Calculate jet lag and time differences
```bash
python scripts/timezone_helper.py --from "New York" --to "Tokyo" --flight-hours 14
# Output: Jet lag tips and schedule adjustment
```

## Trip Types

| Type | Template | Key Considerations |
|------|----------|-------------------|
| Business | [templates/business.md](templates/business.md) | Meetings, expense tracking |
| Conference | [templates/conference.md](templates/conference.md) | Sessions, networking |
| Client visit | [templates/client.md](templates/client.md) | Prep, follow-up |
| Multi-city | [templates/multi-city.md](templates/multi-city.md) | Logistics between stops |

## Packing Rules

- **Carry-on only** when possible (<5 days)
- **Wear bulky items** on the plane
- **Roll clothes** to save space
- **Pack cubes** for organization
- **One outfit per day** plus one backup

## Resources

- **Full planning guide**: [reference.md](reference.md)
- **Itinerary template**: [templates/itinerary.md](templates/itinerary.md)
- **Packing checklists**: [templates/packing.md](templates/packing.md)
- **Emergency info card**: [templates/emergency.md](templates/emergency.md)

## Related Skills

- Scheduling travel meetings: `meeting-scheduler`
- Travel coordination emails: `email-drafting`
- Prioritizing travel prep: `task-prioritizer`
