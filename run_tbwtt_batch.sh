#!/usr/bin/env bash
# Resilient batch runner for the remaining TBWTT languages.
# Per language, retries the full pipeline until it exits 0 (the per-paragraph
# cache makes every re-run resume from where a transient network drop killed
# it — no re-spend). Local only; does NOT deploy.
cd "$(dirname "$0")"
LANGS=(es ru ko ja zh zh-Hant)
MAX_ATTEMPTS=8
for lang in "${LANGS[@]}"; do
  echo "==================== LANGUAGE: $lang ===================="
  attempt=1
  until ./run_tbwtt_lang.sh "$lang"; do
    code=$?
    if [ "$attempt" -ge "$MAX_ATTEMPTS" ]; then
      echo "!!!! [$lang] gave up after $MAX_ATTEMPTS attempts (last exit $code) — moving on"
      break
    fi
    wait=$((attempt * 15))
    echo ">>>> [$lang] attempt $attempt failed (exit $code); resuming from cache in ${wait}s …"
    sleep "$wait"
    attempt=$((attempt + 1))
  done
  echo "==================== [$lang] settled after $attempt attempt(s) ===================="
done
echo "########## BATCH COMPLETE ##########"
