#!/usr/bin/env python3
import os
import sys

filepath = "notebook.txt"
arguments = sys.argv[1:]

if not arguments:
    print("Use: new ou read")
    sys.exit(1)

if arguments[0] == "new":
    note_text = arguments[1]
    tag = "general"
    for arg in arguments[2:]:
        if arg.startswith("--tag="):
            tag = arg.split("=")[1]
    with open(filepath, "a") as f:
        f.write(f"{tag}:{note_text}\n")
    print(f"Salvo em {tag}")

elif arguments[0] == "read":
    tag_filter = None
    for arg in arguments[1:]:
        if arg.startswith("--tag="):
            tag_filter = arg.split("=")[1]
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            for line in f:
                t, txt = line.strip().split(":", 1)
                if tag_filter is None or t == tag_filter:
                    print(f"[{t}] {txt}")
