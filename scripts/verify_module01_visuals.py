#!/usr/bin/env python3
"""Check Module 01 GitHub lesson visuals and the offline memory-hook explorer.

Zero third-party Python dependencies. Run from any working directory:
    python scripts/verify_module01_visuals.py
"""
from __future__ import annotations

import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets/module-01"
HTML = ROOT / "visuals/module-01/memory-hook-explorer.html"
LESSONS = [
    (ROOT / "content/module-01/01_AI_Basics_and_How_Machines_Learn.md", 3),
    (ROOT / "content/module-01/02_LLM_Building_Blocks_and_Model_Choices.md", 4),
]
REQUIRED_HEADINGS = [
    "Problem Statement", "Learning Objectives", "5W + H Framework",
    "Real-Life Analogy", "Memory Hook", "Visualization", "Simple Explanation",
    "Engineering Explanation", "Real Project Usage", "Python Example",
    "Complexity Discussion", "Hands-on Exercise", "Best Practices",
    "Common Mistakes", "Interview Questions", "Quick Revision", "Assignment",
    "Additional Reading", "Completion Check", "Next Topic",
]
SVG_NS = "{http://www.w3.org/2000/svg}"
failures: list[str] = []


def check(condition: bool, message: str) -> None:
    print(("PASS" if condition else "FAIL") + " " + message)
    if not condition:
        failures.append(message)


all_images: list[Path] = []
for file, required_images in LESSONS:
    content = file.read_text(encoding="utf-8")
    headings = re.findall(r"^## (.+)$", content, re.MULTILINE)
    expected = [
        f"{i + 1}. {heading}" if i < 18 else heading
        for i, heading in enumerate(REQUIRED_HEADINGS)
    ]
    check(headings == expected, f"{file.name}: 20 ordered template headings")
    images = re.findall(
        r"!\[([^\]]+)\]\((\.\./\.\./assets/module-01/[^)]+\.svg)\)",
        content,
    )
    check(len(images) == required_images, f"{file.name}: {required_images} SVG images")
    check(
        "visuals/module-01/memory-hook-explorer.html" in content,
        f"{file.name}: offline explorer linked",
    )
    for alt, relative in images:
        asset = (file.parent / relative).resolve()
        check(bool(alt.strip()) and asset.is_file(), f"{asset.name}: valid alt and path")
        all_images.append(asset)

check(len(all_images) == 7 and len(set(all_images)) == 7, "seven distinct illustrations")
for asset in sorted(set(all_images)):
    try:
        root = ET.parse(asset).getroot()
        title = root.find(SVG_NS + "title")
        desc = root.find(SVG_NS + "desc")
        check(
            root.tag == SVG_NS + "svg"
            and title is not None and bool(title.text)
            and desc is not None and bool(desc.text),
            f"{asset.name}: valid accessible SVG",
        )
    except ET.ParseError as error:
        check(False, f"{asset.name}: XML parse error: {error}")

html = HTML.read_text(encoding="utf-8")
match = re.search(r"const scenes = (\[[^\n]+\]);\nconst el", html)
check(match is not None, "offline explorer scenes JSON present")
if match:
    scenes = json.loads(match.group(1))
    check(len(scenes) == 7, "seven selectable memory stories")
    check(sum(len(scene["steps"]) for scene in scenes) == 27, "27 stepwise explanations")
    check(len({scene["slug"] for scene in scenes}) == 7, "unique scene IDs")
    for scene in scenes:
        image = ASSETS / scene["image"]
        check(
            image.resolve() in all_images and len(scene["steps"]) >= 3
            and all(
                all(step.get(key) for key in ("verb", "tech", "example", "trap"))
                for step in scene["steps"]
            ),
            f"{scene['slug']}: image and action/meaning/example/trap",
        )

check("prefers-reduced-motion" in html, "reduced-motion support")
check("aria-live" in html and 'role="status"' in html, "accessible live status")
check(all(x in html for x in ('id="prev"', 'id="next"', 'id="play"', 'id="reset"')), "playback controls")
check(all(x not in html for x in ("<script src=", "fetch(", "XMLHttpRequest")), "offline, no external scripts/network")
script = re.search(r"<script>\n([\s\S]*?)\n</script>", html)
check(script is not None, "interactive JavaScript present")
if script and shutil.which("node"):
    test = subprocess.run(
        ["node", "--check", "-"],
        input=script.group(1),
        text=True,
        capture_output=True,
        check=False,
    )
    check(test.returncode == 0, "JavaScript syntax (node --check)")
    if test.returncode != 0:
        print(test.stderr, file=sys.stderr)
else:
    print("INFO Node.js unavailable: JavaScript syntax test skipped")

if failures:
    sys.exit(f"\nFAILED: {len(failures)} visual-quality checks")
print("\nPASS: Module 01 visuals, templates and interactive explorer verified")
