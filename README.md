# Taste-matched picks: clickable prototype

A PM portfolio prototype for a food delivery feature: use **repeat orders**, not star ratings, as the taste signal, and show 1–3 dish picks with a one-line reason you can check. Fake data only, no backend.

Open `index.html` in a browser. On a laptop it shows a phone with a short guide beside it; on a phone it fills the screen. Demo controls sit under the app: **Restart demo**, **Simulate quiet area**, **Simulate 3rd reorder**.

## 60-second run
1. Home: tap the reason under Riya's pick → "Why this pick?"
2. Add to cart → View cart → Place order → "Order delivered"
3. Simulate 3rd reorder → "Looks like a favourite. Recommend it to your friends?" → Recommend
4. Tap your photo → Sharing & privacy → Hide a shared pick
5. Simulate quiet area → "Highly rated nearby" replaces the group section, labelled as ratings-based

Ordering Ghee roast dosa from Udupi Corner also triggers the prompt naturally, because the user has ordered it twice before.

## Privacy rules the prototype enforces
- No order counts, dates, times or prices next to a friend's name.
- Strangers only appear as a group, never by name.
- Group counts only show when the group is 20 people or more; below that, the ratings fallback appears and no count is shown.
- Only opted-in friends appear (the data includes a friend who hasn't opted in, and they never show).

## Files
- `prototype/template.html`: the page source (HTML, CSS, JS).
- `prototype/build.py`: embeds the images and writes `prototype/taste-matched-picks.html` and `index.html`. Run `python3 prototype/build.py` after editing the template.
- `prototype/assets/`: dish art and avatars. See `prototype/assets/CREDITS.md`.
