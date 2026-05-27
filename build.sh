#!/usr/bin/env bash
# build.sh — Convert jupytext .py sources to .ipynb files in dist/
#
# Usage: bash build.sh
#
# Scans every *.py file in grader/ and week-XX/ directories,
# converts each to a Jupyter notebook, and writes the result to
# the matching path under dist/.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DIST="$REPO_ROOT/dist"

converted=0
errors=0

convert_file() {
    local src="$1"                          # e.g. grader/grader.py
    local rel="${src#"$REPO_ROOT/"}"        # e.g. grader/grader.py
    local dir
    dir="$(dirname "$rel")"                 # e.g. grader
    local base
    base="$(basename "$src" .py)"           # e.g. grader
    local out="$DIST/$dir/$base.ipynb"

    mkdir -p "$DIST/$dir"

    if jupytext --to notebook --output "$out" "$src" 2>/dev/null; then
        echo "  ✓  $rel  →  dist/$dir/$base.ipynb"
        ((converted++)) || true
    else
        echo "  ✗  $rel  (conversion failed)" >&2
        ((errors++)) || true
    fi
}

echo "Building notebooks..."
echo ""

# grader/
while IFS= read -r -d '' file; do
    convert_file "$file"
done < <(find "$REPO_ROOT/grader" -maxdepth 1 -name "*.py" -print0 2>/dev/null | sort -z)

# week-XX/
while IFS= read -r -d '' file; do
    convert_file "$file"
done < <(find "$REPO_ROOT" -maxdepth 2 -path "*/week-[0-9][0-9]/*.py" -print0 2>/dev/null | sort -z)

echo ""
echo "Done: $converted notebook(s) converted, $errors error(s)."

if [[ $errors -gt 0 ]]; then
    exit 1
fi
