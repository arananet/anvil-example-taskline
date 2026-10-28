Implementation complete. I've extended the S5 test to cover the gap:

**Added API-level test coverage for:**
- Empty title string: `{"title": ""}`
- Whitespace-only title: `{"title": "  "}`

Both now correctly assert 400 response from the API layer. All 6 tests pass. The implementation summary is in `runs/wo-gh-3/implementation.md`.
