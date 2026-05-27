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
# Excludes:
#   checks-NN.py            — plain Python module (not a jupytext notebook)
#   homework_solution-NN.py — instructor-only; never published to dist/
while IFS= read -r -d '' file; do
    convert_file "$file"
done < <(find "$REPO_ROOT" -maxdepth 2 -path "*/week-[0-9][0-9]/*.py" \
    -not -name "checks-[0-9][0-9].py" \
    -not -name "homework_solution-[0-9][0-9].py" \
    -print0 2>/dev/null | sort -z)

# homework_solution-NN.py — built in-place (next to source, not in dist/)
# The resulting .ipynb is git-ignored so it never reaches the public repo.
while IFS= read -r -d '' file; do
    local_dir="$(dirname "$file")"
    local_base="$(basename "$file" .py)"
    local_out="$local_dir/$local_base.ipynb"
    local_rel="${file#"$REPO_ROOT/"}"
    if jupytext --to notebook --output "$local_out" "$file" 2>/dev/null; then
        echo "  ✓  $local_rel  →  ${local_out#"$REPO_ROOT/"}"
        ((converted++)) || true
    else
        echo "  ✗  $local_rel  (conversion failed)" >&2
        ((errors++)) || true
    fi
done < <(find "$REPO_ROOT" -maxdepth 2 -path "*/week-[0-9][0-9]/homework_solution-[0-9][0-9].py" -print0 2>/dev/null | sort -z)

echo ""
echo "Done: $converted notebook(s) converted, $errors error(s)."

if [[ $errors -gt 0 ]]; then
    exit 1
fi
