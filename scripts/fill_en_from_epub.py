#!/usr/bin/env python3
"""Retired: proportional paragraph assignment corrupts bilingual references.

Use apply_reviewed_alignment.py with an audited manifest instead.
The old implementation remains available in Git history for investigation.
"""
import sys


def main():
    sys.exit('Proportional EPUB alignment has been retired. '
             'Use scripts/apply_reviewed_alignment.py with a reviewed manifest; '
             'see reviews/lwte-alignment-2026-10-18/README.md.')


if __name__ == '__main__':
    main()
