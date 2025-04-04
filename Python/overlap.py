def handle_event_overlaps(events):
    """
    Handles event overlaps based on priority rules:
    - High priority events cut other overlapping events
    - Mid and low priority events can overlap
    
    Parameters:
    events: List of dictionaries with keys 'priority', 'start', 'end'
    
    Returns:
    List of adjusted events with updated start/end times
    """
    # Sort events by priority (high first) and start time
    priority_order = {'high': 0, 'mid': 1, 'low': 2}
    sorted_events = sorted(
        events,
        key=lambda x: (priority_order[x['priority']], x['start'])
    )
    
    # Create a copy to store adjusted events
    adjusted_events = []
    
    for event in sorted_events:
        if event['priority'] == 'high':
            # High priority events get added as-is
            adjusted_events.append(event.copy())
        else:
            # For mid/low priority, check overlap with high priority events
            current_event = event.copy()            #8-12 | 2-5
            for existing_event in adjusted_events:      # 10-15  | 8-12
                if existing_event['priority'] == 'high':    #10-15
                    # Check for overlap
                    if (current_event['start'] < existing_event['end'] and 
                        current_event['end'] > existing_event['start']):
                        
                        # Split the event if necessary
                        if current_event['start'] < existing_event['start']:
                            # Add first part of split event
                            split_event = current_event.copy()
                            split_event['end'] = existing_event['start']
                            adjusted_events.append(split_event)
                        
                        if current_event['end'] > existing_event['end']:
                            # Update current event to start after high priority event
                            current_event['start'] = existing_event['end']
                        else:
                            # Event is completely covered by high priority event
                            current_event = None
                            break
                
            if current_event:
                adjusted_events.append(current_event)
    
    return sorted(adjusted_events, key=lambda x: x['start'])

# Example usage
events = [
    {'priority': 'mid', 'start': 2, 'end': 5},
    {'priority': 'high', 'start': 10, 'end': 15},
    {'priority': 'mid', 'start': 8, 'end': 18},
    {'priority': 'low', 'start': 11, 'end': 14},
    {'priority': 'mid', 'start': 13, 'end': 17},
    {'priority': 'high', 'start': 13, 'end': 16},
]

adjusted = handle_event_overlaps(events)
print(adjusted)

'''
[
    {'priority': 'mid', 'start': 2, 'end': 5},
    {'priority': 'mid', 'start': 8, 'end': 10},
    {'priority': 'high', 'start': 10, 'end': 15},
    {'priority': 'high', 'start': 13, 'end': 16},
    {'priority': 'mid', 'start': 16, 'end': 17}]

    {'priority': 'high', 'start': 10, 'end': 15},
    {'priority': 'high', 'start': 13, 'end': 16},
    {'priority': 'mid', 'start': 2, 'end': 5},
    {'priority': 'mid', 'start': 8, 'end': 12},
    {'priority': 'mid', 'start': 13, 'end': 17},
    {'priority': 'low', 'start': 11, 'end': 14},

[   {'priority': 'mid', 'start': 2, 'end': 5},
    {'priority': 'mid', 'start': 8, 'end': 10},
    {'priority': 'high', 'start': 10, 'end': 15},
    {'priority': 'high', 'start': 13, 'end': 16},
    {'priority': 'mid', 'start': 16, 'end': 18},
    {'priority': 'mid', 'start': 16, 'end': 17}]
'''