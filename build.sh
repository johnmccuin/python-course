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

# Detect current branch so notebooks fetched during Colab testing
# resolve to the right raw-file URLs.  Sources always contain "main";
# on a feature branch we rewrite the generated .ipynb files in place.
CURRENT_BRANCH="$(git -C "$REPO_ROOT" rev-parse --abbrev-ref HEAD 2>/dev/null || echo "main")"
if [[ "$CURRENT_BRANCH" == "HEAD" ]]; then
    CURRENT_BRANCH="main"   # detached HEAD (e.g. CI checkout) → use main
fi

converted=0
errors=0

# Rewrite /python-course/main → /python-course/<branch> in a generated
# notebook when we are not on main.  No-op on main.
patch_branch_url() {
    local file="$1"
    if [[ "$CURRENT_BRANCH" != "main" ]]; then
        sed -i "s|/python-course/main|/python-course/$CURRENT_BRANCH|g" "$file"
    fi
}

# GitHub's renderer (nbconvert 7.x) requires language_info.pygments_lexer
# to render notebooks. jupytext strips it via notebook_metadata_filter:-all.
# Inject a minimal but complete language_info so GitHub can render the file.
patch_language_info() {
    local file="$1"
    python3 - "$file" <<'PYEOF'
import json, sys
path = sys.argv[1]
with open(path) as f:
    nb = json.load(f)
nb.setdefault("metadata", {})
nb["metadata"]["language_info"] = {
    "name": "python",
    "version": "3.11.0",
    "mimetype": "text/x-python",
    "file_extension": ".py",
    "pygments_lexer": "ipython3",
    "codemirror_mode": {"name": "ipython", "version": 3}
}
with open(path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
    f.write("\n")
PYEOF
}

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
        patch_branch_url "$out"
        patch_language_info "$out"
        echo "  ✓  $rel  →  dist/$dir/$base.ipynb"
        ((converted++)) || true
    else
        echo "  ✗  $rel  (conversion failed)" >&2
        ((errors++)) || true
    fi
}

echo "Building notebooks (branch: $CURRENT_BRANCH)..."
if [[ "$CURRENT_BRANCH" != "main" ]]; then
    echo "  Note: raw-file URLs will point to '$CURRENT_BRANCH' instead of 'main'."
fi
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
        patch_branch_url "$local_out"
        patch_language_info "$local_out"
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
