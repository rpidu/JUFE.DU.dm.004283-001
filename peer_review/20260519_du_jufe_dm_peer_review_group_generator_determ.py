#!/usr/bin/env python3
"""
Create balanced identifier groupings where each identifier serves as a group identifier,
and all identifiers appear approximately the same number of times across all groups.

The script reads identifiers from a text file and generates groupings of 9 identifiers each,
with the first identifier being the group identifier and the remaining 8 sorted.
"""

import argparse
import sys
import math
from collections import defaultdict, Counter
from itertools import cycle
from typing import List, Set, Dict, Tuple, Optional


class Backend:
    """
    Backend class responsible for file reading operations.
    
    This class follows the backend pattern to abstract data input operations,
    providing a clean interface for reading identifiers from text files.
    """
    
    def __init__(self, filepath: str):
        """
        Initialize the backend with a target file path.
        
        Args:
            filepath: Path to the input file containing identifiers
        """
        self.filepath = filepath
    
    def read_identifiers(self) -> List[str]:
        """
        Read identifiers from the file, one per line.
        
        Returns:
            List of identifier strings stripped of whitespace
            
        Raises:
            FileNotFoundError: If the specified file doesn't exist
            ValueError: If no valid identifiers are found
        """
        identifiers = []
        try:
            with open(self.filepath, 'r', encoding='utf-8') as file:
                for line_num, line in enumerate(file, 1):
                    identifier = line.strip()
                    if identifier:  # Skip empty lines
                        identifiers.append(identifier)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Input file not found: {self.filepath}") from e
        
        if not identifiers:
            raise ValueError(f"No valid identifiers found in {self.filepath}")
        
        return identifiers


class Model:
    """
    Model class responsible for processing identifiers and generating groupings.
    
    This class implements the grouping algorithm, ensuring balanced distribution
    of identifiers across groups and handling edge cases gracefully.
    """
    
    def __init__(self, backend: Backend):
        """
        Initialize the model with a backend object.
        
        Args:
            backend: Backend instance for data reading operations
        """
        self.backend = backend
        self.identifiers: List[str] = []
        self.group_size = 9
    
    def load_data(self) -> None:
        """Load identifiers from the backend into the model."""
        self.identifiers = self.backend.read_identifiers()
    
    def process(self) -> List[List[str]]:
        """
        Process identifiers to create balanced groupings.
        
        Returns:
            List of groupings, each as a list where the first element is the
            group identifier and the remaining are the grouped identifiers
            
        Algorithm:
            1. Calculate target appearances per identifier (floor/ceil)
            2. Create a circular list of all identifiers
            3. For each group identifier, select unique identifiers following
               a rotating pattern to ensure even distribution
            4. Fill remaining slots with least-used identifiers when needed
        """
        n = len(self.identifiers)
        if n < self.group_size:
            raise ValueError(
                f"Need at least {self.group_size} identifiers, but only {n} provided"
            )
        
        # Sort identifiers for consistent ordering
        sorted_ids = sorted(self.identifiers)
        
        # Calculate target appearances per identifier
        total_slots = n * (self.group_size - 1)  # Excluding group identifier position
        min_appearances = total_slots // n
        extra_appearances = total_slots % n
        
        # Track how many times each identifier has been used as a member
        usage_counter = Counter()
        
        # Calculate target usage for each identifier
        target_usage = {
            id_: min_appearances + (1 if i < extra_appearances else 0)
            for i, id_ in enumerate(sorted_ids)
        }
        
        # Prepare result groupings
        groupings = []
        
        # Create a circular sequence for selection
        # We'll use a rotating offset to ensure even distribution
        for group_idx, group_id in enumerate(sorted_ids):
            # Start with the group identifier
            group = [group_id]
            
            # We need to select self.group_size - 1 other identifiers
            needed = self.group_size - 1
            
            # Create a pool of potential candidates (all except the group identifier)
            candidates = [id_ for id_ in sorted_ids if id_ != group_id]
            
            # Sort candidates by current usage count to select least-used first
            # This implements the balancing algorithm
            candidates.sort(key=lambda x: (usage_counter[x], x))
            
            selected = []
            
            # Select needed number of candidates
            for candidate in candidates:
                if len(selected) >= needed:
                    break
                
                # Check if we're not exceeding target usage
                if usage_counter[candidate] < target_usage.get(candidate, float('inf')):
                    selected.append(candidate)
                    usage_counter[candidate] += 1
            
            # If we couldn't select enough due to constraints, fill remaining
            # with the least-used identifiers regardless of target
            if len(selected) < needed:
                remaining_needed = needed - len(selected)
                all_candidates = [id_ for id_ in sorted_ids if id_ != group_id]
                all_candidates.sort(key=lambda x: (usage_counter[x], x))
                
                for candidate in all_candidates:
                    if len(selected) >= needed:
                        break
                    if candidate not in selected:
                        selected.append(candidate)
                        usage_counter[candidate] += 1
            
            # Sort the selected identifiers alphanumerically
            selected.sort()
            group.extend(selected)
            groupings.append(group)
        
        return groupings


def create_groupings_round_robin(identifiers: List[str], group_size: int) -> List[List[str]]:
    """
    Alternative IPO-style function for creating balanced groupings using round-robin.
    
    Args:
        identifiers: List of identifier strings
        group_size: Number of identifiers per group (including group identifier)
    
    Returns:
        List of groupings following the specified format
    
    Algorithm:
        1. Create a circular list of all identifiers
        2. For each group identifier, take the next (group_size-1) identifiers
        3. Rotate the starting point for each group to ensure even distribution
    """
    n = len(identifiers)
    sorted_ids = sorted(identifiers)
    groupings = []
    
    # Create a circular list by repeating the identifiers enough times
    # This ensures we can select unique identifiers for each group
    extended_list = sorted_ids * (group_size)
    
    for i, group_id in enumerate(sorted_ids):
        group = [group_id]
        
        # Calculate starting position for this group
        # Using a step pattern to ensure even distribution
        start_pos = (i + 1) % n
        
        # Collect the next (group_size-1) unique identifiers
        selected = []
        pos = start_pos
        while len(selected) < group_size - 1:
            candidate = extended_list[pos % n]
            if candidate != group_id and candidate not in selected:
                selected.append(candidate)
            pos += 1
        
        selected.sort()
        group.extend(selected)
        groupings.append(group)
    
    return groupings


def validate_groupings(groupings: List[List[str]], identifiers: List[str], group_size: int) -> bool:
    """
    Validate the generated groupings for correctness.
    
    Args:
        groupings: List of groupings to validate
        identifiers: Original list of identifiers
        group_size: Expected group size
    
    Returns:
        True if groupings are valid, False otherwise
    
    Validation checks:
        - Correct number of groups
        - All groups have correct size
        - Each identifier appears as a group identifier exactly once
        - No duplicate identifiers within a group
        - All identifiers are from the original set
    """
    n = len(identifiers)
    id_set = set(identifiers)
    group_ids = set()
    
    if len(groupings) != n:
        print(f"Validation failed: Expected {n} groups, got {len(groupings)}")
        return False
    
    for i, group in enumerate(groupings):
        if len(group) != group_size:
            print(f"Validation failed: Group {i} has size {len(group)}, expected {group_size}")
            return False
        
        # Check group identifier is first
        group_id = group[0]
        if group_id in group_ids:
            print(f"Validation failed: Group identifier {group_id} appears multiple times")
            return False
        group_ids.add(group_id)
        
        # Check for duplicates and valid identifiers
        group_set = set(group)
        if len(group_set) != len(group):
            print(f"Validation failed: Group {i} has duplicate identifiers")
            return False
        
        # Check all identifiers are from original set
        if not group_set.issubset(id_set):
            print(f"Validation failed: Group {i} contains unknown identifiers")
            return False
    
    return True


def main() -> None:
    """Main function to orchestrate the backend-model-process pattern."""
    parser = argparse.ArgumentParser(
        description="Create balanced identifier groupings of 9 identifiers each",
        epilog="Each identifier serves as a group identifier once. All identifiers appear "
               "approximately the same number of times across all groupings."
    )
    parser.add_argument(
        'input_file',
        type=str,
        help='Path to text file containing identifiers (one per line)'
    )
    parser.add_argument(
        '--validate',
        action='store_true',
        help='Validate the generated groupings before output'
    )
    parser.add_argument(
        '--method',
        choices=['balanced', 'roundrobin'],
        default='balanced',
        help='Method for creating groupings (default: balanced)'
    )
    
    args = parser.parse_args()
    
    try:
        # Backend: File reading
        backend = Backend(args.input_file)
        
        # Model: Processing
        model = Model(backend)
        model.load_data()
        
        # Process: Create groupings
        if args.method == 'roundrobin':
            groupings = create_groupings_round_robin(model.identifiers, model.group_size)
        else:
            groupings = model.process()
        
        # Optional validation
        if args.validate:
            if validate_groupings(groupings, model.identifiers, model.group_size):
                print("Validation passed!", file=sys.stderr)
            else:
                print("Validation failed!", file=sys.stderr)
                sys.exit(1)
        
        # Output groupings
        for group in groupings:
            # Sort group members (excluding first element which is already sorted)
            # First element is group identifier, remaining are sorted in model.process()
            print(' '.join(group))
        
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()