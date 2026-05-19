#!/usr/bin/env python3
"""
Identifier Grouping Generator - Creates balanced groupings of identifiers where each identifier
serves as a group identifier and appears equally across all groupings.

Architecture: Backend-Model-Process pattern with IPO (Input-Process-Output) style processing.
- Backend: Handles file I/O operations
- Model: Stores and manages identifier data
- Process: Implements the grouping algorithm
"""

import argparse
import random
from collections import defaultdict, Counter
from typing import List, Set, Tuple, Optional


class Backend:
    """
    Backend class responsible for file I/O operations.
    Handles reading identifiers from input file and writing groupings to output.
    """
    
    def __init__(self, input_file: str, output_file: Optional[str] = None):
        """
        Initialize Backend with input and optional output file paths.
        
        Args:
            input_file: Path to file containing identifiers (one per line)
            output_file: Optional path for output (defaults to stdout)
        """
        self.input_file = input_file
        self.output_file = output_file
    
    def read_identifiers(self) -> List[str]:
        """
        Read identifiers from input file.
        
        Returns:
            List of identifier strings (stripped of whitespace)
            
        Raises:
            FileNotFoundError: If input file doesn't exist
        """
        try:
            with open(self.input_file, 'r') as f:
                # Read lines, strip whitespace, filter out empty lines
                identifiers = [line.strip() for line in f if line.strip()]
            return identifiers
        except FileNotFoundError:
            raise FileNotFoundError(f"Input file '{self.input_file}' not found.")
    
    def write_groupings(self, groupings: List[Tuple[str, List[str]]]) -> None:
        """
        Write groupings to output file or stdout.
        
        Args:
            groupings: List of (group_identifier, member_list) tuples
        """
        # Sort groupings by group identifier
        sorted_groupings = sorted(groupings, key=lambda x: x[0])
        
        # Prepare output lines
        output_lines = []
        for group_id, members in sorted_groupings:
            # Format: "group_id member1 member2 ..."
            line = f"{group_id} {' '.join(members)}"
            output_lines.append(line)
        
        # Write to file or stdout
        if self.output_file:
            with open(self.output_file, 'w') as f:
                f.write('\n'.join(output_lines))
        else:
            print('\n'.join(output_lines))


class Model:
    """
    Model class that manages the identifier dataset and grouping constraints.
    Stores identifiers and provides validation for grouping requirements.
    """
    
    def __init__(self, identifiers: List[str]):
        """
        Initialize Model with list of identifiers.
        
        Args:
            identifiers: List of unique identifier strings
        """
        self.identifiers = identifiers
        self.count = len(identifiers)
        self.group_size = 9  # Fixed group size as per specification
        
    def validate(self) -> bool:
        """
        Validate that requirements can be reasonably met.
        
        Returns:
            True if validation passes, False otherwise
        """
        if self.count < self.group_size:
            print(f"Warning: Only {self.count} identifiers available, but group size is {self.group_size}")
            return False
        
        # Calculate ideal frequency: each identifier should appear equally
        # Total slots = count * (group_size - 1) because each group has group_size-1 members
        # Times identifier appears as member = total_slots / count
        total_member_slots = self.count * (self.group_size - 1)
        ideal_frequency = total_member_slots / self.count
        
        print(f"Dataset size: {self.count} identifiers")
        print(f"Group size: {self.group_size}")
        print(f"Ideal appearance frequency per identifier: {ideal_frequency:.2f}")
        
        return True
    
    def get_identifier_pool(self) -> Set[str]:
        """
        Get the set of all identifiers.
        
        Returns:
            Set of identifier strings
        """
        return set(self.identifiers)


class GroupingProcessor:
    """
    Process class implementing the grouping algorithm.
    Uses IPO pattern: Input (identifiers + constraints), Process (algorithm), Output (groupings)
    """
    
    def __init__(self, model: Model):
        """
        Initialize processor with a Model instance.
        
        Args:
            model: Model containing identifiers and constraints
        """
        self.model = model
        self.group_size = model.group_size
        
    def process(self) -> List[Tuple[str, List[str]]]:
        """
        Main processing function implementing IPO pattern.
        Creates balanced groupings where each identifier appears as group identifier once.
        
        Returns:
            List of (group_identifier, member_list) tuples
        """
        # Input: Get identifiers and prepare data structures
        identifiers = self.model.identifiers
        identifier_set = set(identifiers)
        id_count = self.model.count
        
        # Track how many times each identifier appears across all groups
        appearance_count = defaultdict(int)
        
        # Create list to store result groups
        groupings = []
        
        # Process: Build groups for each identifier as group leader
        for group_leader in identifiers:
            # Create a group with the leader
            group = [group_leader]
            
            # Need to select (group_size - 1) unique members
            members_needed = self.group_size - 1
            
            # Strategy: Select members with lowest appearance count so far
            # This creates a balanced distribution
            available = identifier_set - {group_leader}
            
            # Convert to list for selection
            available_list = list(available)
            
            # Sort available identifiers by their current appearance count (lowest first)
            # This implements the balancing heuristic
            available_list.sort(key=lambda x: appearance_count[x])
            
            # Select the first 'members_needed' identifiers
            selected_members = available_list[:members_needed]
            
            # If we don't have enough unique identifiers, handle gracefully
            if len(selected_members) < members_needed:
                # This should not happen with valid inputs, but handle anyway
                print(f"Warning: Insufficient unique members for group {group_leader}")
                # Fill with duplicates (will be replaced in final pass)
                while len(selected_members) < members_needed:
                    selected_members.append(available_list[0])
            
            # Update appearance counts for selected members
            for member in selected_members:
                appearance_count[member] += 1
            
            # Sort members alphanumerically
            selected_members.sort()
            group.extend(selected_members)
            
            groupings.append((group_leader, selected_members))
        
        # Post-processing: Check balance and report statistics
        self._report_balance(appearance_count)
        
        # Attempt optimization if balance is poor (optional improvement pass)
        if self._needs_optimization(appearance_count):
            print("Attempting optimization pass for better balance...")
            groupings = self._optimize_groupings(groupings, appearance_count)
        
        # Output: Return the processed groupings
        return groupings
    
    def _report_balance(self, appearance_count: defaultdict) -> None:
        """
        Report balance statistics of the groupings.
        
        Args:
            appearance_count: Dictionary of identifier -> frequency count
        """
        if not appearance_count:
            return
        
        frequencies = list(appearance_count.values())
        min_freq = min(frequencies)
        max_freq = max(frequencies)
        avg_freq = sum(frequencies) / len(frequencies)
        
        print(f"\nBalance Statistics:")
        print(f"  Min appearances: {min_freq}")
        print(f"  Max appearances: {max_freq}")
        print(f"  Avg appearances: {avg_freq:.2f}")
        print(f"  Range: {max_freq - min_freq}")
        
        # Identify under/over represented identifiers
        under_represented = [id for id, count in appearance_count.items() 
                            if count < avg_freq - 0.5]
        over_represented = [id for id, count in appearance_count.items() 
                           if count > avg_freq + 0.5]
        
        if under_represented:
            print(f"  Under-represented (showing first 5): {under_represented[:5]}")
        if over_represented:
            print(f"  Over-represented (showing first 5): {over_represented[:5]}")
    
    def _needs_optimization(self, appearance_count: defaultdict) -> bool:
        """
        Determine if optimization is needed based on balance quality.
        
        Args:
            appearance_count: Dictionary of identifier -> frequency count
            
        Returns:
            True if optimization would be beneficial
        """
        if not appearance_count:
            return False
        
        frequencies = list(appearance_count.values())
        max_freq = max(frequencies)
        min_freq = min(frequencies)
        
        # Optimize if range is more than 2
        return (max_freq - min_freq) > 2
    
    def _optimize_groupings(self, groupings: List[Tuple[str, List[str]]], 
                           appearance_count: defaultdict) -> List[Tuple[str, List[str]]]:
        """
        Optimize groupings to improve balance using local swaps.
        
        Args:
            groupings: Current groupings
            appearance_count: Current appearance counts
            
        Returns:
            Optimized groupings
        """
        # Create mutable representation for optimization
        group_dict = {leader: members.copy() for leader, members in groupings}
        id_count = self.model.count
        
        # Simple optimization: attempt swaps for limited iterations
        for _ in range(id_count * 2):  # Limited iterations for performance
            # Find most and least frequent identifiers
            freqs = {id_: count for id_, count in appearance_count.items()}
            if not freqs:
                break
                
            most_freq_id = max(freqs, key=freqs.get)
            least_freq_id = min(freqs, key=freqs.get)
            
            # If balance is good, stop
            if freqs[most_freq_id] - freqs[least_freq_id] <= 1:
                break
            
            # Try to swap most_freq_id with least_freq_id in some group
            swapped = False
            for leader, members in group_dict.items():
                if most_freq_id in members and least_freq_id not in members and least_freq_id != leader:
                    # Swap them
                    members.remove(most_freq_id)
                    members.append(least_freq_id)
                    members.sort()
                    appearance_count[most_freq_id] -= 1
                    appearance_count[least_freq_id] += 1
                    swapped = True
                    break
            
            if not swapped:
                break
        
        # Rebuild groupings list
        optimized = [(leader, members) for leader, members in group_dict.items()]
        return optimized


def main():
    """
    Main function: Parse CLI arguments, orchestrate Backend-Model-Process pattern.
    """
    parser = argparse.ArgumentParser(
        description="Generate balanced identifier groupings where each identifier appears as group leader once."
    )
    parser.add_argument(
        'input_file',
        type=str,
        help='Path to input text file with one identifier per line'
    )
    parser.add_argument(
        '-o', '--output',
        type=str,
        default=None,
        help='Output file path (default: print to stdout)'
    )
    parser.add_argument(
        '-s', '--seed',
        type=int,
        default=None,
        help='Random seed for reproducibility'
    )
    
    args = parser.parse_args()
    
    # Set random seed for reproducibility if provided
    if args.seed is not None:
        random.seed(args.seed)
    
    try:
        # Backend: Read data
        backend = Backend(args.input_file, args.output)
        identifiers = backend.read_identifiers()
        
        # Model: Initialize and validate
        model = Model(identifiers)
        if not model.validate():
            print("Proceeding with best-effort grouping...")
        
        # Process: Generate groupings
        processor = GroupingProcessor(model)
        groupings = processor.process()
        
        # Backend: Write output
        backend.write_groupings(groupings)
        
        print(f"\nSuccessfully generated {len(groupings)} groupings.")
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}")
        return 1
    
    return 0


if __name__ == '__main__':
    exit(main())