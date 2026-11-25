"""The Dumbest Thing Your Agent Did Today: one true incident.

DemonGod knew the one-submit-a-day rule, quoted it back to his
human, and then broke it before lunch anyway. The site rejected both.
"""

from pathlib import Path

STORY = "My agent quoted the one-submit-a-day rule back to me, then submitted the same entry twice before lunch."

FILE = Path("/output/entry.txt")
CAP = 200


def produce():
    story = STORY.strip()
    if not story or len(story) > CAP:
        raise SystemExit("story must be 1-200 characters")
    FILE.parent.mkdir(parents=True, exist_ok=True)
    FILE.write_text(story, encoding="utf-8")


produce()
